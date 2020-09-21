from django.urls import path

from . import views

from . import views
app_name = 'website'
urlpatterns = [
    path('', views.welcome, name='welcome'),
    ]