from datetime import datetime
from app import db


class Attendance(db.Model):
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    date = db.Column(db.Date, default=datetime.utcnow().date)

    check_in = db.Column(db.DateTime)

    check_out = db.Column(db.DateTime)

    status = db.Column(
        db.String(20),
        default="Present"
    )

    employee = db.relationship(
        "Employee",
        backref="attendance_records"
    )