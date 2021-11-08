from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# @api_view()
# def hello_func(request):
#     return Response({'msg':'Hello world'})

# @api_view(['GET'])
# def hello_func(request):
#     return Response({'msg':'Hello world'})

# @api_view(['POST'])
# def hello_func(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'This is POST request'})

@api_view(['GET','POST'])
def hello_func(request):
    if request.method=='GET':
        return Response({'msg':'This is GET request'})
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'This is POST request','data':request.data})
