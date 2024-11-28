from django.urls import path, include


from health_assist.web_pages.views import AboutUsDetailView, PageInfoEditView, NewsDetailView, PageInfoAddView, \
    InsuranceDetailView, delete_info, partners, contacts

urlpatterns = [
    path('about/', AboutUsDetailView.as_view(), name='about-us'),
    path('news/', NewsDetailView.as_view(), name='news'),
    path('insurance/', InsuranceDetailView.as_view(), name='insurances'),
    path('partners/', partners, name='partners'),
    path('contacts/', contacts, name='contacts'),
    path('add/', PageInfoAddView.as_view(), name='add-info'),
    path('<int:pk>/', include([
        path('edit/', PageInfoEditView.as_view(), name='edit-info'),
        path('delete/', delete_info, name='delete-info'),
    ])),
]
