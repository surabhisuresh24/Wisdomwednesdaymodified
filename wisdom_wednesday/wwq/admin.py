from django.contrib import admin
from django import forms
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from .models import Quote, Blog, DepartmentPage, UserDetail, QuizQuestion, QuizResult
from import_export import resources, fields
from import_export.widgets import DateTimeWidget
from import_export.admin import ExportMixin

class QuizResultResource(resources.ModelResource):
    date_taken = fields.Field(column_name='date_taken', attribute='date_taken', widget=DateTimeWidget(format='%Y-%m-%d %H:%M:%S'))

    class Meta:
        model = QuizResult
        fields = ('user__name', 'user__employee_id', 'user__department', 'score', 'date_taken')

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': AdminDateWidget},
    }
    list_display = ('title', 'volume', 'part', 'published_date', 'author')
    ordering = ('volume', 'part')
    fields = ('title', 'volume', 'part', 'content', 'additional_content', 'published_date', 'week', 'image', 'additional_image', 'author', 'author_photo')

@admin.register(DepartmentPage)
class DepartmentPageAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'department', 'submission_date')

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_option')
    list_filter = ('correct_option',)

@admin.register(QuizResult)
class QuizResultAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = QuizResultResource
    list_display = ('user', 'score', 'date_taken', 'get_department')
    list_filter = ('date_taken', 'score', 'user__department')

    def get_department(self, obj):
        return obj.user.department
    get_department.short_description = 'Department'
