from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class Test(APIView):
    def get(self,request,*args,**kwargs):
     return Response({"apple":"dsd"})



class Index(APIView):
    def get(self,request,*args,**kwargs):
     return render(request,'index.html')
