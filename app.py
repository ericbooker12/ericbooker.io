from flask import Flask, render_template, Response, request, redirect, url_for
from episode_data import get_series_data, get_movie_data
import random


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
	return render_template("index.html")

@app.route("/episode-picker", methods=["GET", "POST"])
def episode_picker():
    return render_template("episode-picker.html")

@app.route("/episode-picker-deluxe", methods=["GET", "POST"])
def episode_picker_deluxe():

    return render_template("episode-picker-deluxe.html")


@app.route("/get-show-data", methods=["GET", "POST"])
def get_show_data():

    if request.method == 'POST':
        show = request.form['show']

        show_info = get_series_data(show)

        if show_info == "movie":

            movie_info = get_movie_data(show)

            print(movie_info)

            return render_template("movie-results.html", movie = movie_info) 
        
        else:

            print("*************************")
            print(show_info)
            print("*************************")
            
        
            num_of_seasons = len(show_info)
            
            rand_season = random.randint(1, num_of_seasons)

            season = show_info[rand_season - 1]
            year = season['year_released']
            number_of_episodes = season['number_of_episodes']
            show_title = season["title"]

            random_episode = random.randint(1, number_of_episodes)

            episode_list = season['episode_list']
            episode_to_watch = episode_list[random_episode - 1]
            
            return render_template(
                "episode-results.html", 
                show_title = show_title, 
                show_info = show_info, 
                year_released = year, 
                num_of_seasons = num_of_seasons,
                season_number = rand_season,
                episode_number = random_episode,
                episode_title = episode_to_watch,
            )

    else:
        return redirect(url_for('episode_picker_deluxe'))


if __name__ == '__main__':
	app.run(debug=True)