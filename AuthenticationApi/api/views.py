"""
from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print('**********List********************')
        print('basename : ',self.basename)
        print('action : ',self.action)
        print('Detail : ',self.detail)
        print('Suffix : ', self.suffix)
        print('Name : ', self.name)
        print('Description : ', self.description)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        print('**********Retrieve********************')
        print('basename : ',self.basename)
        print('action : ',self.action)
        print('Detail : ',self.detail)
        print('Suffix : ', self.suffix)
        print('Name : ', self.name)
        print('Description : ', self.description)
        
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def create(self,request):
        print('**********create********************')
        print('basename : ',self.basename)
        print('action : ',self.action)
        print('Detail : ',self.detail)
        print('Suffix : ', self.suffix)
        print('Name : ', self.name)
        print('Description : ', self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully!!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        print('**********update********************')
        print('basename : ',self.basename)
        print('action : ',self.action)
        print('Detail : ',self.detail)
        print('Suffix : ', self.suffix)
        print('Name : ', self.name)
        print('Description : ', self.description)
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data updated Successfully!!'})

    def destroy(self,request,pk):
        print('**********delete********************')
        print('basename : ',self.basename)
        print('action : ',self.action)
        print('Detail : ',self.detail)
        print('Suffix : ', self.suffix)
        print('Name : ', self.name)
        print('Description : ', self.description)
       
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'msg':'Data deleted Successfully!!'})
"""
# ReadOnlyModelViewSet class
"""

from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset  = Student.objects.all()
    serializer_class = StudentSerializer
"""
"""
# Authentication and Permission


from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset  = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]
"""

# Session Authentication and Permission 

from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset  = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    #permission_classes = [IsAdminUser]
