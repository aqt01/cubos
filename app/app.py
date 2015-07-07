from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask import request
from util import processor
import json

app = Flask(__name__)
"""
app.config['SECRET_KEY'] = 'F34TF$($e34D';
"""

color_mixer = processor.Color_Mixer()
@app.route('/')
def home(name=None):
    return render_template('index.html',name=name)

@app.route('/api/receive_colors', methods=['GET','POST'])
def receive_colors():
    color = request.get_data()    
    color_mixer.color_processor( color.split("=")[1] )

if __name__ == "__main__":
    app.run()
