from django.urls import path
from . import views
app_name = 'website'
urlpatterns = [
    path('', views.index, name='welcome'),
     path ('rooms',views.roomdetail,name="rooms"),
     path ('date',views.date),
     path ('about',views.about,name="about"),
     path ('meetings/<int:id>',views.detail),

    ]