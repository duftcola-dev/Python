from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.views import View
# Create your views here.

class Test(View):

    def get(request,*args,**kwargs):
        return JsonResponse({"Ok":1})
