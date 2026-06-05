from django.urls import path

from health_assist.packages.views import UserPackage, UnderCoverage, UploadFilesView, UploadClaimFileView

urlpatterns = [
    path('package/', UserPackage.as_view(), name='package'),
    path('package/<int:pk>/', UnderCoverage.as_view(), name='under-package'),
    path(
        "<slug:under_package_slug>/upload/<int:document_id>/",
        UploadClaimFileView.as_view(),
        name="upload_document_ajax"
    ),
]