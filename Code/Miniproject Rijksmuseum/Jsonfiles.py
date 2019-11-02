import json

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