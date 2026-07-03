// ==========================================================
// Digital Nurture 5.0
// Module 3 - Database Integration
// Hands-On 5
// Task 1 : Create Collection and Insert Documents
// ==========================================================

// Create Database
use("college_nosql");

// Create Collection
db.createCollection("feedback")

// Insert Sample Documents
db.feedback.insertMany([

{
student_id:1,
course_code:"CS101",
semester:"2022-ODD",
rating:5,
comments:"Excellent teaching.",
tags:["challenging","well-structured","good-examples"],
submitted_at:new Date("2022-11-30"),
attachments:[
{
filename:"notes.pdf",
size_kb:240
}
]
},

{
student_id:2,
course_code:"CS101",
semester:"2022-ODD",
rating:4,
comments:"Very informative.",
tags:["challenging","interesting"],
submitted_at:new Date("2022-11-25"),
attachments:[
{
filename:"assignment.pdf",
size_kb:180
}
]
},

{
student_id:3,
course_code:"CS101",
semester:"2022-ODD",
rating:5,
comments:"Loved the practical sessions.",
tags:["challenging","practical"],
submitted_at:new Date("2022-11-28"),
attachments:[
{
filename:"lab.pdf",
size_kb:210
}
]
},

{
student_id:4,
course_code:"CS102",
semester:"2022-ODD",
rating:3,
comments:"Good course.",
tags:["database","sql"],
submitted_at:new Date("2022-11-20"),
attachments:[
{
filename:"db.pdf",
size_kb:200
}
]
},

{
student_id:5,
course_code:"CS102",
semester:"2022-ODD",
rating:2,
comments:"Needs more examples.",
tags:["database"],
submitted_at:new Date("2022-11-21"),
attachments:[
{
filename:"review.pdf",
size_kb:120
}
]
},

{
student_id:6,
course_code:"EC101",
semester:"2021-EVEN",
rating:4,
comments:"Interesting.",
tags:["electronics"],
submitted_at:new Date("2021-12-15"),
attachments:[
{
filename:"ec.pdf",
size_kb:140
}
]
},

{
student_id:7,
course_code:"ME101",
semester:"2022-ODD",
rating:5,
comments:"Very engaging.",
tags:["mechanical"],
submitted_at:new Date("2022-11-26"),
attachments:[
{
filename:"me.pdf",
size_kb:170
}
]
},

{
student_id:8,
course_code:"CS103",
semester:"2022-ODD",
rating:1,
comments:"Too difficult.",
tags:["oop"],
submitted_at:new Date("2022-11-18"),
attachments:[
{
filename:"oop.pdf",
size_kb:90
}
]
},

{
student_id:9,
course_code:"CS103",
semester:"2022-ODD",
rating:4,
comments:"Useful course.",
tags:["oop","coding"],
submitted_at:new Date("2022-11-22"),
attachments:[
{
filename:"code.pdf",
size_kb:150
}
]
},

// No attachments field 
{
student_id:10,
course_code:"ME101",
semester:"2022-ODD",
rating:5,
comments:"Excellent faculty.",
tags:["mechanical","practical"],
submitted_at:new Date("2022-11-27")
}

]);


// Verify Count
db.feedback.countDocuments()