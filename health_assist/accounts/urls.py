from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from health_assist.accounts.views import RegisterView, ProfileUpdateView, ProfileDetailsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', include([
        path('', ProfileDetailsView.as_view(), name='profile'),
        path('<int:pk>/', ProfileUpdateView.as_view(), name='profile-edit'),
    ]))
]