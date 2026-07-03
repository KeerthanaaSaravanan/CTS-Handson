from flask import Blueprint, request, jsonify
from extensions import db
from .models import Course, Student, Enrollment

courses_bp = Blueprint('courses', __name__)

# GET /api/courses/
@courses_bp.route('/', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])

# POST /api/courses/
@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    # Validate required fields
    required_fields = ['name', 'code', 'credits', 'department_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    # Check if course code already exists
    if Course.query.filter_by(code=data['code']).first():
        return jsonify({'error': 'Course code already exists'}), 400

    course = Course(
        name=data['name'],
        code=data['code'],
        credits=data['credits'],
        department_id=data['department_id']
    )
    db.session.add(course)
    db.session.commit()
    return jsonify(course.to_dict()), 201

# GET /api/courses/<int:id>
@courses_bp.route('/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict())

# PUT /api/courses/<int:id>
@courses_bp.route('/<int:id>', methods=['PUT'])
def update_course(id):
    course = Course.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    # Update fields if provided
    if 'name' in data:
        course.name = data['name']
    if 'code' in data:
        # Check if new code conflicts with another course (excluding current)
        existing = Course.query.filter_by(code=data['code']).first()
        if existing and existing.id != id:
            return jsonify({'error': 'Course code already exists'}), 400
        course.code = data['code']
    if 'credits' in data:
        course.credits = data['credits']
    if 'department_id' in data:
        course.department_id = data['department_id']

    db.session.commit()
    return jsonify(course.to_dict())

# DELETE /api/courses/<int:id>
@courses_bp.route('/<int:id>', methods=['DELETE'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course deleted successfully'}), 200

# GET /api/courses/<int:id>/students/
@courses_bp.route('/<int:id>/students/', methods=['GET'])
def get_course_students(id):
    course = Course.query.get_or_404(id)
    # Join enrollments and students to get enrolled students for this course
    students = Student.query.join(Enrollment).filter(Enrollment.course_id == id).all()
    return jsonify([student.to_dict() for student in students])