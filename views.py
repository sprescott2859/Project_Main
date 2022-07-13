from flask import Flask, render_template, Blueprint, redirect, url_for


my_view = Blueprint('my_view', __name__)

@my_view.route('/index')
def index():
    return render_template("index.html")

@my_view.route('/home')
def index():
    return render_template("home.html")

@my_view.route('/page1')
def about():
    return render_template("page1.html")

@my_view.route('/page2')
def about():
    return render_template("page2.html")

@my_view.route('/page3')
def about():
    return render_template("page3.html")

@my_view.route('/page4')
def about():
    return render_template("page4.html")

@my_view.route('/home')
def about_redirect():
    return redirect(url_for("my_view.home"))