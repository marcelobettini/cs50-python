# import json
from clear import clear_screen
import requests
import sys
if len(sys.argv) != 2:
    sys.exit("Must include artist or band in quotes")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])
o = response.json()
# print(json.dumps(o["results"],indent=1))
i=0
clear_screen()
for result in o["results"]:
    i+=1
    print(f'{"{:02d}".format(i)} - {result["trackName"]} #{result["trackId"]}')