from app import mongo
import datetime
from bson.objectid import ObjectId

class ScrapperModel():
    def save_settings(website, context, id):
        scrap_settings = mongo.db.scrap_settings
        filter_criteria = {"_id": ObjectId(id)}
        update_data = {"$set": {"website": website, "context": context, 'created_at': datetime.datetime.now()}}
        return scrap_settings.update_one(filter_criteria, update_data)
    
    def fetch_settings():
        scrap_settings = mongo.db.scrap_settings
        return list(scrap_settings.find())
    
    def add_new():
        scrap_settings = mongo.db.scrap_settings
        return scrap_settings.insert_one({
            'website': '',
            'created_at': datetime.datetime.now(),
        })
    
    def delete(id):
        scrap_settings = mongo.db.scrap_settings
        return scrap_settings.delete_one({
            '_id': ObjectId(id),
        })
