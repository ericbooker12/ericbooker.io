from imdb import IMDb

def get_series_data(show):
  ia =IMDb()
  series = ia.search_movie(show)[0]

  if series['kind'] == 'tv series':

    ia.update(series, 'episodes')

    year = series['year']

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

      season_data['title'] = series
      season_data['year_released'] = year
      season_data['season_number'] =  season_number
      season_data['number_of_episodes'] =  num_of_episodes
      season_data['episode_list'] =  episode_list

      series_data.append(season_data)

    # series_data will be return value
    return series_data
  
  elif series['kind'] == 'movie':
    return "movie"



def get_movie_data(movie):
  ia =IMDb()
  movie_data = ia.search_movie(movie)

  title = str(movie_data[0])

  m = movie_data[0]

  movie = ia.get_movie(m.movieID)
  plot = movie['plot'][1]
  release_date = str(movie['original air date'])
  print(release_date)
  year = movie['year']
  url = movie['cover url']
  directors = []
  cast = []
  writers = []

  movie_data = {}

  i = 0
  for actor in movie['cast']:
    cast.append(str(actor))
  
  for i in movie['directors']:
    directors.append(str(i))
  
  for i in movie['writers']:
    writers.append(str(i))
    
  movie_data["title"] = title
  movie_data["year"] = year
  movie_data["release_date"] = release_date
  movie_data["plot"] = plot
  movie_data["year"] = year
  movie_data["url"] = url
  movie_data["director"] = directors
  movie_data["writer"] = writers
  movie_data["cast"] = cast

  return movie_data

# def comma_builder(lst):
#   str = ''
#   count = lent(lst)
#   for i in range(0, count) list:
#     str += i
#     if i < count


  # movie_data:  {
  #   'plot': 'Josh Baskin would do anything to be big to hang out with his crush at the carnival. He finds a Zoltar machine, and he wishes to be big. After Zoltar tells him, "his wish is granted", Josh notices the machine is unplugged. He wakes up the next morning in an adult\'s body but he still has the same personality. With the help of his best friend, Billy, Josh learns how to act like a grown up. But as he gets a girlfriend and a fun job, he doesn\'t want to be a kid again. Will Josh stay big or become a 13 year old boy again?', 'year': 
  #   '03 Jun 1988 (USA)', 
  #   'url': 'https://m.media-amazon.com/images/M/MV5BMDQ1ODM5MTMtMjAwYi00ZGUxLTliNTMtN2ZhODAwMjVhMTRlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY150_CR0,0,101,150_.jpg'}

# {'main': 
#   ['original title', 
#   'cast', 
#   'genres', 
#   'runtimes', 
#   'countries', 
#   'country codes', 
#   'language codes', 
#   'color info', 
#   'aspect ratio', 
#   'sound mix', 
#   'box office', 
#   'certificates', 
#   'original air date', 
#   'rating', 
#   'votes', 
#   'cover url', 
#   'imdbID', 
#   'plot outline', 
#   'languages', 
#   'title', 
#   'year', 
#   'kind', 
#   'directors', 
#   'writers', 
#   'producers', 
#   'composers', 
#   'cinematographers', 
#   'editors', 
#   'editorial department', 
#   'casting directors', 
#   'production designers', 
#   'art directors', 
#   'set decorators', 
#   'costume designers', 
#   'make up department', 
#   'production managers', 
#   'assistant directors', 
#   'art department', 
#   'sound department', 
#   'camera department', 
#   'casting department', 
#   'costume departmen', 
#   'location management', 
#   'music department', 
#   'script department', 
#   'transportation department', 
#   'miscellaneous', 
#   'thanks', 
#   'akas', 
#   'writer', 
#   'director', 
#   'production companies', 
#   'distributors', 
#   'other companies'], 
#   'plot': ['plot', 'synopsis']}

# [<Movie id:0094737[http] title:_Big (1988)_>, 
# <Movie id:1000777[http] title:_Uncharted: Drake's Fortune (2007) (VG)_>, 
# <Movie id:2441802[http] title:_Big (2012)_>, 
# <Movie id:9140560[http] title:_WandaVision (2020)_>, 
# <Movie id:0898266[http] title:_"The Big Bang Theory" (2007)_>, 
# <Movie id:3920596[http] title:_"Big Little Lies" (2017)_>, 
# <Movie id:0118715[http] title:_The Big Lebowski (1998)_>, 
# <Movie id:0078748[http] title:_Alien (1979)_>, 
# <Movie id:11794642[http] title:_"Big Sky" (2020)_>, 
# <Movie id:1596363[http] title:_The Big Short (2015)_>, 
# <Movie id:6524350[http] title:_"Big Mouth" (2017)_>, 
# <Movie id:0319061[http] title:_Big Fish (2003)_>, 
# <Movie id:2245084[http] title:_Big Hero 6 (2014)_>, 
# <Movie id:0142342[http] title:_Big Daddy (1999)_>, 
# <Movie id:0251497[http] title:_"Big Brother" (II) (2000)_>, 
# <Movie id:0058791[http] title:_"The Big Valley" (1965)_>, 
# <Movie id:5462602[http] title:_The Big Sick (2017)_>, 
# <Movie id:1931435[http] title:_The Big Wedding (2013)_>, 
# <Movie id:0421030[http] title:_"Big Love" (2006)_>, 
# <Movie id:9441638[http] title:_The Big Ugly (2020)_>]

