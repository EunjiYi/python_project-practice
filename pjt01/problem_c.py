import json
from pprint import pprint


def movie_info(movies, genres):
    result = []
    for movie in movies:
    
        genre_name = []
    
        for i in range(0, len(movie['genre_ids'])):
            genre_name = genre_name + [movie['genre_ids'][i]]
    

        for i in range(0, len(genre_name)):
            for j in range(0, len(genres)):
                if genre_name[i] == genres[j]['id']:
                    genre_name[i] = genres[j]['name']
        
        movie_detail = {}
        movie_detail['id'] = movie['id']
        movie_detail['title'] = movie['title']
        movie_detail['poster_path'] = movie['poster_path']
        movie_detail['vote_average'] = movie['vote_average']
        movie_detail['overview'] = movie['overview']
        movie_detail['genre_ids'] = genre_name
        result = result + [movie_detail]
    return result



if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))