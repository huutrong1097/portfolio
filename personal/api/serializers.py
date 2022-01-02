from ..models import About, Skill, SubSkill
from rest_framework import fields, serializers

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class SubSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSkill
        fields = ['id', 'skill','percentage']
class SkillSerializer(serializers.ModelSerializer):
    subskill = SubSkillSerializer(many= True, read_only=True)
    class Meta:
        model = Skill
        fields = ['id','title', 'year_of_experience', 'subskill']