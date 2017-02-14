"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from account import views

urlpatterns = [
    url(r'^register/$', views.UserCreateView.as_view()),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^info/$', views.UserInfoView.as_view()),
    url(r'^change_password/$', views.ChangePasswordView.as_view()),
    url(r'^find_password/$', views.FindPasswordView.as_view()),
    url(r'^reset_password/(?P<url_token>[0-9a-f]{64})/$', views.ResetPasswordView.as_view()),
    
    url(r'', include('rest_framework_social_oauth2.urls'))
]
