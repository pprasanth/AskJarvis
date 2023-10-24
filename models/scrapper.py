from app import mongo
import datetime

class ScrapperModel():
    def save_settings(website):
        scrap_settings = mongo.db.scrap_settings
        scrap_settings.delete_many({})
        return scrap_settings.insert_one({
            'website': website,
            'created_at': datetime.datetime.now(),
        })
    
    def fetch_settings():
        scrap_settings = mongo.db.scrap_settings
        return scrap_settings.find_one()