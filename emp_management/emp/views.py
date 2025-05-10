from django.shortcuts import render

from rest_framework import viewsets

from .models import Skill,Dept,Emp

from .serializers import SkillSerializers,DeptSerializers,EmpSerializers

# Create your views here.

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class= SkillSerializers


class DeptViewSet(viewsets.ModelViewSet):
    queryset = Dept.objects.all()
    serializer_class= DeptSerializers


class EmpViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class= EmpSerializers


