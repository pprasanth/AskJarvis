from flask import render_template, request, url_for, redirect, session
from models.scrapper import ScrapperModel

class ScrapperController():
    def new_scrapper():
        is_scrapping = True if 'scrapping' in session and session['scrapping'] == True else False
        return render_template('/scrapper/new_scrap.html', is_scrapping = is_scrapping)

    def scrapper_settings():
        settings = ScrapperModel.fetch_settings()
        return render_template('/scrapper/settings.html', settings=settings)
    
    def save_scrapper_settings():
        if request.method == 'POST':
            if ('submit' in request.form and request.form['submit'] == 'add_new'):
                ScrapperModel.add_new()
                success_message = "Added new URL"
                return redirect(url_for('admin_blueprint.scrapper_settings', success_message=success_message))
            elif ('delete' in request.form):
                ScrapperModel.delete(request.form['delete'])
                success_message = "Deleted URL"
                return redirect(url_for('admin_blueprint.scrapper_settings', success_message=success_message))
            elif 'submit' in request.form and request.form['submit'] == 'save':
                print(request.form)
                for index in range(int(request.form['count'])):
                    print(request.form['website_'+str(index+1)])
                    website = request.form['website_'+str(index+1)]
                    context = request.form['context_'+str(index+1)]
                    id = request.form['id_'+str(index+1)]
                    ScrapperModel.save_settings(website, context, id)
                success_message = "Settings saved"
                return redirect(url_for('admin_blueprint.scrapper_settings', success_message=success_message))
        else:
            error_message = "Error saving settings"
            return redirect(url_for('admin_blueprint.scrapper_settings', error_message=error_message))
        
    def start_scrapping():
        if ('scrapping' in session and session['scrapping'] == True):
            session['scrapping'] = False
        else:
            session['scrapping'] = True
        return redirect(url_for('admin_blueprint.new_scrapper'))