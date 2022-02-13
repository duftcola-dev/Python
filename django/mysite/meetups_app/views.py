from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    data = [
        {"title" : "A  first meetup app","address":"New York","slug" : "first-meet-up"},
        {"title" : "A second meetup app","address": "Barcelona","slug" : "second-meet-up"}
    ]
    return render(request, 'meetups_app/index.html',{
        
        "show_meetups":False,
        "data" : data,
        "header" : "This a meetups page",
        "heading" : "MEETUPS TITLE"
        
        })

def details(request,meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        "title" : "A first meetup",
        "description" : "this is some practice app",
    }
    return render(request,'meetups_app/details.html',{
        "title" : selected_meetup["title"],
        "description" : selected_meetup["description"]

        })