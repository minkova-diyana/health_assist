from django.urls import path

from health_assist.packages.views import UserPackage, UnderCoverage, UploadFilesView

urlpatterns = [
    path('package/', UserPackage.as_view(), name='package'),
    path('package/<int:pk>/', UnderCoverage.as_view(), name='under-package'),
    path('upload/<slug:under_package_slug>/<int:document_id>/', UploadFilesView.as_view(), name='upload_document'),
]