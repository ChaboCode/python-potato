from django.contrib import admin
from .models import Teacher, Group, Subject, Student, GroupRegisters

admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(GroupRegisters)
