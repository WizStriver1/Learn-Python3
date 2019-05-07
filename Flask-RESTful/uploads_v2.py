#!/usr/env python3
# -*- coding: utf-8 -*-
# python v2.7.14

from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_uploads import IMAGES, UploadSet, configure_uploads
from werkzeug import secure_filename, FileStorage

import webbrowser

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, (photos, ))

class UploadsRESTful(Resource):

    def get(self):
        req = request
        return {'Hello': 'get'}

    def post(self):
        request_files = request.files
        req = request
        all_files = request.files.iteritems(multi=True)
        file_list = request.files.getlist('photo')
        filenames = []
        for filename, file in all_files:
            file_name = file.filename
            filenames.append(photos.save(file))

        return {'Hello': 'World', 'filename': filenames}

@app.route('/upload')
def upload():
    return render_template('uploads.html')

# media = UploadSet('media', default_dest=lambda app: app.instance_path)
api.add_resource(UploadsRESTful, '/')

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 6100
    webbrowser.open('http://%s:%d/upload' % (host, port))
    app.run(host=host, port=port, debug=True)