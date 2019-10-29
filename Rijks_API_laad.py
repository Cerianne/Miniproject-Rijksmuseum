import http.client, urllib.parse, json

# https://www.rijksmuseum.nl/api/nl/collection?key=UYzK8jDV&format=json&type=schilderij&f.normalized32Colors.hex=%20%23367614


params = urllib.parse.urlencode({
    'p': '0',
    'ps': '100',
    'q': input("naam :")
})
conn = http.client.HTTPSConnection('www.rijksmuseum.nl')
conn.request("GET", "/api/nl/collection?key=UYzK8jDV&format=json&" + params)

response = conn.getresponse()
responsetext = response.read()
data = json.loads(responsetext)
schilderij = data["artObjects"]

print("count = {}".format(data["count"]))

for data in schilderij:
    print("{:40} \t {:60} \t {:15}".format(data["principalOrFirstMaker"], data["title"], data["objectNumber"]))

with open("search_result.json", "w") as json_file:
    json.dump(schilderij, json_file, indent=4)
