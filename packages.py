import requests
import json

import cowsay
import sys

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
t = response.json()
for result in t["results"]:
    print(result["trackName"])