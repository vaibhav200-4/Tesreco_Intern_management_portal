from flask import Blueprint, jsonify, redirect, render_template, request, url_for

from database.intern_crud import (
    delete_intern,
    get_all_interns,
    get_intern_by_id,
    insert_intern,
    update_intern,
)

intern_bp = Blueprint("intern", __name__)


@intern_bp.route("/add-intern")
def add_page():
    return render_template("add_intern.html")


@intern_bp.route("/view-interns")
def view_page():
    interns = get_all_interns()
    return render_template("view_intern.html", interns=interns)


@intern_bp.route("/view-intern")
def old_view_page():
    return redirect(url_for("intern.view_page"))


@intern_bp.route("/register-form", methods=["POST"])
def register_form():
    insert_intern(
        request.form["name"],
        request.form["email"],
        request.form["domain"],
        request.form["duration"],
    )

    return redirect(url_for("intern.view_page"))


@intern_bp.route("/edit-intern/<int:id>")
def edit_intern_page(id):
    intern = get_intern_by_id(id)
    if intern is None:
        return redirect(url_for("intern.view_page"))

    return render_template("edit_intern.html", intern=intern)


@intern_bp.route("/update-intern/<int:id>", methods=["POST"])
def update_intern_form(id):
    update_intern(
        id,
        request.form["name"],
        request.form["email"],
        request.form["domain"],
        request.form["duration"],
    )

    return redirect(url_for("intern.view_page"))


@intern_bp.route("/delete-intern/<int:id>")
def delete_intern_page(id):
    delete_intern(id)
    return redirect(url_for("intern.view_page"))


@intern_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    insert_intern(
        data.get("name"),
        data.get("email"),
        data.get("domain"),
        data.get("duration"),
    )

    return jsonify({"message": "Intern registered successfully"}), 201


@intern_bp.route("/interns", methods=["GET"])
def view_interns():
    interns = get_all_interns()
    return jsonify([dict(row) for row in interns])


@intern_bp.route("/intern/<int:id>", methods=["PUT"])
def edit_intern(id):
    data = request.get_json()

    update_intern(
        id,
        data["name"],
        data["email"],
        data["domain"],
        data["duration"],
    )

    return jsonify({"message": "Updated successfully"})


@intern_bp.route("/intern/<int:id>", methods=["DELETE"])
def remove_intern(id):
    delete_intern(id)
    return jsonify({"message": "Deleted successfully"})
