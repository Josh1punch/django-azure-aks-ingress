from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Meeting,Room

def detail(request,id):
    meeting=get_object_or_404(Meeting,pk=id)
    #meetings the S must be same with the templates/xxxx (here is meetings)
    return render(request,"meetings/detail.html",{"meeting":meeting})

def roomdetail(request,):
    # rooms=get_object_or_404(Room) # cant use pk=id, since only one can use this!
    #meetings the S must be same with the templates/xxxx (here is meetings)
    return render(request,"meetings/roomDetail.html",{"rooms":Room.objects.all()})
