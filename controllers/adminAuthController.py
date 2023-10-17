from flask import render_template, request, redirect, url_for

def admin_login_view():
    return render_template('login.html')

def admin_login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        return redirect(url_for('admin_blueprint.dashboard'))
    else:
        message="Crendentials invalid!"
        return render_template('login.html', message=message)