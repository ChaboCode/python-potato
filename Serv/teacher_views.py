from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from . import serializers as nervERs
from .models import Teacher
from hashlib import sha256


@api_view(['POST'])
def getGroups(req):
    try:
        teacher = Teacher.objects.get(key=req.data['key'])
    except Teacher.DoesNotExist:
        return HttpResponse(status=404)
    serializer = nervERs.TeacherSerializer(teacher)
    return JsonResponse(serializer.data['subjects'], safe=False)
