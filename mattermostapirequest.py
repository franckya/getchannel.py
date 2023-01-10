import json
import requests
import os

mytoken = '<enter your access token here'
apiurl = 'https://chat.opennms.com/api/v4/'
page = 0
per_page = 100
fetch = 1


while(fetch):
    r = requests.get(apiurl + '/channels?page=' + str(page) + '&per_page=' + str(per_page), headers={"Authorization": "Bearer " + mytoken})
    data = r.json()
    json_len = len(data)
    page = page + 1
    print("Page " + str(page) + " Length: " + str(json_len))
    for record in data:
        display_name = record['display_name']
        channel_type = record['type']
        team_id = record['team_id']

        print(display_name + '      ' + channel_type + '     ' + team_id)

    if json_len < per_page:
        fetch = 0
