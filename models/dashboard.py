from app import mongo


def getTotalStatements():
    statements = mongo.db.statements
    filtered = statements.find({ 'in_response_to': { '$exists': True, '$ne': None } })
    return filtered.count()

def getYearsList():
    statements = mongo.db.statements
    return list(statements.aggregate([
        {'$project':{'year': { '$year': '$created_at' }}},
        {'$group': {'_id': "$year", 'count': { '$sum': 1 }}},
        {'$sort': { '_id': 1 }},
        {'$project': {'_id': 0,'year': '$_id'}}
    ]))