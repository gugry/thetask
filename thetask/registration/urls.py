from django.conf.urls import include, url
from . import views

app_name = 'registration'
urlpatterns = [
    url(r'^$', views.reg_form, name='reg_form'),
    url(r'^usernamevalidate/$', views.validate_username, name='validate_username'),

]






