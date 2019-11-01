import json
from Galerij import Galerij 
from Person import Person
import Jsonfiles

#kunstdata = Jsonfiles.get_alle_kunstdata()
#dict_of_art = []

# Zet alle kunstvoorwerpen in een json
#for kunst in Jsonfiles.get_alle_kunstdata():
    #dict_of_art.append( {"Naam": kunst['title'],'ObjectNumber': kunst['objectNumber'], 'Available': True })

#for kunstwerk in Jsonfiles.get_kunstdata()['Kunststukken']:
    #for item in kunstwerk[':
        #print(item)

#dict_of_art = Jsonfiles.get_alle_kunstdata()
#for kunst in dict_of_art:
    #dict_of_art['Kunststukken'] = {'Naam' : kunst['title'], 'ObjectNumber': kunst['objectNumber'], 'Available': True }

#dict_of_art = json.dumps(dict_of_art,indent=2)

#with open ('KunstUitleen.json','w') as f:
    #for item in dict_of_art:
        #f.writelines(item)

for kunstwerk in Jsonfiles.get_kunstdata():
    if kunstwerk['Available'] == True:
        print(kunstwerk['Available'])