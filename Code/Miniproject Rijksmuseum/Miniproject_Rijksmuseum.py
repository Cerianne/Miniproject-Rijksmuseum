import json
from Galerij import Galerij 
from Person import Person

listOfArt = []

# laad de json in een python-leesbaar object
with open('test.json') as f:
    data = json.load(f)

# Zet alle kunstvoorwerpen in een lijst
for kunst in data['artObjects']:
    listOfArt.append(kunst['title'])

print(listOfArt)

buitenkunst = Galerij('Buitenkunst','Zwolle', 'buitenkunst@buitenkunst.nl')
print(buitenkunst.login('Buitenkunst','Zwolle'))
print(buitenkunst.kunst_lenen('Karel Appel'))

klaas = Person('Klaas','klaas@testen.com')
print(klaas.login('Klaas','banaan'))

with open('KunstUitleen.txt', 'a') as f:
    f.writelines(listOfArt)

def is_uitgeleend(naam_kunstwerk):
    with open('KunstUitleen.txt', 'r') as f:
        uitgeleend = f.readlines()
        if naam_kunstwerk in uitgeleend:
            return("Sorry, dit kunstwerk is al uitgeleend.")