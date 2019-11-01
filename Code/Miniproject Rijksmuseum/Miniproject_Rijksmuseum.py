import json
from Galerij import Galerij 
from Person import Person
import Jsonfiles

galerijdata = Jsonfiles.get_galerijdata()


# Zet alle kunstvoorwerpen in een json
#for kunst in Jsonfiles.get_kunstdata():
    #dict_of_art[kunst['title']] = {'ObjectNumber': kunst['objectNumber'], 'Available': True }

for galerij in galerijdata['Gallerijhouders']:
    print(galerij['Gebruikersnaam'])
    print(galerij['Wachtwoord'])
