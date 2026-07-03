from rest_framework import serializers
from .models import Department, Course, Student, Enrollment

# ModelSerializers automatically generate a set of fields for you based on the model.
# They also automatically generate validators for the model fields, such as unique_together.
# You can declare which fields to include; using '__all__' includes every field in the model.

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'