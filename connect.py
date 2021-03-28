import pandas as pd
import requests

api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/search/movie'
searched_query = 'The Matrix'
end_point = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searched_query}"
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
