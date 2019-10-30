class Galerij(object):
    """description of class"""

    def __init__(self, gebruikersnaam, wachtwoord, email):
        self.gebruikersnaam = gebruikersnaam
        self.wachtwoord = wachtwoord
        self.email = email
        self.kunst = []

    def login(self,gebruikersnaam, wachtwoord):
        return True if self.gebruikersnaam == gebruikersnaam and self.wachtwoord == wachtwoord else False
        #return self.gebruikersnaam == gebruikersnaam and self.wachtwoord == wachtwoord

    def kunst_lenen(self, kunst):
        self.kunst.append(kunst)
        return "Gefeliciteerd! je hebt '" + kunst + "' geleend."

    def geleend(self):
        if len(self.kunst) > 0:
            return self.kunst
        else:
            return "Je hebt nog niets geleend!"

