import json


def max_revenue(movies):
    movies_ids = []
    for movie in movies:
        movies_ids = movies_ids + [movie['id']]

    movies_budgets = []    
    for i in movies_ids:
        movie_json = open(f'data/movies/{i}.json', encoding='UTF8')
        movie_json_load = json.load(movie_json)    
        movies_budgets = movies_budgets + [movie_json_load['budget']]
    
    maxmax = 0
    for budget in movies_budgets:
        if budget > maxmax:
            maxmax = budget

    cnt = 0
    for budget in movies_budgets:
        
        if maxmax ==  budget:
            break
        cnt += 1
    
    #movies_ids[cnt]에 수익 제일 높은 아이디 있음.
    for i in range(0, len(movies)):
        if movies_ids[cnt] == movies[i]['id']:
            budget_name = movies[i]['title']
    return budget_name
        
    
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    print(max_revenue(movies_list))