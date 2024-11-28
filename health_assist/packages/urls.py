from django.urls import path

from health_assist.packages.views import UserPackage, UnderCoverage

urlpatterns = [
    path('package/', UserPackage.as_view(), name='package'),
    path('package/<int:pk>/', UnderCoverage.as_view(), name='under-package'),
]