import json

# Alle get() functies van de verschillende Jsonfiles.
def get_alle_kunstdata():
    with open('alle_kunststuken.json') as f:
        kunstdata = json.load(f)
        return kunstdata

def get_galerijdata():
    with open('galleries.json') as f:
        galleriedata = json.load(f)
        return galleriedata

def get_persoondata():
    with open('persoonsgegevens.json') as f:
        persoondata = json.load(f)
        return persoondata

def get_kunstdata():
    with open('KunstUitleen.json') as f:
        data = json.load(f)
        return data
    
# Alle set() functies van de verschillende Jsonfiles.
def set_alle_kunstdata(kunstdata):
    with open('alle_kunststuken.json','w') as f:
        kunstdata = json.dumps(kunstdata,indent=2)
        f.writelines(kunstdata)

def set_galerijdata(galerijdata):
    with open('galleries.json', 'w') as f:
        galerijdata = json.dumps(galerijdata,indent=2)
        f.writelines(galerijdata)

def set_persoondata(persoonsdata):
    with open('persoonsgegevens.json', 'w') as f:
        persoonsdata = json.dumps(persoonsdata,indent=2)
        f.writelines(persoonsdata)

def set_kunstdata(kunstdata):
    with open('KunstUitleen.json', 'w') as f:
        kunstdata = json.dumps(kunstdata,indent=2)
        f.writelines(kunstdata)
