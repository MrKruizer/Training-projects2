from welcome_page.models import Person, Course, Grade
from django.contrib import admin

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display = ("last_name", "first_name")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ("name", "year")

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
	pass

