from flask import Flask, render_template, request, redirect, url_for, jsonify
import io
import random
from flask import Flask, Response, request
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():


	return "<H1>Eric Booker</H1>"


if __name__ == '__main__':
	app.run(debug=True)