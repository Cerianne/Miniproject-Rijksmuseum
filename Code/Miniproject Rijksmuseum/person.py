class Person(object):
    """description of class"""
    def __init__(self, gebruikersnaam, email):
        self.gebruikersnaam = gebruikersnaam
        self.email = email

    def login(self,gebruikersnaam, email):
        return True if self.gebruikersnaam == gebruikersnaam and self.email == email else False
        #return self.gebruikersnaam == gebruikersnaam and self.wachtwoord == wachtwoord

klaas = Person('Klaas','klaas@testen.com')
print(klaas.login('Klaas','kareltje@banaan.com'))


