from django.urls import path, re_path, include
from django.contrib import admin
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
    path('', views.index),
    path('home', views.home),
    path('login', views.login),
    re_path(r'^about/contact', views.contact, name='contact'),
    re_path(r'^about', views.about, kwargs={'name':'Dudde', 'age':100500} , name='about'),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', views.user, name='user'),
    re_path(r'^user/(?P<name>\D+)', views.user, name='user'),
    re_path(r'^user', views.user, name='user'),
    re_path(r'^products/(?P<id>\D+)/', include(product_patterns)),
    re_path(r'^products/', include(products_patterns)),
    re_path(r'^dudde',views.getter),
    re_path(r'^access/(?P<age>\d+)', views.access),
    re_path(r'^nope', views.go_out),
    re_path(r'^json', views.json_resp),
    re_path(r'^get_cookie', views.get_cookie),
    re_path(r'^set_cookie', views.set_cookie),
]
