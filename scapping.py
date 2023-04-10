import requests
from bs4 import BeautifulSoup

try:
    req = requests.get("https://stackoverflow.com/questions/tagged/python")
    req.raise_for_status()

    soup = BeautifulSoup(req.text,"html.parser")

    ques= soup.select('div.s-post-summary--content h3')
    for q in ques:
        name = q.find('a').text
        
        print(name)

    print(len(ques))

except Exception as e:
    print(e)