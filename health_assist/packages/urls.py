from django.urls import path

from health_assist.packages.views import UserPackage

urlpatterns = [
    path('package/', UserPackage.as_view(), name='package'),
]