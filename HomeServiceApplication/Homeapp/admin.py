from django.contrib import admin
from .models import skill,addSkill,addWork,WorkResponses
# Register your models here.

admin.site.register(skill)
admin.site.register(addSkill)
admin.site.register(addWork)
admin.site.register(WorkResponses)
