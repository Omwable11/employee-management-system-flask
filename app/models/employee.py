from app import db


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    phone = db.Column(db.String(15))

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=True
    )

    position = db.Column(db.String(100))

    salary = db.Column(db.Float)

    joining_date = db.Column(db.Date)

    def __repr__(self):
        return f"<Employee {self.first_name} {self.last_name}>"