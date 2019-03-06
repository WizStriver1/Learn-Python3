#!/usr/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

from werkzeug.utils import secure_filename

import config

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
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

app.run(host='0.0.0.0', port=6100, debug=config.debug)