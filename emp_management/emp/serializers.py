
from rest_framework import serializers

from .models import Skill,Dept,Emp

class SkillSerializers(serializers.ModelSerializer):
    class Meta :
        model = Skill
        fields = '__all__'


class DeptSerializers(serializers.ModelSerializer):
    class Meta :
        model = Dept
        fields = '__all__'

class EmpSerializers(serializers.ModelSerializer):
    class Meta :
        model = Emp
        fields = '__all__'



