#!/usr/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response, url_for, redirect, abort

from werkzeug.utils import secure_filename

import config

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    if not username:
         resp = make_response(render_template('child.html', items=['Kobe', 'Wade'], msg=None))
         resp.set_cookie('username', 'server_set')
         return resp
    return render_template('child.html', items=['Kobe', 'Wade'], msg=username)

@app.route('/post/<post_id>')
@app.route('/post/<int:post_id>')
@app.route('/post/<float:post_id>')
@app.route('/post/<path:post_id>')
def path_post(post_id):
    return render_template('showpost.html', data=post_id)

@app.route('/userfor')
def usefor():
    return render_template('for.html', navigation=[
            {'href': 'https://www.youtube.com', 'name': 'youtube'},
            {'href': 'https://www.google.com', 'name': 'google'},
            {'name': 'google_nohref'}
        ])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '123':
            return render_template('login.html', msg='恭喜你登陆成功')
        return render_template('login.html', msg='Bad Sign In')
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    msg = None
    if request.method == 'POST':
        f = request.files['resource']
        f.save('uploads/' + secure_filename(f.filename))
        msg = 'Yes, we finished upload'
    return render_template('upload.html', msg = msg)

@app.route('/toredirect')
def toredirect():
    return redirect(url_for('notfound'))

@app.route('/notfound')
def notfound():
    abort(404)
    return render_template('not-found.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not-found.html', msg='render by errorhandler')

app.run(host='0.0.0.0', port=6100, debug=config.debug)