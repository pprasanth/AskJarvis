from flask import render_template, request, url_for, redirect, session
from models.scrapper import ScrapperModel
import crochet

class ScrapperController():
    def new_scrapper():
        is_scrapping = True if 'scrapping' in session else False
        return render_template('/scrapper/new_scrap.html', is_scrapping = is_scrapping)

    def scrapper_settings():
        settings = ScrapperModel.fetch_settings()
        return render_template('/scrapper/settings.html', settings=settings)
    
    def save_scrapper_settings():
        if request.method == 'POST' and 'website' in request.form:
            ScrapperModel.save_settings(request.form['website'])
            success_message = "Settings saved"
            return redirect(url_for('admin_blueprint.scrapper_settings', success_message=success_message))
        else:
            error_message = "Error saving settings"
            return redirect(url_for('admin_blueprint.scrapper_settings', error_message=error_message))
        
    def start_scrapping():
        session['scrapping'] = True
        return redirect(url_for('admin_blueprint.new_scrapper'))