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
