import requests
import re
from bs4 import BeautifulSoup as soup


def cleaner(toClean):
        toClean = toClean.lower()
        return re.sub("[^a-z0-9]","", toClean)

def getStats(): #second input not used
    
    myurl = "http://thunderskill.com/en/stat/Hazeyyyy/vehicles/r" ##type=army&role=all&country=all"

    response = requests.get(myurl, params={'type':'army'})
    print(response.status_code)
    with open('resp.html', 'w', encoding="utf-8") as fiil:
        print(response.content, file=fiil)

    sp = soup(response.content, 'html.parser')
    table = sp.find_all('table')[1]

    f = open("resp3.txt", "w", encoding="utf-8")
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        for column in columns:
            print(column.get_text(), file=f)
    f.close()

    # params = [
    #     "Battles",
    #     "Victories",
    #     "Defeats",
    #     "Deaths",
    #     "Overall ground frags"
    # ]

    # stats = {}
    # plane = ""
       
    # with open("resp2.txt", "r", encoding="utf-8") as infile:
    #     for line in infile:
    #         if re.search("^[ ][a-zA-z0-9]+", line) and "General" not in line:  
    #             plane = cleaner(line.strip())
    #             stats[plane] = {}
    #             continue
    #         for tag in params:
    #             if tag in line:
    #                 stats[plane][re.search("[A-Za-z ]+",line).group()] = int(re.findall('\d+', line)[0])
    #                 break
    # infile.close()

    
    # return stats

#resp = requests.get("http://thunderskill.com/en/stat/Hazeyyyy/vehicles/r")
getStats()