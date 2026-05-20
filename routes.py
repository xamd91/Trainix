from flask import render_template, request, redirect, url_for
from app import db

def register_routes(app):

    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/Training')
    def Training():
        return render_template('Training.html')
