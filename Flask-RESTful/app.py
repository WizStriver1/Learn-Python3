#!/usr/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Helloword(Resource):
    
    def get(self):
        return {'Hello': 'World'}

api.add_resource(Helloword, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6100, debug=True)