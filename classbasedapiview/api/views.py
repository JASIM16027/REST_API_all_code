# from django.shortcuts import render
# import io
# from django.views import View
# from .serializers import StudentSerializer
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from .models import Student
# from django.http import HttpResponse,JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# @method_decorator(csrf_exempt,name='dispatch')
# class studentAPI(View):
#     def get(self, request,*args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             student = Student.objects.get(id=id)
#             serializers = StudentSerializer(student)
#             json_data = JSONRenderer().render(serializers.data)

#             return HttpResponse(json_data,content_type='application/json')

#         student = Student.objects.all()
#         serializers = StudentSerializer(student,many=True)
#         json_data = JSONRenderer().render(serializers.data)

#         return HttpResponse(json_data,content_type='application/json')

#     def post(self, request,*args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = pythondata)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data created '}
#             json_data = JSONRenderer().render(res)

#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)

#         return HttpResponse(json_data, content_type='application/json')
    
#     def put(self, request,*args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         student = Student.objects.get(id=id)
#         print(student)
#         serializer=StudentSerializer(student, data=pythondata,partial=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()

#             res = {'msg':'Data is Saved successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')


#     def delete(self, request,*args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         #pythondata = json.loads(request.body)
#         id = pythondata.get('id')
#         student = Student.objects.get(id=id)
#         student.delete()
#         res = {'msg':'Data deleted'}
#        # json_data = JSONRenderer().render(res)

#        # return HttpResponse(json_data, content_type='application/json')
#         return JsonResponse(res, safe=False)
#================================================================================


# from django.shortcuts import render
# from rest_framework import serializers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerializer

# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request):
#     if request.method =='GET':
#         print(request.data)
#         id = request.data.get('id')
#         if id is not None:
#             student = Student.objects.get(id=id)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)

#     if request.method=='POST':
#         print(request.data)
#         serializer = StudentSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data created'})
#         return Response(serializer.errors)
#     if request.method =='PUT':
#         id = request.data.get('id')
#         student = Student.objects.get(pk=id)
#         serializer = StudentSerializer(student, data=request.data,partial = True)
#         if serializer.is_valid():
#             serializer.save()

#             return Response({'msg':'Data updated Successfully '})
#         return Response(serializer.errors)

#     if request.method =='DELETE':
#         id = request.data.get('id')
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response({'msg':'Data deleted Successfully'})




from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

class StudentAPI(APIView):
    def get(self,request,pk=None, format=None):
        print(request.data)
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        print(request.data)
        serializer = StudentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None, format=None):
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg':' Complete Data updated Successfully '})
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg':' Partial Data updated Successfully '})
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        id= pk
       
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'msg':'Data deleted Successfully'})





    
    
        










