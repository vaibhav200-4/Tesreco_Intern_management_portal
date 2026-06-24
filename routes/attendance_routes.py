from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from database.attendance_crud import add_attendance, get_attendance
from database.intern_crud import get_all_interns

attendance_bp = Blueprint("attendance", __name__)


@attendance_bp.route("/attendance-page")
def attendance_page():
    interns = get_all_interns()
    records = get_attendance()
    return render_template("attendance.html", interns=interns, records=records)


@attendance_bp.route("/attendance-form", methods=["POST"])
def attendance_form():
    add_attendance(
        request.form["intern_id"],
        request.form["date"],
        request.form["status"],
    )

    return redirect(url_for("attendance.attendance_page"))


@attendance_bp.route("/attendance", methods=["POST"])
def attendance():
    data = request.get_json()

    add_attendance(
        data["intern_id"],
        data["date"],
        data["status"],
    )

    return jsonify({"message": "Attendance added"})


@attendance_bp.route("/attendance", methods=["GET"])
def attendance_list():
    rows = get_attendance()
    return jsonify([dict(row) for row in rows])
