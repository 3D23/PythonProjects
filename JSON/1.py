import json

with open("character.json", "r") as f:
    character = json.load(f)

print(character['name'])
print(character['origin']['name'])
print(character['episode'])