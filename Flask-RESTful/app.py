#!/usr/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api
import json, webbrowser, os
from datetime import datetime

app = Flask(__name__)
api = Api(app)

def time2str():
    d = datetime.now()
    return d.strftime("%y-%m-%d-%H-%M-%S")

def detect_newname(filepath, index=1):
    filename, file_extension = os.path.splitext(filepath)
    new_path = filename + '_' + str(index) + file_extension
    if os.path.exists(new_path):
        return detect_newname(filepath, index + 1)
    return new_path

def new_filename(filepath, index=1):
    if os.path.exists(filepath):
        return detect_newname(filepath)
    return filepath

def write2file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

class Helloword(Resource):

    def get(self):
        return {'Hello': 'World'}

    def post(self):
        req = request
        data = request.data
        form = json.dumps(request.form)
        print({'data': data, 'form': form})

        return {'data': data, 'form': form}

class Base64(Resource):
    def post(self):
        form_data = request.form
        data = request.data
        timestr = time2str()
        img_filename = new_filename('uploads/base64_%s.jpg' % timestr)
        text_filename = new_filename('uploads/base64_%s.txt' % timestr)
        if not data:
            if form_data.get('base64'):
                data = form_data.get('base64')
                self.base642img(data, img_filename)
                write2file(data.encode('base64'), text_filename)
                status, img = True, '/' + img_filename
            else:
                status, img = False, ''

        result = {
            'status': status,
            'img': img
        }


        return result

    def base642img(self, data, filename):
        with open(filename, 'wb') as f:
            f.write(data.decode('base64'))

api.add_resource(Helloword, '/')
api.add_resource(Base64, '/base64')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6100, debug=True)