// ==========================================================
// Digital Nurture 5.0
// Module 3 - Database Integration
// Hands-On 5
// Task 3 : Aggregation Pipeline
// ==========================================================
use("college_nosql");

// Average rating for each course

db.feedback.aggregate([
{
    $group:{
        _id:"$course_code",
        average_rating:{$avg:"$rating"}
    }
}]).forEach(printjson);

// Total feedback for each course

db.feedback.aggregate([
{
    $group:{
        _id:"$course_code",
        total_feedback:{$sum:1}
    }
}]).forEach(printjson);

// Courses with average rating greater than 4

db.feedback.aggregate([
{
    $group:{
        _id:"$course_code",
        average_rating:{$avg:"$rating"}
    }
},
{
    $match:{
        average_rating:{$gt:4}
    }
}]).forEach(printjson);

// Top 3 highest-rated courses

db.feedback.aggregate([
{
    $group:{
        _id:"$course_code",
        average_rating:{$avg:"$rating"}
    }
},
{
    $sort:{
        average_rating:-1
    }
},
{
    $limit:3
}
]).forEach(printjson);

// Count frequency of each tag

db.feedback.aggregate([
{
    $unwind:"$tags"
},
{
    $group:{
        _id:"$tags",
        count:{$sum:1}
    }
},
{
    $sort:{
        count:-1
    }
}]).forEach(printjson);