from flask import json, jsonify, abort
"""from werkzeug.wrappers import response"""
from database.operations import getTable

def __generate_json(results):
    data = []
    line = 0

    for row in results:
        r = [row.name, row.x, row.y]
        data.insert(line, r)
        line+=1
    
    response = jsonify({'data': data})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def get_json(table=True):
    if table:
        results = getTable()
        return __generate_json(results)  
    else:
        abort(404)