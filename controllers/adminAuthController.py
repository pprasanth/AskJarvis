from flask import render_template, request, redirect, url_for, session
from models.user import auth

def admin_login_view():
    return render_template('login.html')

def admin_login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        user = auth(request.form['username'], request.form['password'])
        if (user):
            session['loggedin'] = True
            session['userid'] = user['_id']
            session['name'] = user['name']
            session['email'] = user['email']
            message = 'Logged in successfully!'
            return redirect(url_for('admin_blueprint.dashboard'))
        else:
            message="Crendentials invalid!"
    else:
        message="Crendentials invalid!"
    return render_template('login.html', message=message)

def admin_logout():
    session.clear()
    return redirect(url_for('admin_blueprint.admin_login_view'))
