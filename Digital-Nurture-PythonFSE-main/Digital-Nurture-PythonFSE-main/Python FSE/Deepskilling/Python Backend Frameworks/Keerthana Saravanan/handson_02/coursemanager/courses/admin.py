from django.contrib import admin
from .models import Department, Course, Student, Enrollment

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_dept', 'budget')
    search_fields = ('name',)
    list_filter = ('head_of_dept',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'credits', 'department']
    search_fields = ['name', 'code']
    list_filter = ['department']
    # list_display: specifies which fields to display in the list view of the admin.
    # search_fields: enables a search box that filters results based on the given fields.
    # list_filter: adds filters in the right sidebar of the admin list page.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'enrollment_year')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'enrollment_year')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'grade')
    search_fields = ('student__first_name', 'student__last_name', 'course__name', 'course__code')
    list_filter = ('enrollment_date', 'grade', 'course__department')
    # To prevent duplicate enrollments via admin, we rely on the model's unique_together constraint.
    # Django's ModelForm will raise a validation error if a duplicate is attempted.
