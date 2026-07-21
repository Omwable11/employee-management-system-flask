from io import BytesIO

from flask import Blueprint, send_file
from flask_login import login_required
from openpyxl import Workbook

from app.models import Employee

export = Blueprint(
    "export",
    __name__,
    url_prefix="/export"
)


@export.route("/employees")
@login_required
def employees_excel():

    wb = Workbook()

    ws = wb.active

    ws.title = "Employees"

    ws.append([
        "ID",
        "First Name",
        "Last Name",
        "Email",
        "Department",
        "Position",
        "Salary"
    ])

    employees = Employee.query.all()

    for emp in employees:

        ws.append([
            emp.id,
            emp.first_name,
            emp.last_name,
            emp.email,
            emp.department.name if emp.department else "",
            emp.position,
            emp.salary
        ])

    output = BytesIO()

    wb.save(output)

    output.seek(0)

    return send_file(
        output,
        download_name="employees.xlsx",
        as_attachment=True,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )