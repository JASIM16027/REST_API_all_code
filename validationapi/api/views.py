
from django.shortcuts import render
import io
from django.views import View
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class studentAPI(View):
    def get(self, request,*args, **kwargs):
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

    def post(self, request,*args, **kwargs):
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
    
    def put(self, request,*args, **kwargs):
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


    def delete(self, request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        #pythondata = json.loads(request.body)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg':'Data deleted'}
        json_data = JSONRenderer().render(res)

        return HttpResponse(json_data, content_type='application/json')
        #return JsonResponse(res, safe=False)



