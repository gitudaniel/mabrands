from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from brands import views


urlpatterns = [
    url(r'^$', views.InfoList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.InfoDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
