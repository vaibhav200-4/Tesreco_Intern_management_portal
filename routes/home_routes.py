from flask import Blueprint, render_template

from database.attendance_crud import count_attendance
from database.intern_crud import count_interns
from database.mentor_crud import count_assignments, count_mentors

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    return render_template("home.html")


@home_bp.route("/dashboard")
def dashboard():
    stats = {
        "total_interns": count_interns(),
        "total_mentors": count_mentors(),
        "attendance_records": count_attendance(),
        "assigned_mentors": count_assignments(),
    }
    return render_template("dashboard.html", stats=stats)


@home_bp.route("/about")
def about():
    return render_template("about.html")
