import json
from Galerij import Galerij 
from Person import Person

listOfArt = []

# laad de jsons in een python-leesbaar object
with open('alle_kunststuken.json') as f:
    kunstdata = json.load(f)
with open('galleries.json') as f:
    galleriedata = json.load(f)
with open('persoonsgegevens.json') as f:
    persoondata = json.load(f)

# Zet alle kunstvoorwerpen in een lijst
for kunst in kunstdata:
    listOfArt.append(kunst['title'])

print(listOfArt)

#Maak wat testclasses aan
buitenkunst = Galerij('Buitenkunst','Bu1tenKunst!', 'Assensestraat', '13', 'Zwolle')
print(buitenkunst.kunst_lenen('Karel Appel'))

#sla de galerie op in een .json
with open ('galleries.json', 'a' ) as f:
    f.writelines = buitenkunst.sla_op()

klaas = Person('Klaas','klaas@testen.com')
print(klaas.login('Klaas','banaan'))

with open('KunstUitleen.txt', 'a') as f:
    f.writelines(listOfArt)

def is_uitgeleend(naam_kunstwerk):
    with open('KunstUitleen.txt', 'r') as f:
        uitgeleend = f.readlines()
        if naam_kunstwerk in uitgeleend:
            return("Sorry, dit kunstwerk is al uitgeleend.")