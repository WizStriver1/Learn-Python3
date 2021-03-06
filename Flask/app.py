#!/usr/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response, url_for, redirect, abort, session, escape

from flask_sockets import Sockets

from werkzeug.utils import secure_filename
# import logging

import config

app = Flask(__name__)
# log = logging.getLogger('werkzeug')
# log.disabled = True

@app.route('/')
def index():
    username = request.cookies.get('username')
    if not username:
         resp = make_response(render_template('child.html', items=['Kobe', 'Wade'], msg=None))
         resp.set_cookie('username', 'server_set')
         return resp
    return render_template('child.html', items=['Kobe', 'Wade'], msg=username)

@app.route('/checksession')
def session_index():
    if 'username' in session:
        return render_template('session.html', msg='login with ' + escape(session['username']), login=True)
    return render_template('session.html', msg='you are not login', login=False)

@app.route('/sessionlogin', methods=['GET', 'POST'])
def session_login():
    if request.method == 'POST':
        session['username'] = request.form['username']

    return redirect(url_for('session_index'))

@app.route('/sessionlogout')
def session_logout():
    session.pop('username', None)
    return redirect(url_for('session_index'))

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

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('not-found.html', msg='render by errorhandler')

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('not-found.html', msg='render by errorhandler'), 404

@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('not-found.html', msg='render by errorhandler'), 404)
    resp.headers['X-Something'] = 'value'
    return resp

sockets = Sockets(app)

@sockets.route('/')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send(message)

app.secret_key = '\x19\xedy<Y\x88\xa1#\xaaB:\xff>\xe5\xec\x16\x80\xaf\xec\xdb\t\xad\xa8A'

if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    # app.run(host='0.0.0.0', port=6100, debug=config.debug)
    server = pywsgi.WSGIServer(('', 6100), app, handler_class=WebSocketHandler)
    server.serve_forever()