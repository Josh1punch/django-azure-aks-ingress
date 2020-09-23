from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting,Room
from django.shortcuts import render, get_object_or_404
def index(request):
        return render(request, 'website/Smash.html')
def date(request):
    return HttpResponse("This request was served at "+ str(datetime.now()))
#exercise add a text page to talk about myself
def about(request):
    return HttpResponse(" Hi there, this is Josh from Plano. I'm a Data Scientist and I'm enthusiastic about programming,"
                        "foods, travel and good books.")


def detail(request,id):
    meeting=get_object_or_404(Meeting,pk=id)
    #meetings the S must be same with the templates/xxxx (here is meetings)
    return render(request,"meetings/detail.html",{"meeting":meeting})

def roomdetail(request,):
    # rooms=get_object_or_404(Room) # cant use pk=id, since only one can use this!
    #meetings the S must be same with the templates/xxxx (here is meetings)
    return render(request,"website/roomDetail.html",{"rooms":Room.objects.all()})
