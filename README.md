# TESRECO Internship Management Portal

A Flask and SQLite portal for managing TESRECO internship operations. The app includes intern CRUD, attendance tracking, mentor management, mentor assignment, dashboard cards, HTML pages, and JSON API endpoints.

## Folder Structure

```text
TESRECO_PORTAL/
  app.py
  database/
    db_connect.py
    init_db.py
    intern_crud.py
    attendance_crud.py
    mentor_crud.py
  routes/
    home_routes.py
    intern_routes.py
    attendance_routes.py
    mentor_routes.py
  models/
    intern.py
    mentor.py
    reports.py
  templates/
    base.html
    home.html
    dashboard.html
    about.html
    add_intern.html
    view_intern.html
    edit_intern.html
    attendance.html
    mentor.html
    assign_mentor.html
  static/
    css/style.css
    images/logo.png
  utils/
    decorators.py
    iterator.py
    generators.py
    exceptions.py
    functional.py
    copy_demo.py
    logger_config.py
  concurrency/
    multithreading_demo.py
  multiprocessing_demo.py
  interns.db
  tesreco.log
```

## Requirements

- Python 3.10+
- Flask
- SQLite

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install flask
python database/init_db.py
```

## Running Application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

## Web Routes

- `GET /` - Home page
- `GET /dashboard` - Dashboard with totals
- `GET /about` - About page
- `GET /add-intern` - Add intern form
- `POST /register-form` - Submit intern form
- `GET /view-interns` - View interns
- `GET /edit-intern/<id>` - Edit intern form
- `POST /update-intern/<id>` - Update intern
- `GET /delete-intern/<id>` - Delete intern and redirect
- `GET /attendance-page` - Attendance form and table
- `POST /attendance-form` - Submit attendance form
- `GET /mentor-page` - Mentor form and table
- `POST /mentor-form` - Submit mentor form
- `GET /assign-page` - Assignment form and table
- `POST /assign-form` - Submit mentor assignment

## API Endpoints

- `POST /register` - Register intern
- `GET /interns` - List interns
- `PUT /intern/<id>` - Update intern
- `DELETE /intern/<id>` - Delete intern
- `POST /attendance` - Add attendance
- `GET /attendance` - List attendance records
- `POST /mentor` - Add mentor
- `GET /mentors` - List mentors
- `POST /assign-mentor` - Assign mentor to intern
- `GET /assignments` - List assignments

## Features

- Flask Blueprints for route separation
- Jinja2 templates with shared base layout
- SQLite database with interns, attendance, mentors, and assignment tables
- Foreign key enforcement through SQLite pragma
- Dashboard summary cards
- Intern web CRUD workflow
- Attendance, mentor, and assignment pages
- Advanced Python examples for decorators, iterators, generators, exceptions, functional programming, copy behavior, logging, inheritance, abstract classes, multithreading, and multiprocessing
