from django.contrib import admin
from .models import (
    About,
    Skill,
    SubSkill,
    Education,
    Company,
    Service,
    Experience, 
    Project,
    Contact
)
# Register your models here.

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(SubSkill)
admin.site.register(Education)
admin.site.register(Company)
admin.site.register(Service)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Contact)
