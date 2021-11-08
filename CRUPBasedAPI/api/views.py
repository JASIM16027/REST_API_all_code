from functools import partial
from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method =='GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializers = StudentSerializer(student)
            json_data = JSONRenderer().render(serializers.data)

            return HttpResponse(json_data,content_type='application/json')

        student = Student.objects.all()
        serializers = StudentSerializer(student,many=True)
        json_data = JSONRenderer().render(serializers.data)

        return HttpResponse(json_data,content_type='application/json')
    
    if request.method =='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created '}
            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type='application/json')
    if request.method=='PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        print(student)
        serializer=StudentSerializer(student, data=pythondata,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()

            res = {'msg':'Data is Saved successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
        
    if request.method=='DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        #pythondata = json.loads(request.body)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg':'Data deleted'}
       # json_data = JSONRenderer().render(res)

       # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)



