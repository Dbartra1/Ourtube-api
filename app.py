from flask import Flask, request, jsonify, redirect, url_for, render_template
from pytube import YouTube, Search, Stream
import urllib.request
from PIL import Image
from pathlib import Path


app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        form_data = request.form.get("rsearch")
        yt_id = Youtube.from_id(s)
        return "The video ID is:" + str ()
        

if __name__ == '__main__': 
    app.run(host = 'localhost', debug=True, port=9090)
