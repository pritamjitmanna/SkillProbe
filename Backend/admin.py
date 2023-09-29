from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Company,Candidate
from .Models.challengeModels import Challenge,MCQ,Coding,TestCase

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display=('email','username','is_admin')
    fieldsets=()


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.unregister(Group)


@admin.register(Candidate)
class CandidateModel(admin.ModelAdmin):
    list_display=['user']


@admin.register(Company)
class CompanyModel(admin.ModelAdmin):
    list_display=['user']

@admin.register(Challenge)
class CallengeModel(admin.ModelAdmin):
    list_display=['challenge_name','start_time','end_time']


@admin.register(MCQ)
class MCQModel(admin.ModelAdmin):
    list_display=['q_name','score','challenge']


@admin.register(Coding)
class CodingModel(admin.ModelAdmin):
    list_display=['problem_name','score','challenge']


@admin.register(TestCase)
class TestCaseModel(admin.ModelAdmin):
    list_display=['testcase_name','difficulty','problem']
