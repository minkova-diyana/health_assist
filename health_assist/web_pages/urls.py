from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from health_assist.web_pages.views import AboutUsDetailView, PageInfoEditView, NewsDetailView, PageInfoAddView, \
    InsuranceDetailView, delete_info, contacts, PartnersDetailView, PartnerAddView, PartnerEditView, delete_partner, \
    QuestionsDetailView

urlpatterns = [
    path('about/', AboutUsDetailView.as_view(), name='about-us'),
    path('news/', NewsDetailView.as_view(), name='news'),
    path('insurance/', InsuranceDetailView.as_view(), name='insurances'),
    path('questions/', QuestionsDetailView.as_view(), name='questions'),
    path('partners/', PartnersDetailView.as_view(), name='partners'),
    path('contacts/', contacts, name='contacts'),
    path('add/', PageInfoAddView.as_view(), name='add-info'),
    path('partner/add/', PartnerAddView.as_view(), name='partner-add'),
    path('<int:pk>/', include([
        path('edit/', PageInfoEditView.as_view(), name='edit-info'),
        path('delete/', delete_info, name='delete-info'),
    ])),
    path('partner/<int:pk>', include([
        path('edit/', PartnerEditView.as_view(), name='edit-partner'),
        path('delete/', delete_partner, name='delete-partner'),
    ])),
]
