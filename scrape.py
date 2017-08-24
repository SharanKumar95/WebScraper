import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Resource_Reservation_Protocol'
response = requests.get(url)
html = response.content

soup=BeautifulSoup(html)
table=soup.find('table',attrs={'class':'vertical-navbox nowraplinks hlist'})
list_of_rows=[]
for row in table.findAll('tr')[1:]:
    list_of_cells=[]
    for cell in row.findAll('a'):
         # print row.prettify()
         text= cell.text
         list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
#print list_of_rows

outfile=open("./inmates.csv","wb")
writer= csv.writer(outfile)
writer.writerow(["Last"])
writer.writerows(list_of_rows)
