from app import app

from flask import Blueprint, render_template, redirect, url_for

error = Blueprint("error", __name__, url_prefix="/error")

@error.route("/")
def error_template(error=""):
  return render_template('error.html', error=error), 500

@app.errorhandler(Exception)
def handle_error(error):
  return error_template(error)

