import requests

"""https://api.themoviedb.org/3/movie/550?api_key=eb3a7d37cbc42bb0f1598c41b1384cc7"""

person_id = 5
base_url = "https://api.themoviedb.org/3"
end_path = f'/person/{person_id}/tv_credits'
end_point = f'{base_url}{end_path}?api_key={api_key}'

r = requests.get(end_point)
data = r.json()
# print(data.keys())
# print(data['id'])
cast_data = data['cast']
for cast in cast_data:
    print(cast.keys())
    print()
