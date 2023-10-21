from flask import render_template, request, url_for

class ScrapperController():
    def new_scrapper():
        return render_template('/scrapper/new_scrap.html')

    def scrapper_settings():
        return render_template('/scrapper/settings.html')