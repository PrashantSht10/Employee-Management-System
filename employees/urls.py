from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_form'),  # Main form page
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

