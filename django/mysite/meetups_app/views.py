from django.shortcuts import render
from django.http import HttpResponse
from .models import meetup
# Create your views here.

def index(request):

    data = meetup.objects.all()

    return render(request, 'meetups_app/index.html',{
        
        "show_meetups":False,
        "data" : data,
        
        })


def details(request,meetup_slug):

    print(meetup_slug)
    selected_meetup = meetup.objects.get(slug=meetup_slug)
    return render(request,'meetups_app/details.html',{
        "title" : selected_meetup["title"],
        "description" : selected_meetup["description"]

        })