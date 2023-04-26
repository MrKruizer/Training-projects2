from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('signup/', views.SignUp.as_view(), name='signup'),
]