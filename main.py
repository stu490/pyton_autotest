import requests

URL='https://api.pokemonbattle.ru/v2'
TOKEN='92ab1f19099a5c6a99b684767a3d1f58'
HEADER={'Content-Type':'application/json','trainer_token':TOKEN}
body={
    "name": "generate",
    "photo_id":-1
}
response= requests.post(url=f'{URL}/pokemons',headers=HEADER,json=body)
print(response.text) 

response= requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,
json=
  {"pokemon_id":"247085"}
)
print(response.text)


response= requests.put(url=f'{URL}/pokemons',headers=HEADER,
json= {
    "pokemon_id": "187773",
    "name": "New Name",
    "photo_id": 2
}
 )
print(response.text)

