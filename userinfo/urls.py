from django.urls import path
from django.views.generic import TemplateView
from .views import UserInfoFormView, UserProfileLoginFormView, logout_user
from django.contrib.auth.decorators import login_required

app_name = 'userinfo'

urlpatterns = [
    path('register/', UserInfoFormView.as_view(), name='registration'),
    path('login/', UserProfileLoginFormView.as_view(), name='login'),
    path('logout/', login_required(logout_user), name='logout'),

]
