import flask
from flask import Flask, render_template, redirect, Blueprint, url_for, request
import numpy as np
import pandas as pd
import pickle
from io import StringIO
import json as JSON
import folium

app = flask.Flask(__name__)



# Load homepage when root of url is loaded
@app.route("/")
def viz_page():
    return render_template('page.html')

#Function to run when /calculate is called. Function takes data from site, processes it, and returns new data to display
@app.route("/calculate", methods=["POST"])
def calculate():
	data_from_site = flask.request.json

	def process_keyword(keyword):
		
		with open('all_words_for_location.json') as json_file:  
			data_dict = JSON.load(json_file)
		
		matches = []
		
		for key, values in data_dict.items():
			if keyword.lower() in values:
				matches.append(key)
			elif keyword.lower() not in values: 
				pass
		
		return (matches)      

	result = process_keyword(data_from_site[0])

	results = {'result':result}

	return flask.jsonify(results)

@app.route("/getmap")    

def index():
	start_coords = (40.7128, -74.0060)
	folium_map = folium.Map(location=start_coords, zoom_start=10,  tiles="cartodbpositron")
	return folium_map._repr_html_()  


#Run the flask app
if __name__ == '__main__':
    #app.run()
    app.run(debug=True)