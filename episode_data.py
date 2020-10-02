from imdb import IMDb

def get_series_data(show):
  ia =IMDb()
  series = ia.search_movie(show)[0]
  ia.update(series, 'episodes')

  episode_data = series.data['episodes']
  num_of_seasons = len(episode_data)
  series_data = []
  seasons = {}

  for season_number in episode_data:
    episode_list = []

    season = episode_data[season_number]
    season_number = season_number
    num_of_episodes = len(season)

    for episode in season:
      season_data = {}
      episode_list.append(str(season[episode]))

    season_data['season_number'] =  season_number
    season_data['number_of_episodes'] =  num_of_episodes
    season_data['episode_list'] =  episode_list

    series_data.append(season_data)

	# series_data will be return value
  return series_data
