from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask import request
from util import processor
import json

# Timer for total calc
import time
from threading import Timer



app = Flask(__name__)
"""
app.config['SECRET_KEY'] = 'F34TF$($e34D';
"""

color_mixer = processor.Color_Proc()

@app.route('/')
def home(name=None):
    return render_template('index.html',name=name)

@app.route('/api/receive_colors', methods=['GET','POST'])
def receive_colors():
    color = request.get_data()    
    color_mixer.color_processor( color.split("=")[1] )

if __name__ == "__main__":
    # Timer for checking total every time
    timer = processor.RepeatedTimer(5,color_mixer.total_cal)
    app.run()

