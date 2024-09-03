from django.contrib import admin
from .models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title']


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'students_qty')
    search_fields = ['title']
    list_filter = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
