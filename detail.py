import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
Year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
Month = []
Day = []

i = 1
while i < 13:
    Month.append(i)
    i += 1
i = 1
while i < 32:
    Day.append(i)
    i += 1

box_links = []
for y in Year:
    y = str(y)
    for m in Month:
        m = str(m)
        for d in Day:
            d = str(d)
            status = 1 - (Year[len(Year)-1] - (int(y)-1))/len(Year) + ((int(m)/12) * 1/len(Year)) + (int(d)/30 * 1/12 * 1/len(Year))
            print("{0:.8%}".format(status))
            try:
                date = str(m) + "/" + str(d) + "/" + str(y)
                link = "https://www.basketball-reference.com/boxscores/index.fcgi?month=" + m + "&day=" + d + "&year=" + y
                html = requests.get(link).content
                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find_all('table')
                cell = table[1]
                z = cell.find_all('td')
                games = soup.find('div', attrs={"class": "section_heading"})

                if len(games.text) == 11:
                    game_count = games.text[0]
                else:
                    game_count = games.text[:1]

                gam = soup.find_all('div', attrs={"class": "game_summary expanded nohover"})


                z = 0
                game_bank = []
                running_record = []

                try:
                    while z < int(game_count):
                        t1 = gam[z].text
                        t2 = t1.split("\n")
                        for t in t2:
                            if len(t) < 2:
                                pass
                            else:
                                game_bank.append(t)
                        AQ = game_bank[8]
                        HQ = game_bank[10]
                        fin_game_bank = [game_bank[0], game_bank[1], game_bank[3], game_bank[4], AQ[:2], AQ[2:4], AQ[4:6],
                                         AQ[6:8], HQ[:2], HQ[2:4], HQ[4:6], HQ[6:8], date]
                        running_record.append(fin_game_bank)
                        game_bank.clear()
                        z += 1

                    Headers = ['Away Team', 'Away Total', 'Home Team', 'Home Total', 'AQ1', 'AQ2', 'AQ3', 'AQ4', 'HQ1', 'HQ2',
                               'HQ3', 'HQ4', 'Date']
                    game_record = pd.DataFrame(running_record, columns=Headers)
                    csv_file = game_record.to_csv(d + "_" + m + "_" + y + '_game_record.csv', index=True)
                except:
                    pass
            except:
                pass
