from app import app

from flask import Blueprint, render_template, redirect, url_for

error = Blueprint("error", __name__, url_prefix="/error")

@error.route("/")
def error_template():
  return render_template('error.html'), 500

@error.errorhandler(Exception)
def handle_error(e):
  return redirect(url_for('error'))
