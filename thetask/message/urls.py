from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='simple_response'),
    url(r'^emails/$', views.admin_emails, name='simple_response'),
]