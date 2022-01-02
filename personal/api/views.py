from rest_framework import viewsets
from .serializers import AboutSerializer, SkillSerializer
from ..models import About, Skill, SubSkill

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()#.order_by('name')
    serializer_class = AboutSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

