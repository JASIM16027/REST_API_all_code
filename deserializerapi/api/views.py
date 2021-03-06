import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        #print('json_data : ',json_data)
        stream = io.BytesIO(json_data)
        #print('stream : ',stream)
        pythondata = JSONParser().parse(stream)
        #print('pythondata : ',pythondata)
        serializer = StudentSerializer(data = pythondata)
        #print('serializer',serializer)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}

            json_data = JSONRenderer().render(res)
            #print(json_data)

            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data,contnet_type = 'application/json')
