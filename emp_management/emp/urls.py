
from django.contrib import admin

from django.urls import path,include

from rest_framework.routers import SimpleRouter

from .views import SkillViewSet,DeptViewSet,EmpViewSet


router = SimpleRouter()

router.register('skill',SkillViewSet)

router.register('dept',DeptViewSet)

router.register('emp',EmpViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
