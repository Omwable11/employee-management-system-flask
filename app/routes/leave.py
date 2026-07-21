from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required

from app import db
from app.models import Leave, Employee
from app.forms import LeaveForm

leave = Blueprint(
    "leave",
    __name__,
    url_prefix="/leave"
)


@leave.route("/")
@login_required
def index():
    leaves = Leave.query.order_by(Leave.id.desc()).all()
    return render_template(
        "leave/index.html",
        leaves=leaves
    )


@leave.route("/apply", methods=["GET", "POST"])
@login_required
def apply():

    form = LeaveForm()

    if form.validate_on_submit():

        # Change this later when Employee is linked to User
        employee = Employee.query.first()

        leave = Leave(
            employee_id=employee.id,
            leave_type=form.leave_type.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            reason=form.reason.data,
        )

        db.session.add(leave)
        db.session.commit()

        flash("Leave applied successfully!", "success")

        return redirect(url_for("leave.index"))

    return render_template(
        "leave/apply.html",
        form=form
    )

    from flask_login import login_required
from app.utils.decorators import admin_required


@leave.route("/approve/<int:id>")
@login_required
@admin_required
def approve(id):
    leave_request = Leave.query.get_or_404(id)

    leave_request.status = "Approved"

    db.session.commit()

    flash("Leave approved successfully.", "success")

    return redirect(url_for("leave.index"))


@leave.route("/reject/<int:id>")
@login_required
@admin_required
def reject(id):
    leave_request = Leave.query.get_or_404(id)

    leave_request.status = "Rejected"

    db.session.commit()

    flash("Leave rejected successfully.", "danger")

    return redirect(url_for("leave.index"))