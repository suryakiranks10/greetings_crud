from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        response_data={"meaasage":"hello world"}

        return JsonResponse(response_data)

class GoodMorningView(View):
    def get(self,request):
        response_data={"meaasage":"good morning"}

        return JsonResponse(response_data)

class GoodEveningView(View):
    def get(self,request):
        response_data={"meaasage":"good evening"}

        return JsonResponse(response_data)

class GoodNightView(View):
    def get(self,request):
        response_data={"meaasage":"good night"}

        return JsonResponse(response_data)

class GoodafternoonView(View):
    def get(self,request):
        response_data={"meaasage":"good afternoon"}

        return JsonResponse(response_data)

