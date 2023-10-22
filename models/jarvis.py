from app import mongo
import datetime

class JarvisModel():
    def listAll(search="", pageNo = 1):
        skip = (pageNo * 10) - 10
        statements = mongo.db.statements
        queryString = {}
        if search:
            queryString = { '$or': [{ 'text': { '$regex': search } }, { 'in_response_to': { '$regex': search } }], 'conversation': { '$eq': 'training' } }
        else:
            queryString = { 'in_response_to': { '$exists': True, '$ne': None }, 'conversation': { '$eq': 'training' } }
        filtered = statements.find(queryString)
        return filtered.count(), list(filtered.skip(skip).limit(10))

    def create_new_tag(tageName):
        tags = mongo.db.tags
        tags.insert({
            'id': tags.count() + 1,
            'name': tageName
        })
        return True

    def listAllTags(search="", pageNo = 1):
        skip = (pageNo * 10) - 10
        tags = mongo.db.tags
        queryString = {}
        if search:
            queryString = { 'name': { '$regex': search } }
        else:
            queryString = { 'name': { '$exists': True } }
        filtered = tags.find(queryString)
        return filtered.count(), list(filtered.skip(skip).limit(10))


    def fetch_tags():
        return list(mongo.db.tags.find({ 'name': { '$exists': True } }))
    
    def fetch_response_list():
        statements = mongo.db.statements
        return list(statements.aggregate([
            {
                '$project': {
                    'text': 1
                }
            }, {
                '$group': {
                    '_id': '$text', 
                    'count': {
                        '$sum': 1
                    }
                }
            }, {
                '$sort': {
                    '_id': 1
                }
            }, {
                '$project': {
                    '_id': 0,
                    'response': '$_id'
                }
            }
        ]))
    
    def create_new_training(text, search_text, conversation, in_response_to, search_in_response_to, persona, tags):
        created_at = datetime.datetime.now()
        statements = mongo.db.statements
        return statements.insert_one({
            'text': text,
            'search_text': search_text,
            'conversation': conversation,
            'persona': persona,
            'in_response_to': in_response_to,
            'search_in_response_to': search_in_response_to,
            'tags': tags,
            'created_at': created_at,
        })

