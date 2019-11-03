def email(naamtk):
       persoonsdata = Jsonfiles.get_persoonsdata
       for person in persoonsdata['Persoonsgegevens']:
              if person['Naam'] == naamtk:
                     return codetk

def code(codetk):
       persoonsdata = Jsonfiles.get_persoonsdata
       for person in persoonsdata['Persoonsgegevens']:
              if person['Ticketnummer'] == codetk:
                     return codetk

def kunststuk(kunststuktk):
       persoonsdata = Jsonfiles.get_persoonsdata
       for person in persoonsdata['Persoonsgegevens']:
              if person['Kunststukken'] == kunststuktk:
                     return kunststuktk
