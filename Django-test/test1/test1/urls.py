"""
URL configuration for test1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from welcome_page import views

products_patterns = [
    path('',views.products),
    re_path('^new', views.new),
    re_path('^top', views.top),
]
product_patterns = [
    path('',views.product),
    re_path(r'^questions', views.questions),
    re_path(r'^comments', views.comments),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    re_path(r'^about/contact', views.contact, name='contact'),
    re_path(r'^about', views.about, kwargs={'name':'Dudde', 'age':100500} , name='about'),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', views.user, name='user'),
    re_path(r'^user/(?P<name>\D+)', views.user, name='user'),
    re_path(r'^user', views.user, name='user'),
    re_path(r'^products/(?P<id>\D+)/', include(product_patterns)),
    re_path(r'^products/', include(products_patterns)),
    re_path(r'^dudde/',views.getter),
    re_path(r'^access/(?P<age>\d+)', views.access),
]
