from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.forms import ChangePasswordForm

profile = Blueprint(
    "profile",
    __name__,
    url_prefix="/profile"
)


@profile.route("/")
@login_required
def index():

    return render_template(
        "profile/index.html",
        user=current_user
    )

@profile.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():

    form = ChangePasswordForm()

    if form.validate_on_submit():

        if not check_password_hash(
            current_user.password,
            form.current_password.data
        ):
            flash("Current password is incorrect.", "danger")
            return redirect(url_for("profile.change_password"))

        current_user.password = generate_password_hash(
            form.new_password.data
        )

        db.session.commit()

        flash("Password changed successfully.", "success")

        return redirect(url_for("profile.index"))

    return render_template(
        "profile/change_password.html",
        form=form
    )