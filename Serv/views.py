from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . import serializers as nervERs
from .models import Student


def hello_nerv(req):
    students = Student.objects.all()
    return render(req, 'Serv/hello_nerv.html', {'students': students})


@csrf_exempt
def getAllStudents(req):
    if req.method == 'GET':
        students = Student.objects.all()
        serializer = nervERs.StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif req.method == 'POST':
        data = JSONParser().parse(req)
        serializer = nervERs.StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)
