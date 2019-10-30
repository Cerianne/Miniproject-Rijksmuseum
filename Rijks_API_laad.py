import http.client, urllib.parse, json


# opvragen

def opvragenKunststuk(invoer):
    params = urllib.parse.urlencode({
        'p': '0',
        'ps': '1',
        'q': str(invoer)
    })

    conn = http.client.HTTPSConnection('www.rijksmuseum.nl')
    conn.request("GET", "/api/nl/collection?key=UYzK8jDV&format=json&" + params)

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
    params = urllib.parse.urlencode({
        'p': '0',
        'ps': '1',
        'q': str(invoer)
    })

    conn = http.client.HTTPSConnection('www.rijksmuseum.nl')
    conn.request("GET", "/api/nl/collection?key=UYzK8jDV&format=json&" + params)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)
    schilderij = data["artObjects"]
    for data in schilderij:
        return data["webImage"]["url"]


# invoer

text = input("titel van het kunstwerk: ")

print(opvragenKunststuk(text))
print(imgKunstwerk(text))
