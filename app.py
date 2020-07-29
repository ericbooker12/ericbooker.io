from flask import Flask, render_template, Response, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
	return "<H1>Eric Booker</H1>"

@app.route("/episode-picker", methods=["GET", "POST"])
def episode_picker():
    return render_template("episode-picker.html")


if __name__ == '__main__':
	app.run(debug=True)