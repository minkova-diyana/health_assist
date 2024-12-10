from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from health_assist.accounts.views import RegisterView, ProfileUpdateView, ProfileDetailsView, update_email, \
    UpdatePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', include([
        path('', ProfileDetailsView.as_view(), name='profile'),
        path('<int:pk>/', include([
            path('', ProfileUpdateView.as_view(), name='profile-edit'),
            path('email/', update_email, name='email-edit'),
        path('password/', UpdatePasswordView.as_view(), name='password'),
        ])),
    ]))
]