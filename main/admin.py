from django.contrib import admin
from.models import *
from .models import ClassSchedule, ClassAttendance, Query, QueryComment
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display=("name", "date_created", "date_modified")


admin.site.register(Course)


# Lucky assignment
admin.site.register(ClassSchedule)
admin.site.register(ClassAttendance)
admin.site.register(Query)
admin.site.register(QueryComment)
