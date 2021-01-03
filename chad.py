"""# Italy Challenge for MUCH
# Author: Yuval Meshorer


# Web server setup
from flask import Flask, Response, request, render_template_string, render_template
app = Flask("Peppa Pig fan page",
            template_folder='/app/templates',
            static_folder='/app/templates'
)

# To not spam the poor server
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Database
#import pymongo_wrapper

# Challenge setup
import secret

# This will only help true Peppa fans!
app.jinja_env.globals['fanpage'] = secret.page
app.jinja_env.globals['flag'] = secret.flag

# Used to "cache" the files to make the server a little faster.
with open('/app/app.py') as source_file:
    app_response = Response(source_file.read(), mimetype='text/plain')

with open('/app/logs.pig') as logs_file:
    logs_response = Response(logs_file.read(), mimetype='text/plain')


# Force web page cache to be disabled.
@app.after_request
def add_header(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


# Main page
@app.route('/')
@app.route('/it/')
def index():
    return render_template('index.html')


# Get this file
@app.route('/app.py')
@app.route('/it/app.py')
def get_source():
    return app_response


# Get the database logs
@app.route('/logs.pig')
@app.route('/it/logs.pig')
def get_logs():
    return logs_response


# Blessing generator
@app.route('/bless')
@app.route('/it/bless')
def bless_peppa():
    template = request.args.get('blessing') or '...'
    template = template.replace('_', '')

    return render_template_string(template)


# Secret page for #1 fans :)
@app.route(secret.page)
@app.route('/it' + secret.page)
def secret_page():
    argument = request.args.get(secret.parameter)
    if argument is None:
        return render_template(secret.page[1:] + '.html')
    
    #return pymongo_wrapper.find_one(argument) or '{}'


# Load the stupid thing
app.run(host='0.0.0.0', port=9230)"""
import requests

proxies = {
 "http": "http://10.10.10.10:8000",
 "https": "http://10.10.10.10:8000",
}
r = requests.get("http://much-challenges.cyber.org.il/ci/")
print(r.content)