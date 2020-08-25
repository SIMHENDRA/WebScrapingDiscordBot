import requests
from bs4 import BeautifulSoup as soup
import re
import os

def cleaner(toClean):
        toClean = toClean.lower()
        return re.sub("[^a-z0-9]","", toClean)

def stdoutStats(stats):
    for key in stats:
    #if "a" in key:
        print("----------")
        print(key)
        for key2 in stats[key]:
            print(("     {cat} : {entry}".format(cat=key2, entry=stats[key][key2])))

def stroutStats(stats):
    ret = ""
    for key in stats:
        ret+=("-----------\n")
        ret+=(key+"\n")
        for key2 in stats[key]:
            if "Overall air frags" in key2:
                k = int(stats[key][key2]) 
            if "Deaths" in key2:
                d = int(stats[key][key2])
            ret+=("     {cat} : {entry} \n".format(cat=key2, entry=stats[key][key2]))
    try:
        kd = k/d
        if kd<1:
            tag = "this is a monke\n"
        elif kd<3:
            tag = "they ok\n"
        else:
            tag = "it needs to stop camping af\n"
        
    except:
        tag = ""
  
    return ret+tag

def getStats(username, req):
    
    myurl = "http://thunderskill.com/en/stat/"+username+"/vehicles/r#type=aviation&role=all&country=all"

    response = requests.get(myurl)

    sp = soup(response.content, 'html.parser')
    table = sp.find_all('table')[0]

    f = open("resp2.txt", "w", encoding="utf-8")
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        for column in columns:
            print(column.get_text(), file=f)
    f.close()

    params = [
        "Battles",
        "Victories",
        "Defeats",
        "Deaths",
        "Overall air frags"
    ]

    stats = {}
    plane = ""
       
    with open("resp2.txt", "r", encoding="utf-8") as infile:
        for line in infile:
            if re.search("^[ ][a-zA-z0-9]+", line) and "General" not in line:            
                plane = cleaner(line.strip())
                stats[plane] = {}
                continue
            for tag in params:
                if tag in line:
                    stats[plane][re.search("[A-Za-z ]+",line).group()] = re.findall('\d+', line)[0]
                    break
    infile.close()
    
    ret = {}
    search = cleaner(req)
    for key in stats:
        if search in key:
            ret[key] = stats[key]

    os.remove("resp2.txt")
    return ret

