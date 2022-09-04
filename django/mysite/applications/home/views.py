from pydoc import resolve
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
# Create your views here.


class HomeView(View):

    template_name= "home/home.html"

    def get(self,request):

        return render(request,self.template_name)



class TestView(View):

    def get(self,request:HttpRequest):
        print("HEADERS: \n")
        print(request.headers)
        print("METHOD: \n")
        print(request.method)
        name = request.GET.get("name","")
        surname = request.GET.get("surname","")
        date = request.GET.get("date","")
        
        payload = f"{name},{surname},{date}"
        response = HttpResponse()
        response.headers={"Content-Type":"text/plain"}
        response.status_code=200
        response.content=payload
        return  response


    def post(self,request:HttpRequest):
        print("METHOD: \n")
        print(request.method)
        print("HEADERS: \n")
        print(request.headers)
        payload = json.loads(request.body)
        print(payload)

        return  JsonResponse(payload,status=201)