from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from health_assist.web_pages.forms import InfoEditForm, InfoAddForm, PartnersAddForm
from health_assist.web_pages.models import Information, Partners


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insurances'] = Information.objects.filter(pages__name='insurances').order_by('created_at')
        return context


class PartnersDetailView(ListView):
    model = Partners
    template_name = 'pages/partners.html'
    context_object_name = 'partner'


class PartnerAddView(CreateView):
    model = Partners
    form_class = PartnersAddForm
    template_name = 'common/add-partner.html'
    success_url = reverse_lazy('partners')

def contacts(request):
    return render(request, 'pages/contacts.html')


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
