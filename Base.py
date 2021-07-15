import requests
from bs4 import BeautifulSoup
import pandas as pd
Year = [2020, 2021]
Month = []
Day = []
i=1
while i < 13:
    Month.append(i)
    i += 1
i=1
while i < 32:
    Day.append(i)
    i += 1

for y in Year:
    y = str(y)
    for m in Month:
        m = str(m)
        for d in Day:
            d = str(d)
            print(m + "/" + d)
            date = str(m) + "/" + str(d) + "/" + str(y)
            try:
                if int(m) < 10 and int(d) < 10:
                    link = "https://www.basketball-reference.com/boxscores/" + y + "0"+m + "0"+d + "0PHI.html"

                    html = requests.get(link).content
                    soup = BeautifulSoup(html, 'html.parser')
                elif int(m) < 10:
                    link = "https://www.basketball-reference.com/boxscores/" + y + "0" + m + d + "0PHI.html"
                    html = requests.get(link).content
                    soup = BeautifulSoup(html, 'html.parser')
                elif int(d) < 10:
                    link = "https://www.basketball-reference.com/boxscores/" + y + m + "0" + d + "0PHI.html"
                    html = requests.get(link).content
                    soup = BeautifulSoup(html, 'html.parser')
                else:
                    link = "https://www.basketball-reference.com/boxscores/" + y + m + d + "0PHI.html"
                    html = requests.get(link).content
                    soup = BeautifulSoup(html, 'html.parser')


                table = soup.find('table', id="box-PHI-game-advanced")
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
                    x += 1

                masterset = []
                z = 0

                while z < len(dset):
                    masterset.append(dset[z:z + 17])
                    z += 17

                Categories = Categories[:17]
                Categories.remove("Starters")
                Categories.insert(0, "Player")
                Categories.remove("Reserves")
                Categories.append("BPM")
                masterset.append(date)
                Categories.append("Date")
                dfobj_advanced = pd.DataFrame(masterset, columns=Categories)


                table = soup.find('table', id="box-PHI-game-basic")
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
                    dset.append(m+"/"+d+"/"+y)
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

                Tot = [dfobj_basic, dfobj_advanced]
                fin = pd.concat(Tot)
                csv_file = fin.to_csv('Sixers'+d+"_"+m+"_"+y+'.csv', index=True)
            except:
                print("no game")
                pass








