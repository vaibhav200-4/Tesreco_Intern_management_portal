from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from database.intern_crud import get_all_interns
from database.mentor_crud import (
    assign_mentor,
    get_all_mentors,
    get_assignments,
    insert_mentor,
)

mentor_bp = Blueprint("mentor", __name__)


@mentor_bp.route("/mentor-page")
def mentor_page():
    mentors = get_all_mentors()
    return render_template("mentor.html", mentors=mentors)


@mentor_bp.route("/mentor-form", methods=["POST"])
def mentor_form():
    insert_mentor(
        request.form["name"],
        request.form["specialization"],
    )

    return redirect(url_for("mentor.mentor_page"))


@mentor_bp.route("/assign-page")
def assign_page():
    interns = get_all_interns()
    mentors = get_all_mentors()
    assignments = get_assignments()
    return render_template(
        "assign_mentor.html",
        interns=interns,
        mentors=mentors,
        assignments=assignments,
    )


@mentor_bp.route("/assign-form", methods=["POST"])
def assign_form():
    assign_mentor(
        request.form["intern_id"],
        request.form["mentor_id"],
    )

    return redirect(url_for("mentor.assign_page"))


@mentor_bp.route("/mentor", methods=["POST"])
def add_mentor():
    data = request.get_json()

    insert_mentor(
        data["name"],
        data["specialization"],
    )

    return jsonify({"message": "Mentor created"})


@mentor_bp.route("/mentors")
def mentors():
    mentors = get_all_mentors()
    return jsonify([dict(row) for row in mentors])


@mentor_bp.route("/assign-mentor", methods=["POST"])
def assign():
    data = request.get_json()

    assign_mentor(
        data["intern_id"],
        data["mentor_id"],
    )

    return jsonify({"message": "Mentor assigned"})


@mentor_bp.route("/assignments")
def assignments():
    rows = get_assignments()
    return jsonify([dict(row) for row in rows])
