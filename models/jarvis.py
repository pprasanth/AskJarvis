from app import mongo

def listAll(search="", pageNo = 1):
    skip = (pageNo * 10) - 10
    statements = mongo.db.statements
    queryString = {}
    if search:
        queryString = { '$or': [{ 'text': { '$regex': search } }, { 'in_response_to': { '$regex': search } }] }
    else:
        queryString = { 'in_response_to': { '$exists': True, '$ne': None } }
    filtered = statements.find(queryString)
    return filtered.count(), list(filtered.skip(skip).limit(10))
