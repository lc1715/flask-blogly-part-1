
"""Blogly application."""
from flask import Flask, redirect, request, render_template, session, flash
from models import db, connect_db, User
from sqlalchemy.sql import text

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)        


@app.route('/')
def homepage():
    """Redirect to '/users' which will show a list of all users in db"""

    return redirect('/users')


@app.route('/users')
def show_users():
    """Show list of all users in db and can click on user's name to get user's information"""

    users = User.query.all()
    return render_template('show_users.html', users=users)
   

@app.route('/users/new')
def add_user_form():
    """Shows the add user form. Show a form to create a new user, object(instance)"""

    return render_template('add_user_form.html')


@app.route('/users/new', methods=["POST"])
def add_user():
    """To create a new user, instance(object)"""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    image_url = image_url if image_url else None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')


@app.route('/users/<user_id>')
def user_details(user_id):
    """Show the details about that particular user"""

    user = User.query.get_or_404(user_id)     
    return render_template('user_details.html', user=user)


@app.route('/user/<user_id>/edit')
def edit_user_form(user_id):
    """Get the user's object(instance) and show the edit user form"""

    user = User.query.get_or_404(user_id)
    return render_template('edit_user_form.html', user=user)


@app.route('/users/<user_id>/edit', methods=["POST"])
def edit_user(user_id):
    """Update the user's information"""

    user = User.query.get_or_404(user_id)

    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()
    return redirect ('/users')


@app.route('/users/<user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Delete a user"""

    User.query.filter_by(id = user_id).delete()     
    db.session.commit()
    return redirect('/users')
