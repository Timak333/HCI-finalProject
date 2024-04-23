#!/usr/bin/env python

from flask import Flask, request, make_response, redirect, url_for, session
from flask import render_template

from database import Mentor, get_mentor, get_mentor_by_name, get_mentor_id_by_name, get_mentors

app = Flask(__name__)
app.secret_key = 'CPSC_HCI_2024'  # Secret key for security purposes

@app.route("/", methods=["GET"])
@app.route("/start", methods=["GET"])
def index():
    """Launch page for application"""
    session.clear()  # Clear the session at the start of the flow
    return render_template("index.html")

@app.route("/category", methods=["GET", "POST"])
def category():
    """Select mentorship category"""
    if request.method == "POST":
        session['category'] = request.form['category']
        print("command")
        if session['category'] == 'academic':
            return redirect(url_for('academic'))
        elif session['category'] == 'personal':
            return redirect(url_for('culture'))
    return render_template("category.html")

@app.route("/academic", methods=["GET", "POST"])
def academic():
    """Select mentorship focus"""
    if request.method == "POST":
        print(request.form)  # Add this line for debugging
        session['academic_focus'] = request.form.get('academic_focus')
        return redirect(url_for('major'))
    return render_template("academic.html")

@app.route("/major", methods=["GET", "POST"])
def major():
    """Select discipline"""
    if request.method == "POST":
        session['major'] = request.form.get('major')
        return redirect(url_for('matches'))
    return render_template("major.html")

@app.route("/culture", methods=["GET", "POST"])
def culture():
    """Select cultural preference"""
    if request.method == "POST":
        session['culture'] = request.form.get('culture')
        return redirect(url_for('gender'))
    return render_template("culture.html")

@app.route("/gender", methods=["GET", "POST"])
def gender():
    """Select gender"""
    if request.method == "POST":
        session['gender'] = request.form.get('gender')
        return redirect(url_for('fgli'))
    return render_template("gender.html")

@app.route("/fgli", methods=["GET", "POST"])
def fgli():
    """Select FGLI"""
    if request.method == "POST":
        session['fgli'] = request.form.get('fgli')
        return redirect(url_for('rural'))
    return render_template("fgli.html")

@app.route("/rural", methods=["GET", "POST"])
def rural():
    """Select rural"""
    if request.method == "POST":
        session['rural'] = request.form.get('rural')
        return redirect(url_for('matches'))
    return render_template("rural.html")

@app.route("/matches", methods=["GET", "POST"])
def matches():
    """Page with all matches"""
    if request.method == "POST":
        pass

    mentors = get_mentors([1, 2, 3])  # Simulated function call for example
    user_preferences = session.copy()
    return render_template("matches.html", mentors=mentors, preferences=user_preferences)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Page to contact mentor"""
    if request.method == "POST":
        mentor_name = request.form.get('name')
        mentor_email = request.form.get('email')
        mentor_description = request.form.get('description')

        selected_mentor = {
            'name': mentor_name,
            'email': mentor_email,
            'description': mentor_description
        }
        session['selected_mentor'] = selected_mentor

    mentor = session.get('selected_mentor')
    return render_template("contact.html", mentor=mentor)

# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "GET":
#         mentor_name = request.args.get('mentor')
#         mentor = get_mentor_by_name(mentor_name)
#         if mentor:
#             mentor_info = {
#                 'name': mentor.name,
#                 'email': mentor.email,
#                 'description': mentor.description
#             }
#             session['mentor_info'] = mentor_info
#             mentor = session.get('mentor_info')
#             return render_template("contact.html", mentor=mentor)
#         else:
#             return "Mentor not found", 404


@app.errorhandler(404)
def not_found(error):
    """Error page content."""
    return render_template("404.html", error_msg=str(error)), 404

if __name__ == '__main__':
    app.run(debug=True)
