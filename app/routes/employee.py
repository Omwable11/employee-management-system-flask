from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from sqlalchemy import or_

from app import db
from app.models import Employee
from app.forms import EmployeeForm
from app.utils.decorators import admin_required

employee = Blueprint(
    "employee",
    __name__,
    url_prefix="/employees"
)


# ===========================
# Employee List + Search
# ===========================
@employee.route("/")
@login_required
def index():
    search = request.args.get("search", "")

    if search:
        employees = Employee.query.filter(
            or_(
                Employee.first_name.ilike(f"%{search}%"),
                Employee.last_name.ilike(f"%{search}%"),
                Employee.department.ilike(f"%{search}%"),
                Employee.position.ilike(f"%{search}%"),
            )
        ).order_by(Employee.id.desc()).all()
    else:
        employees = Employee.query.order_by(Employee.id.desc()).all()

    return render_template(
        "employee/index.html",
        employees=employees,
        search=search,
    )


# ===========================
# Add Employee
# ===========================
@employee.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add():
    form = EmployeeForm()

    if form.validate_on_submit():

        employee = Employee(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            department=form.department.data,
            position=form.position.data,
            salary=form.salary.data,
            joining_date=form.joining_date.data,
        )

        db.session.add(employee)
        db.session.commit()

        flash("Employee added successfully!", "success")
        return redirect(url_for("employee.index"))

    return render_template(
        "employee/add.html",
        form=form,
    )


# ===========================
# Edit Employee
# ===========================
@employee.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(id):
    employee_obj = Employee.query.get_or_404(id)

    form = EmployeeForm(obj=employee_obj)

    if form.validate_on_submit():

        employee_obj.first_name = form.first_name.data
        employee_obj.last_name = form.last_name.data
        employee_obj.email = form.email.data
        employee_obj.phone = form.phone.data
        employee_obj.department = form.department.data
        employee_obj.position = form.position.data
        employee_obj.salary = form.salary.data
        employee_obj.joining_date = form.joining_date.data

        db.session.commit()

        flash("Employee updated successfully!", "success")
        return redirect(url_for("employee.index"))

    return render_template(
        "employee/edit.html",
        form=form,
    )


# ===========================
# Delete Employee
# ===========================
@employee.route("/delete/<int:id>")
@login_required
@admin_required
def delete(id):
    employee_obj = Employee.query.get_or_404(id)

    db.session.delete(employee_obj)
    db.session.commit()

    flash("Employee deleted successfully!", "success")

    return redirect(url_for("employee.index"))