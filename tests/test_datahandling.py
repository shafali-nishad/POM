import pytest
import json
from playwright.sync_api import Playwright

@pytest.mark.dh
def test_json_credentials():
    with open("testData//creds.json") as data:  #open the path and save data in data variable as string
        creds= json.load(data)                         #string is converted to json via json load
        print(creds["username"])
        print(creds["password"])
        print(creds)