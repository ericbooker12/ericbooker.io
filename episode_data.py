from imdb import IMDb

def get_series_data_random(show):
  ia =IMDb()
  series = ia.search_movie(show)[0]
  movie_id = series.movieID
  # print(movie_id)
  series_data = ia.get_movie(movie_id)

  # outline = series_data.data['plot outline'] 
  plot = series_data.data['plot']

  if series['kind'] == 'tv series':

    ia.update(series, 'episodes')

    year = series['year']

    episode_data = series.data['episodes']
    # plot = series.data['plot outline'] 2

    # print(series)
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
      season_data['plot'] =  plot
  

      series_data.append(season_data)

    # series_data will be return value
    return series_data
  
  elif series['kind'] == 'movie':
    return "movie"

def get_series_data(show):
  ia =IMDb()
  series = ia.search_movie(show)[0]
  movie_id = series.movieID
  series_data = ia.get_movie(movie_id)
  cast = []
  show_data = {}

  if series['kind'] == 'tv series':

    ia.update(series, 'episodes')

    for cast_member in series_data['cast']:
      cast.append(cast_member['name'])

    show_data['title'] = str(series_data)
    show_data['plot'] = series_data.data['plot'][0].split("::")[0]
    show_data['rating'] = series_data.data['rating']
    show_data['year'] = series_data.data['year']
    show_data['genre'] = series_data.data['genres'][0]
    show_data['years_active'] = series_data.data['series years']
    show_data['cast'] = cast

    episode_data = series.data['episodes']

    num_of_seasons = len(episode_data)
    series_data = []
    seasons = {}

    for season_number in episode_data:
      episode_list = []

      season_name = 'season ' + str(season_number)

      # print(season_name)

      season = episode_data[season_number]
      season_number = season_number
      num_of_episodes = len(season)

      for episode in season:  
        season_data = {}
        episode_list.append(str(season[episode]))

      seasons[season_name] = episode_list
      
      series_data.append(season_data)

    show_data['episodes'] = seasons

    return show_data
  
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

#__________________________________________________________

# {'original title': 'Woke (2020- )', 
# 'cast': [<Person id:2031358[http] name:_Lamorne Morris_>, 
# <Person id:2981935[http] name:_Blake Anderson_>, 
# <Person id:5968385[http] name:_T. Murph_>, 
# <Person id:1356578[http] name:_J.B. Smoove_>, 
# <Person id:3550886[http] name:_Sasheer Zamata_>, 
# <Person id:0570860[http] name:_Rose McIver_>, 
# <Person id:7596733[http] name:_Alvina August_>, 
# <Person id:3931538[http] name:_Sam Richardson_>, 
# <Person id:0355024[http] name:_Tony Hale_>, 
# <Person id:3355329[http] name:_Nicole Byer_>, 
# <Person id:0147825[http] name:_Cedric the Entertainer_>, 
# <Person id:6297445[http] name:_Donna Benedicto_>, 
# <Person id:1275101[http] name:_Shannon Chan-Kent_>, 
# <Person id:1273767[http] name:_Kurt Long_>, 
# <Person id:3651929[http] name:_Shannon Kook_>, 
# <Person id:0838588[http] name:_Cree Summer_>, 
# <Person id:1034338[http] name:_Elizabeth Bowen_>, 
# <Person id:0341176[http] name:_Eddie Griffin_>, 
# <Person id:1442113[http] name:_Jack McBrayer_>, 
# <Person id:8409919[http] name:_Adam Kirschner_>, 
# <Person id:1352845[http] name:_David Ury_>, 
# <Person id:0202966[http] name:_Keith David_>, 
# <Person id:5088392[http] name:_Justyna Bania_>, 
# <Person id:1052534[http] name:_Nathan Lee Graham_>, 
# <Person id:2577076[http] name:_Lil Rel Howery_>, 
# <Person id:1022732[http] name:_Link Baker_>, 
# <Person id:9112433[http] name:_Jarrett Carlington_>, 
# <Person id:0150376[http] name:_Lossen Chambers_>, 
# <Person id:0445389[http] name:_Peter Kelamis_>, 
# <Person id:1284045[http] name:_Diana Pavlovská_>, 
# <Person id:7856682[http] name:_Leanne Allen_>, 
# <Person id:2390004[http] name:_Bryan Demore_>, 
# <Person id:11885145[http] name:_Cassandra Bolinski_>, 
# <Person id:0237943[http] name:_Jasmin Dring_>, 
# <Person id:11401307[http] name:_Sarah Rodgers_>, 
# <Person id:6801314[http] name:_Clare Filipow_>, 
# <Person id:10479344[http] name:_Sam Rahmani_>, 
# <Person id:5820794[http] name:_Lyle Reginald_>, 
# <Person id:2686167[http] name:_Krista Magnusson_>, 
# <Person id:4316154[http] name:_Vanessa Richards_>, 
# <Person id:1995155[http] name:_Janet Glassford_>, 
# <Person id:7221026[http] name:_Jacki Gunn_>, 
# <Person id:0836071[http] name:_Wes Studi_>, 
# <Person id:0871141[http] name:_Phil Trasolini_>, 
# <Person id:0183576[http] name:_Chris Cound_>, 
# <Person id:4269856[http] name:_Susan Hanson_>, 
# <Person id:2788169[http] name:_Casey Manderson_>, 
# <Person id:1417897[http] name:_Brandi Alexander_>, 
# <Person id:0242151[http] name:_Herbert Duncanson_>, 
# <Person id:11885132[http] name:_Ute Rée_>], 
# 'genres': ['Comedy'], 
# 'countries': ['United States'], 
# 'country codes': ['us'], 
# 'language codes': ['en'], 
# 'color info': ['Color'], 
# 'certificates': ['Canada:TV-MA::(self-applied)', 
# 'United States:TV-MA::(self-applied)'], 
# 'creator': [<Person id:10056664[http] name:_Keith Knight_>, 
# <Person id:1187871[http] name:_Marshall Todd_>], 
# 'number of seasons': 1, 
# 'rating': 6.2, 
# 'votes': 1642, 
# 'cover url': 'https://m.media-amazon.com/images/M/MV5BNDIzOTJjM2QtNjkwNS00NGFhLWJhYjgtZjAxZGZmYjFlZTg4XkEyXkFqcGdeQXVyNjEwNTM2Mzc@._V1_SY150_CR3,0,101,150_.jpg', 
# 'imdbID': '9223870', 
# 'languages': ['English'], 
# 'title': 'Woke', 
# 'year': 2020, 
# 'kind': 'tv series', 
# 'series years': '2020-', 
# 'akas': ['Прозревший (Russia)'], 
# 'seasons': ['1'], 
# 'writer': [<Person id:10056664[http] name:_Keith Knight_>, 
# <Person id:1187871[http] name:_Marshall Todd_>, 
# <Person id:2953647[http] name:_Conor Galvin_>], 
# 'production companies': [<Company id:0294149[http] name:_Cloud Nine Productions_>, 
# <Company id:0219609[http] name:_Olive Bridge Entertainment_>, 
# <Company id:0086397[http] name:_Sony Pictures Television_>], 
# 'distributors': [<Company id:0218858[http] name:_Hulu_>], 
# 'special effects': [<Company id:0197392[http] name:_Ingenuity Studios_>], 
# 'other companies': [<Company id:0632193[http] name:_Bespoke Post_>, 
# <Company id:0028470[http] name:_Company 3_>], 
# 'plot': ['Keef is an African-American cartoonist on the verge of mainstream success when an unexpected incident changes his life.::Anonymous']}
