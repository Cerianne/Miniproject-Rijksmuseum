import json
listOfArt = []

# laad de json in een python-leesbaar object
with open('test.json') as f:
    data = json.load(f)

# Zet alle kunstvoorwerpen in een lijst
for kunst in data['artObjects']:
    listOfArt.append(kunst['title'])

print(listOfArt)

with open('KunstUitleen.txt', 'a') as f:
    f.writelines(listOfArt)

