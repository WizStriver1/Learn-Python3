#!/usr/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api
import json, webbrowser

app = Flask(__name__)
api = Api(app)

class Helloword(Resource):

    def get(self):
        return {'Hello': 'World'}

    def post(self):
        req = request
        data = request.data
        form = json.dumps(request.form)
        print({'data': data, 'form': form})

        return {'data': data, 'form': form}

api.add_resource(Helloword, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6100, debug=True)