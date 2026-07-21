from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.department import Department
from flask_login import login_required

department = Blueprint(
    "department",
    __name__,
    url_prefix="/departments"
)


@department.route("/")
@login_required
def index():
    departments = Department.query.all()
    return render_template(
        "department/index.html",
        departments=departments
    )


@department.route("/add", methods=["GET", "POST"])
@login_required
def add():

    if request.method == "POST":

        name = request.form["name"]
        description = request.form["description"]

        department = Department(
            name=name,
            description=description
        )

        db.session.add(department)
        db.session.commit()

        flash("Department added successfully.", "success")

        return redirect(url_for("department.index"))

    return render_template("department/add.html")


@department.route("/delete/<int:id>")
@login_required
def delete(id):

    department = Department.query.get_or_404(id)

    db.session.delete(department)
    db.session.commit()

    flash("Department deleted successfully.", "success")

    return redirect(url_for("department.index"))