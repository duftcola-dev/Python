from django.urls import path
from . import views

urlpatterns = [
    path("meetups/",views.index,name="index_meetup_page"),  # our-domain.com/meetups
    path("meetups/<slug:meetup_slug>",views.details,name="meetup_details_page") # a dynamic url-path-segment
]