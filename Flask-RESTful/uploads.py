#!/usr/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api

from flask_uploads import IMAGES, UploadSet, configure_uploads
from werkzeug import secure_filename, FileStorage

app = Flask(__name__)
api = Api(app)

app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, (photos, ))

class UploadsRESTful(Resource):
    
    def post(self):
        all_files = request.files.iteritems(multi=True)
        test_photos = photos
        filename = photos.save(request.files['photo'])

        return {'Hello': 'World', 'filename': filename}

media = UploadSet('media', default_dest=lambda app: app.instance_path)
api.add_resource(UploadsRESTful, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6100, debug=True)