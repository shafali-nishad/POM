import json


def json_credentials(filepath):
    with open(filepath) as data:  #open the path and save data in data variable as string
        creds= json.load(data)                         #string is converted to json via json load
        return creds