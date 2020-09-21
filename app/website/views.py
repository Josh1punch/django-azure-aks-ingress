from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.
from meetings.models import Meeting,Room
#this welcome func here is returning a website only
# def welcome(request):
#     return HttpResponse("Welcome to Josh Mtg Planner~~!")

#in order to use welcome html template, we shall use render to call the template
# the 2nd para is the name and path pf the template, since we are under the website folder, we just need fill in the folder inside templates
#to get the html.
def welcome(request):
    # return render(request,"website/welcome.html")
    return render(request,"website/Smash.html",
                  #{"msg":"This is a call from welcome in views"},
                  {"meetings":Meeting.objects.all()}
                 # {"rooms":Room.objects.all()}
                  )

# def getRoom(request):
#     # return render(request,"website/welcome.html")
#     return render(request,"website/roomDetail.html",
#                   #{"msg":"This is a call from welcome in views"},
#                   {"rooms":Room.objects.all()}
#                  # {"rooms":Room.objects.all()}
#                   )
def date(request):
    return HttpResponse("This request was served at "+ str(datetime.now()))
#exercise add a text page to talk about myself
def about(request):
    return HttpResponse(" Hi there, this is Josh from Plano. I'm a Data Scientist and I'm enthusiastic about programming,"
                        "foods, travel and good books.")
