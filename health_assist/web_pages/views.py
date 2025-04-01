from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from health_assist.web_pages.forms import InfoEditForm, InfoAddForm, PartnersAddForm, PartnersEditForm, ContactForm
from health_assist.web_pages.models import Information, Partners, InsuranceTypes
from health_assist.web_pages.signals import contact_form_submitted


# Create your views here.
class AboutUsDetailView(ListView):
    model = Information
    template_name = 'pages/about-us.html'
    context_object_name = 'about_us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = Information.objects.filter(pages__name='about-us').first()
        return context


class NewsDetailView(ListView):
    model = Information
    template_name = 'pages/news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = Information.objects.filter(pages__name='news').order_by('-created_at')
        return context


class InsuranceDetailView(ListView):
    model = Information
    template_name = 'pages/insurances.html'
    context_object_name = 'insurances'

    def get_queryset(self):
        return Information.objects.filter(pages__name='insurances').order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        types = InsuranceTypes.objects.values_list("id", "translations__type_insurance")
        context['insurance_groups'] = {
            insurance_type: context['insurances'].filter(type_insurance=id_type)
            for id_type, insurance_type in types
        }

        return context


class QuestionsDetailView(ListView):
    model = Information
    template_name = 'pages/questions.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Information.objects.filter(pages__name='questions').order_by('-created_at')


class PageInfoAddView(CreateView):
    model = Information
    form_class = InfoAddForm
    template_name = 'common/add-info.html'
    context_object_name = 'info'

    def get_success_url(self):
        page_name = self.object.pages.name
        return reverse_lazy(page_name)


class PageInfoEditView(UpdateView):
    model = Information
    form_class = InfoEditForm
    template_name = 'common/edit-info.html'
    context_object_name = 'info'

    def get_success_url(self):
        page_name = self.object.pages.name
        return reverse_lazy(page_name)


def delete_info(request, pk):
    news = Information.objects.get(pk=pk)
    news.delete()
    return redirect(request.META.get('HTTP_REFERER'))


class PartnersDetailView(ListView):
    model = Partners
    template_name = 'pages/partners.html'
    context_object_name = 'partner'


class PartnerAddView(CreateView):
    model = Partners
    form_class = PartnersAddForm
    template_name = 'common/add-partner.html'
    success_url = reverse_lazy('partners')


class PartnerEditView(UpdateView):
    model = Partners
    form_class = PartnersEditForm
    template_name = 'common/edit-partner.html'
    context_object_name = 'partner'
    success_url = reverse_lazy('partners')


def delete_partner(request, pk):
    partner = Partners.objects.get(pk=pk)
    partner.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def contacts(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        contact_form_submitted.send(
            sender=ContactForm,
            **form.cleaned_data
        )
        return redirect('contacts')
    context = {'form': form}
    return render(request, 'pages/contacts.html', context)
