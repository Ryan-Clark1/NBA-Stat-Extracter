import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv

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
links = []

for y in Year:
    y = y - 17
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
                blink = soup.find_all('p', attrs={"class": "links"})

                for h in blink:
                    j = h.find_all('a')
                    for k in j:
                        t = k.get('href')
                        try:
                            if int(t[11]) > 0:
                                links.append(t)
                        except:
                            pass
            except:
                pass

file = open('link_list.csv', 'w+', newline='')
with file:
    write = csv.writer(file)
    write.writerows(links)

orig_search = 30 * len(Year) * 365
count = len(links)
saved_loops = orig_search - count
print(str(count) + " links collected, "+ str(saved_loops) + " loops saved")
