from django.contrib import admin
from django.urls import path, re_path
from products import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/products/$', views.products_list),
    re_path(r'^api/products/(?P<pk>[0-9]+)$', views.products_detail),
]
