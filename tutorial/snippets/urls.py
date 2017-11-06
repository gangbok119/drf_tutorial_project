from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.fbv.snippet_list, name='snippet_list'),
    url(r'^(?P<pk>\d+)/$',views.fbv.snippet_detail,name='snippet_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)