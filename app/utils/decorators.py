from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Please login first.", "warning")
            return redirect(url_for("auth.login"))

        if current_user.role != "admin":
            flash("You don't have permission to access this page.", "danger")
            return redirect(url_for("main.home"))

        return f(*args, **kwargs)

    return decorated_function