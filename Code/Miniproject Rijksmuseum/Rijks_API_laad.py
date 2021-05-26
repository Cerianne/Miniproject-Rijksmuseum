import http.client, urllib.parse, json


# opvragen

def opvragenKunststuk(invoer):
    """ voor het zoeken op naam van het kunstwerk, geeft tuple met info terug voor verdere verwerking"""
    params = urllib.parse.urlencode({
        'p': '0',
        'ps': '1',
        'q': str(invoer)
    })

    conn = http.client.HTTPSConnection('www.rijksmuseum.nl')
    #TODO Add your key here below!
    conn.request("GET", "/api/nl/collection?key= <INPUT KEY HERE> &format=json&" + params)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)
    schilderij = data["artObjects"]

    with open("search_result.json", "w") as json_file:
        json.dump(schilderij, json_file, indent=4)

    for data in schilderij:
        # return data["objectNumber"]
        return data["principalOrFirstMaker"], data["title"], data["objectNumber"]


def imgKunstwerk(invoer):
    """" geeft de hyperlink naar de gezochte afbeeling terug
    (heeft opvragenKunststuk nodig voor het maken van het zoek bestand)"""
    params = urllib.parse.urlencode({
        'p': '0',
        'ps': '1',
        'q': str(invoer)
    })

    conn = http.client.HTTPSConnection('www.rijksmuseum.nl')
    # TODO Add your key here below!
    conn.request("GET", "/api/nl/collection?key= <INPUT KEY HERE> &format=json&" + params)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)
    schilderij = data["artObjects"]
    for data in schilderij:
        return data["webImage"]["url"]


# invoer

# text = input("titel van het kunstwerk: ")
# #
# # print(opvragenKunststuk(text))
# # print(imgKunstwerk(text))

def kunstSlurp():
    params = urllib.parse.urlencode({
        'p': '0',
        'ps': '100',
        'toppieces': 'True',

    })

    conn = http.client.HTTPSConnection('www.rijksmuseum.nl')
    # TODO Add your key here below!
    conn.request("GET", "/api/nl/collection?key= <INPUT KEY HERE> &format=json&" + params)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)
    schilderij = data["artObjects"]

    with open("alle_kunststuken.json", "w") as json_file:
        json.dump(schilderij, json_file, indent=4)

#kunstSlurp()