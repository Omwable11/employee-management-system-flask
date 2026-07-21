from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class LeaveForm(FlaskForm):

    leave_type = SelectField(
        "Leave Type",
        choices=[
            ("Casual", "Casual"),
            ("Sick", "Sick"),
            ("Annual", "Annual")
        ],
        validators=[DataRequired()]
    )

    start_date = DateField(
        "Start Date",
        format="%Y-%m-%d",
        validators=[DataRequired()]
    )

    end_date = DateField(
        "End Date",
        format="%Y-%m-%d",
        validators=[DataRequired()]
    )

    reason = TextAreaField("Reason")

    submit = SubmitField("Apply Leave")