import requests
from time import sleep
import asyncio
from bs4 import BeautifulSoup

check_code = 0
before = ""
after = ""

while check_code == 0:
    url = "http://skrclub.activities-club.com/?page=activities"                                                                                   #url="https://sites.google.com/view/test-for-rallychecker/%E0%B8%AB%E0%B8%99%E0%B8%B2%E0%B9%81%E0%B8%A3%E0%B8%81"
    web_data = requests.get(url)
    out = BeautifulSoup(web_data.text, 'html.parser')
    outstr = str(out)

    before += outstr
    after += outstr

    # Checking #
    if before != after:
        print("Web Updated !")
        before = ""
        after = ""
        check_code += 1   

    elif before == after:
        print("Checking...")

        before = ""
        after = ""
    sleep(2)