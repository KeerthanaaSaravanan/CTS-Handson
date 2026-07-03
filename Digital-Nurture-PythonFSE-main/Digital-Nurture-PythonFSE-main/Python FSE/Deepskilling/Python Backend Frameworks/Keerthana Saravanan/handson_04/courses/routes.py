from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

# In-memory storage for courses
courses = []
next_id = 1

def make_response_json(data, status_code):
    """Create a JSON response with a status envelope."""
    response = {
        'status': 'success',
        'data': data
    }
    return jsonify(response), status_code

@courses_bp.route('/', methods=['GET'])
def get_courses():
    """Return a list of all courses."""
    return make_response_json({'courses': courses}, 200)

@courses_bp.route('/', methods=['POST'])
def create_course():
    """Create a new course."""
    global next_id
    data = request.get_json()

    # Validate required fields
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    required_fields = ['name', 'code', 'credits']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    # Create new course
    new_course = {
        'id': next_id,
        'name': data['name'],
        'code': data['code'],
        'credits': data['credits']
    }
    courses.append(new_course)
    next_id += 1

    return make_response_json(new_course, 201)

@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Return a single course by ID."""
    course = next((c for c in courses if c['id'] == course_id), None)
    if course is None:
        return jsonify({'error': 'Course not found'}), 404
    return make_response_json(course, 200)

@courses_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """Update an existing course."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    course = next((c for c in courses if c['id'] == course_id), None)
    if course is None:
        return jsonify({'error': 'Course not found'}), 404

    # Update fields if provided
    if 'name' in data:
        course['name'] = data['name']
    if 'code' in data:
        course['code'] = data['code']
    if 'credits' in data:
        course['credits'] = data['credits']

    return make_response_json(course, 200)

@courses_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """Delete a course."""
    global courses
    course = next((c for c in courses if c['id'] == course_id), None)
    if course is None:
        return jsonify({'error': 'Course not found'}), 404

    courses = [c for c in courses if c['id'] != course_id]
    return make_response_json({'message': 'Course deleted'}, 200)