import requests
from bs4 import BeautifulSoup as soup
import re
import os
import customHeap as CH

def cleaner(toClean):
        toClean = toClean.lower()
        return re.sub("[^a-z0-9]","", toClean)

def haskey(dic, key):
    if key in dic.keys():
        return True
    else: 
        return False

def dcpy(dic):
    ret = {}
    for key in dic.keys():
        ret[key] = dic[key]
    return ret

def checkEntry(entry, params):
    for key in params:
        if key not in entry.keys():
            return False
    return True

def stdoutStats(stats):
    for key in stats:
    #if "a" in key:
        print("----------")
        print(key)
        for key2 in stats[key]:
            print(("     {cat} : {entry}".format(cat=key2, entry=stats[key][key2])))

def strTag(stats):
    ret = ""
    k = 0
    d = 0
    for key in stats:
        ret+=("-----------\n")
        ret+=(key+"\n")
        for key2 in stats[key]:
            if "Overall air frags" in key2:
                k += int(stats[key][key2]) 
            if "Deaths" in key2:
                d += int(stats[key][key2])
            ret+=("     {cat} : {entry} \n".format(cat=key2, entry=stats[key][key2]))
    try:
        kd = k/d
        if kd<1:
            tag = "\n ... \nthis is a monke\n"
        elif kd<3:
            tag = "\n ... \nthey ok\n"
        else:
            tag = "\n ... \nit needs to stop camping af\n"       
    except:
        tag = ""  
    return ret+tag

def stroutStats(stats):
    ret = ""
    for key in stats:
        ret+=("-----------\n")
        ret+=(key+"\n")
        for key2 in stats[key]:
            ret+=("     {cat} : {entry} \n".format(cat=key2, entry=stats[key][key2]))
    return ret

def stroutArr(plist):
    ret = ""
    for plane in plist:
        ret += ("-----------\n")
        ret += plane["plane"] + "\n" 
        for key2 in plane:
            if "plane" not in key2:
                ret+=("     {cat} : {entry} \n".format(cat=key2, entry=plane[key2]))
    return ret


def stroutPlane(plane, name):
    ret = "-----------\n"
    ret += (name + "\n")
    for key in plane:
        ret+=("     {cat} : {entry} \n".format(cat=key, entry=str(plane[key])))
    return ret


def getStats(username, role="fighters"):
    
    myurl = "http://thunderskill.com/en/stat/"+username+"/vehicles/r#type=aviation&role="+role+"&country=all"

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
                if plane != "" :
                    if not checkEntry(stats[plane],params):
                        del stats[plane]  
                    else:
                        stats[plane]["KD"] = getKD(stats[plane])  
                
                plane = cleaner(line.strip())
                stats[plane] = {}
                continue
            for tag in params:
                if tag in line:
                    stats[plane][re.search("[A-Za-z ]+",line).group()] = int(re.findall('\d+', line)[0])
                    break
    infile.close()

    os.remove("resp2.txt")
    return stats

def getReq(stats, req):
    ret = {}
    search = cleaner(req)
    for key in stats:
        if search in key:
            ret[key] = stats[key]
    return ret

def getWorst(stats, battlemin, ct):
    h = CH.objHeap("KD", False)
    ret = []
    for plane in stats:
        newDict = dcpy(stats[plane])
        newDict["plane"] = plane
        h.push(newDict)
    
    for i in range(0,ct):
        ret.append(h.pop())
    return ret

def getBest(stats, battlemin, ct):
    h = CH.objHeap("KD", True)
    ret = []
    for plane in stats:
        newDict = dcpy(stats[plane])
        newDict["plane"] = plane
        h.push(newDict)
    
    for i in range(0,ct):
        ret.append(h.pop())
    return ret
    

def getKD(plane):
    if haskey(plane,"Overall air frags") and haskey(plane,"Deaths"):
        try:
            ret = plane["Overall air frags"]/plane["Deaths"]
            return ret
        except:
            ret = 999999999999
            return ret
    else:
        return None





def req_stat_plane(username, searchStr):
    return stroutStats(getReq(getStats(username), searchStr))

def req_worst(username, battlemin, ct):
    return stroutArr(getWorst(getStats(username),battlemin, ct))

def req_best(username, battlemin, ct):
    return stroutArr(getBest(getStats(username),battlemin,ct))

# print(req_worst("TheCorkster"))

