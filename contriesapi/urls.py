from django.conf.urls import url

from contriesapi import views

urlpatterns = [
    url(r'^api/contriesapi$', views.countries_list),
    url(r'^api/contriesapi/(?P<pk>[0-9]+)$', views.countries_detail)
]






