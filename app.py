from flask import Flask, render_template, Response, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():


	return "<H1>Eric Booker</H1>"


if __name__ == '__main__':
	app.run(debug=True)