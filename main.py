import requests
from bs4 import BeautifulSoup
import json

def search(c,text):
    data = {
        'do': 'search',
        'subaction': 'search',
        'search_start': c,
        'full_search': 0,
        'result_from': 1,
        'story': text 
    }

    response = requests.post("https://mp3uk.net/index.php?do=search", data=data)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        divs = soup.find_all("div", class_="track-item")

        data = []
        for div in divs:
            title = div.find("a").text.strip()
            time = div.find_all("div")[3].text.strip()
            full = div.find_all('a')[1]['href']
            data.append({"title": title, "time": time, "url": 'https:' + full})

        return data
    else:
        return None


text = input("name: ")
data = []
for e in range(6):
    result = search(e,text)
    if result:
        data.extend(result)
    else:
        break

print(json.dumps(data))
