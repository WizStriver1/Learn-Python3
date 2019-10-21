# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect
from flask_restful import Resource, Api
import os
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, IMAGES, config_for_set, configure_uploads

import time

app = Flask(__name__)
api = Api(app)

UPLOAD_FOLDER = os.path.split(__file__)[0]

photos = UploadSet('IMAGES', IMAGES)

app.config['UPLOADED_IMAGES_URL'] = UPLOAD_FOLDER
app.config['UPLOADED_IMAGES_DEST'] = 'uploads'

configure_uploads(app, (photos, ))

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def strfstamp(stamp=time.time(), format_str='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format_str, time.localtime(stamp))

def get_print_time():
    return '[ %s ]' % strfstamp()

@app.route('/toupload', methods=['get'])
def toupload():

    return render_template('upload.html')

class Upload(Resource):

    def __init__(self):
        pass

    def post(self):
        # check if the post request has the file part
        r = request
        print(get_print_time() + ' ' + r.remote_addr + ' tried to post')
        if 'file' not in request.files:
            print('No file part')
            return redirect('/toupload')
        filename = photos.save(request.files['file'])
        print(filename)
        # return redirect('/toupload')
        return filename

api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6010, debug=True)