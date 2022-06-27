from django.contrib import admin

from Project_Management.models import *

# Register your models here.

class Pro(admin.ModelAdmin):
    list_display = ('project_title','manager','approval_status')

class Rev(admin.ModelAdmin):
    list_display = ('name','rating')


admin.site.register(Project,Pro),
admin.site.register(ProjectTeam),
admin.site.register(Task),
admin.site.register(Teammember)
admin.site.register(Review,Rev)