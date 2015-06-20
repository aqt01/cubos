from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask import request
from util import processor
import requests
import json

app = Flask(__name__)
"""
app.config['SECRET_KEY'] = 'F34TF$($e34D';
"""

@app.route('/')
def home(name=None):
    return render_template('index.html',name=name)

@app.route('/api/receive_colors', methods=['GET','POST'])
def receive_colors():
    import ipdb
    ipdb.set_trace()
    print request._data
    data= request.data
    processor.color_processor(data)            
    return data

# A Naive approach
"""
@app.route('/send_color_red')
def send_red():
    url= 'http://127.0.0.1:5000/api/receive_colors'
    data = {'color':'RED'}
    r = requests.post(url,data=json.dumps(data))
    return redirect(url_for('home'))


@app.route('/send_color_blue')
def send_blue():
    url= 'http://127.0.0.1:5000/api/receive_colors'
    data = {'color':'BLUE'}
    r = requests.post(url,data=json.dumps(data))
    return redirect(url_for('home'))




@app.route('/send_color_green')
def send_green():
    url= 'http://127.0.0.1:5000/api/receive_colors'
    data = {'color':'GREEN'}
    r = requests.post(url,data=json.dumps(data))
    return redirect(url_for('home'))

@app.route('/send_color_white')
def send_whie():
    url= 'http://127.0.0.1:5000/api/receive_colors'
    data = {'color':'WHITE'}
    r = requests.post(url,data=json.dumps(data))
    return redirect(url_for('home'))
"""

if __name__ == '__main__':
    app.run()
