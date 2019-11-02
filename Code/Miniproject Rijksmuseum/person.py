import random
import json

class Person(object):
    """description of class"""
    def __init__(self, gebruikersnaam, email):
        self.gebruikersnaam = gebruikersnaam
        self.email = email
        self.ticketnr = []

    def login(self,gebruikersnaam, email):
        if '@' in email and ('.com' or '.nl' in email):
            return True 
        else:
            return "Dit is geen geldig mailadres. Probeer het nog eens."

    def getCode(self, kunst):
        # Todo: Zoek het kunststuk op. Check of het uitgeleend is. Zo ja, genereer een code voor de bezoeker.
        # De code word random gegenereerd met de unieke code vna het kunstwerk + : + een randint, maar mag niet al bestaan! 
        # Zoek dit op in een .json? / .txt ? 
        # Zo nee, meld dat dit kunststuk gewoon te zien is in het Rijksmuseum.
        return "Dit kunststuk is gewoon te zien in het rijksmuseum!"

    def sla_op(self):
        return json.dumps(self.__dict__, indent=2)


