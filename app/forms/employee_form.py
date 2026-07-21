from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    FloatField,
    DateField,
    SubmitField
)
from wtforms.validators import DataRequired, Email


class EmployeeForm(FlaskForm):

    first_name = StringField(
        "First Name",
        validators=[DataRequired()]
    )

    last_name = StringField(
        "Last Name",
        validators=[DataRequired()]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    phone = StringField("Phone")

    department = StringField("Department")

    position = StringField("Position")

    salary = FloatField("Salary")

    joining_date = DateField(
        "Joining Date",
        format="%Y-%m-%d"
    )

    submit = SubmitField("Save Employee")
    