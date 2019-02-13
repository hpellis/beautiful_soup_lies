import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

soup = BeautifulSoup(r.text, 'html.parser')

lies = soup.find_all('span', attrs={'class':'short-desc'})

number_of_lies = len(lies)


def get_lies():
    dict_of_lies = {}
    for item in lies:
        date = item.find('strong').text[0:-1] + ", 2017"
        lie = item.contents[1]
        explanation = item.find('a').text[1:-1]
        evidence = item.find('a')['href']
        dict_of_lies[date] = lie, explanation, evidence
        return dict_of_lies
    
print(dict_of_lies)
    
    