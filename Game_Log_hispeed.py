import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv


links = []

with open('link_list.csv', 'r') as data:
    for line in csv.reader(data):
        line = ''.join(line)
        links.append(line)

for link in links:
    try:
        m = link[15:17]
        y = link[11:15]
        d = link[17:19]
        t = link[20:23]
        status = int(links.index(link))/len(links)
        print("{0:.4%}".format(status))
        date = str(m) + "/" + str(d) + "/" + str(y)
        url = "https://www.basketball-reference.com" + link
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', id="box-" + t + "-game-advanced")
        cell = table.find_all('td')
        player = table.find_all('th', attrs={"class": "left"})
        headers = table.find_all('th', attrs={"class": "center"})
        data = table.find_all('td', attrs={"class": "right"})
        Categories = []
        Players = []
        Data = []
        for item in player:
            Players.append(item.text)

        for item in headers:
            Categories.append(item.text)
        Categories = Categories[1:]

        for item in data:
            Data.append(item.text)

        dset = []
        x = 0

        while x < len(Players):
            dset.append(Players[x])
            i = x * 16
            while i < x * 16 + 16 and i < len(Data):
                dset.append(Data[i])
                i += 1
            dset.append(date)
            x += 1

        masterset = []
        z = 0

        while z < len(dset):
            masterset.append(dset[z:z + 18])
            z += 18

        Categories = Categories[:17]
        Categories.remove("Starters")
        Categories.insert(0, "Player")
        Categories.remove("Reserves")
        Categories.append("BPM")
        Categories.append("Date")
        dfobj_advanced = pd.DataFrame(masterset, columns=Categories)
        table = soup.find('table', id="box-"+t+"-game-basic")
        cell = table.find_all('td')
        player = table.find_all('th', attrs={"class": "left"})
        headers = table.find_all('th', attrs={"class": "center"})
        data = table.find_all('td', attrs={"class": "right"})

        Categories = []
        Players = []
        Data = []
        for item in player:
            Players.append(item.text)

        for item in headers:
            Categories.append(item.text)

        for item in data:
            Data.append(item.text)

        dset = []
        x = 0
        while x < len(Players):
            dset.append(Players[x])
            i = x * 20
            while i < x * 20 + 20 and i < len(Data):
                dset.append(Data[i])

                i += 1
            dset.append(date)
            x += 1
        masterset = []
        z = 0
        while z < len(dset):
            masterset.append(dset[z:z + 22])
            z += 22
        Categories = Categories[1:22]
        Categories.remove("Starters")
        Categories.insert(0, "Player")
        Categories.remove("Reserves")
        Categories.append("+/-")
        Categories.append("Date")
        dfobj_basic = pd.DataFrame(masterset, columns=Categories)
        csv_file = dfobj_basic.to_csv(t+d+"_"+m+"_"+y+'_basic.csv', index=True)
        csv_file_dup = dfobj_advanced.to_csv(t + d + "_" + m + "_" + y + '_advanced.csv', index=True)

    except:
        pass
