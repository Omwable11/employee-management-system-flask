from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required

from app import db
from app.models import Attendance, Employee

attendance = Blueprint(
    "attendance",
    __name__,
    url_prefix="/attendance"
)


@attendance.route("/")
@login_required
def index():
    records = Attendance.query.order_by(
        Attendance.date.desc()
    ).all()

    return render_template(
        "attendance/index.html",
        records=records
    )


@attendance.route("/checkin")
@login_required
def checkin():

    # Temporary until User ↔ Employee is linked
    employee = Employee.query.first()

    today = datetime.utcnow().date()

    attendance = Attendance.query.filter_by(
        employee_id=employee.id,
        date=today
    ).first()

    if attendance:
        flash("You have already checked in today.", "warning")
        return redirect(url_for("attendance.index"))

    attendance = Attendance(
        employee_id=employee.id,
        date=today,
        check_in=datetime.utcnow(),
        status="Present"
    )

    db.session.add(attendance)
    db.session.commit()

    flash("Checked in successfully!", "success")

    return redirect(url_for("attendance.index"))


@attendance.route("/checkout/<int:id>")
@login_required
def checkout(id):

    attendance = Attendance.query.get_or_404(id)

    attendance.check_out = datetime.utcnow()

    db.session.commit()

    flash("Checked out successfully!", "success")

    return redirect(url_for("attendance.index"))