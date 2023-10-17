from flask import render_template, session, redirect, url_for
from models.dashboard import getTotalStatements, getYearsList

def convert_to_short_scale(number):
    if number >= 1e3:
        units = ['K', 'M', 'B', 'T']  # Add more as needed for larger numbers
        unit = ''
        for i in range(len(units)):
            if number < 10**(3 * (i + 1)):
                unit = units[i]
                number /= 10**(3 * i)
                break
        return f'{number:.1f}{unit}'
    else:
        return str(number)

def dashboard():
    if session.get('userid'):
        totalCount = getTotalStatements()
        years = getYearsList()
        return render_template(
            'dashboard.html',
            totalCount=convert_to_short_scale(totalCount),
            graphCount=totalCount,
            years=years
        )
    else:
        return redirect(url_for('admin_blueprint.admin_login_view'))