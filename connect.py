import pandas as pd
import requests


api_key = 'eb3a7d37cbc42bb0f1598c41b1384cc7'
api_token_v4 = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYjNhN2QzN2NiYzQyYmIwZjE1OThjNDFiMTM4NGNjNyIsInN1YiI6IjYwMzBiNmVjYjRhNTQzMDA0MTExYWY3NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fD6CPamtozVgYwbwiX_ua2j3riyeVGGbbjlJzelzbSI'

"""
https://api.themoviedb.org/3/movie/550?api_key=eb3a7d37cbc42bb0f1598c41b1384cc7
"""
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
# endpoint_path = f'/movie/{movie_id}'
endpoint_path = f'/search/movie'
searched_query = 'The Matrix'
end_point = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searched_query}"
# headers={
#     'Authorization': f'Bearer {api_token_v4}',
#     'Content-Type': 'application/json;charset=utf-8'
# }
r = requests.get(end_point)
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results)>0:
        movie_ids = set()
        for result in results:
            _id = result['id']
            movie_ids.add(_id)

output = 'movies.scv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f'https://api.themoviedb.org/{api_version}'
    endpoint_path = f'/movie/{movie_id}'
    end_point = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(end_point)
    if r.status_code in range (200, 299):
        data = r.json()
        movie_data.append(data)
df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index = False)