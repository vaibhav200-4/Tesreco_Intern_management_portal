
# Organization: TESRECO Technologies
# Duration: 2 Days
# Objective: Evaluate Python programming, OOP, API development, database handling, and Flask web application development skills.

# Scenario

TESRECO is developing an Intern Management Portal to manage interns, mentors, projects, attendance, and performance records. You are required to build different modules of this system using Advanced Python and Flask.

## Part A: Advanced Python
1. Intern Class Design

Create an Intern class with attributes:

intern_id
name
email
domain
duration

Implement:
Constructor
Getter/Setter methods
__str__()

2. Performance Calculator

Create a function that calculates an intern's performance score.

Use a decorator to log:

Function name
Execution time
Result

3. Custom Iterator

Create an iterator that generates Intern IDs:

TES001
TES002
TES003
...

4. Generator Function

Generate internship completion certificates one at a time using a generator.

Example:

Certificate Generated for Khushi
Certificate Generated for Raushan

5. Exception Handling

Create custom exceptions:

InvalidEmailError
InvalidDurationError

Validate intern data before registration.

6. Shallow Copy vs Deep Copy

Demonstrate the difference using an Intern project list.

7. Multiple Inheritance

Create classes:

Person
Employee
Mentor

Create a class:

TESRECOMentor

using multiple inheritance.

Display MRO (Method Resolution Order).

8. Abstract Class

Create an abstract class:

Report

Methods:

generate_report()

Implement:

AttendanceReport
PerformanceReport

9. Lambda & Functional Programming

Given a list of intern scores:

[78, 90, 65, 88, 95]

Use:

map()
filter()
reduce()

to perform analysis.

10. File Handling

Store intern details in a CSV file and implement:

Add Record
Search Record
Delete Record

11. Multithreading

Create two threads:

Attendance Processing
Certificate Generation

Run simultaneously.

12. Multiprocessing

Generate performance reports for multiple interns using multiprocessing.

13. Logging

Create a log file:
tesreco.log

Store:
Login events
Errors
Report generation activities

14. SQLite Integration

Create tables:

Interns
intern_id
name
email
domain
Mentors
mentor_id
name
specialization

Perform CRUD operations.

15. Project Structure

Design a professional folder structure for the Intern Management Portal.

# Part B: Flask Development

16. TESRECO Home Page

Create:

/

Display:

Welcome to TESRECO Internship Program

with company logo and styling.

17. About TESRECO

Create:

/about

Display:

Organization Overview
Internship Domains
Mission and Vision

using Jinja templates.

18. Intern Registration API

Create:

POST /register

Input:

{
    "name":"Vaibhav",
    "email":"Vaibhav@gmail.com",
    "domain":"Data Science"
}
 
Store data in SQLite.

19. View Interns API

Create:

GET /interns

Return all registered interns in JSON format.

20. Update Intern Details

Create:

PUT /intern/<id>

Update intern information.

21. Delete Intern

Create:

DELETE /intern/<id>

Delete intern record.

22. Attendance Module

Create:

POST /attendance

Store:

Intern ID
Date
Status

23. Mentor Assignment Module

Create:

POST /assign-mentor

Assign mentors to interns.

24. Flask CRUD Web Application

Create web pages:

Add Intern
View Interns
Edit Intern
Delete Intern

using:

Flask
SQLite
Jinja2 Templates

# Submission Requirements
* Complete Source Code
* Database File (interns.db)
* Postman Collection
* README.md
* GitHub Repository Link

# All the Best!
# TESRECO Learning & Development Team