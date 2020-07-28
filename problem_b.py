import json
from pprint import pprint


def movie_info(movie, genres):
    result = {}
    genre_name = []
 
    for i in range(0, len(movie['genre_ids'])):
        genre_name = genre_name + [movie['genre_ids'][i]]
 

    for i in range(0, len(genre_name)):
        for j in range(0, len(genres)):
            if genre_name[i] == genres[j]['id']:
                genre_name[i] = genres[j]['name']
  
     
    result['id'] = movie['id']
    result['title'] = movie['title']
    result['poster_path'] = movie['poster_path']
    result['vote_average'] = movie['vote_average']
    result['overview'] = movie['overview']
    result['genre_ids'] =  genre_name
    return result


    


if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))