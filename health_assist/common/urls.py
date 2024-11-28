from django.urls import path


from health_assist.common.views import HealthHomeView, home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('health-assist/', HealthHomeView.as_view(), name='health-home'),
]