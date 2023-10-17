import hashlib
from app import mongo, app

def auth(username, password):
    md5 = hashlib.md5()
    concat_string = app.config['PASSWORD_MD5_HASH'] + password
    md5.update(concat_string.encode())
    md5_hash = md5.hexdigest()
    users = mongo.db.users
    findOne = users.find_one({'username': username, 'password': md5_hash})
    if findOne:
        return findOne
    else:
        return False
