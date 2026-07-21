from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import func

from app import db
from app.models import Employee, Department, Leave, Attendance

main = Blueprint("main", __name__)


@main.route("/")
@login_required
def home():

    # Dashboard Cards
    total_employees = Employee.query.count()
    total_departments = Department.query.count()
    total_positions = db.session.query(
        func.count(func.distinct(Employee.position))
    ).scalar() or 0

    total_leaves = Leave.query.count()

    present_today = Attendance.query.filter_by(
        status="Present"
    ).count()

    # Recent Employees
    recent_employees = Employee.query.order_by(
        Employee.id.desc()
    ).limit(5).all()

    # Employees by Department (Bar Chart)
    department_data = (
        db.session.query(
            Department.name,
            func.count(Employee.id)
        )
        .outerjoin(Employee)
        .group_by(Department.id, Department.name)
        .all()
    )

    # Leave Status (Pie Chart)
    leave_data = (
        db.session.query(
            Leave.status,
            func.count(Leave.id)
        )
        .group_by(Leave.status)
        .all()
    )

    return render_template(
        "dashboard.html",
        total_employees=total_employees,
        total_departments=total_departments,
        total_positions=total_positions,
        total_leaves=total_leaves,
        present_today=present_today,
        recent_employees=recent_employees,
        department_data=department_data,
        leave_data=leave_data
    )