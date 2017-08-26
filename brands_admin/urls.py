from django.conf.urls import url

from brands_admin import views


urlpatterns = [
    url(r'^brands/$', views.ViewAll, name="everything"),
]
