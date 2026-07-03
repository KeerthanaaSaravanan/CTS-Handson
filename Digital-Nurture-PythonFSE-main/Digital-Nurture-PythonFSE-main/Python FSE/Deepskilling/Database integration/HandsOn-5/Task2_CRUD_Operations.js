// ==========================================================
// Digital Nurture 5.0
// Module 3 - Database Integration
// Hands-On 5
// Task 2 : CRUD Operations
// ==========================================================

use("college_nosql");

// Find all feedback with rating >= 4

print("\n----- Feedback with Rating >= 4 -----");

db.feedback.find({
    rating: { $gte: 4 }
}).forEach(printjson);


// Find all feedback for CS101

print("\n----- Feedback for CS101 -----");

db.feedback.find({
    course_code: "CS101"
}).forEach(printjson);


// Find feedback containing the tag 'challenging'

print("\n----- Feedback tagged as 'challenging' -----");

db.feedback.find({
    tags: "challenging"
}).forEach(printjson);

// Update rating of student_id = 5
print("\n----- Updating Rating -----");

db.feedback.find({
    student_id: 5
}).forEach(printjson);

db.feedback.find({ student_id: 5 });

// Delete documents with rating < 2

print("\n----- Deleting Low Ratings -----");

db.feedback.deleteMany({
    rating: { $lt: 2 }
});

print("\nRemaining Documents:");

print("Total Documents: " + db.feedback.countDocuments());
