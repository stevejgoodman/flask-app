# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:32:14 2016

@author: stevegoodman
"""

#Flask hello world
from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/hello")

def hello_world():
    return "hellow world"
if __name__ =="__main__":
    app.run()
