from datetime import date
import urllib.request
from bs4 import BeautifulSoup
def price(wiki):
    today = date.today()
    page = urllib.request.urlopen(wiki)
    soup = BeautifulSoup(page,features="lxml")
    right_table=soup.find('table')
    A=[]
    B=[]
    C=[]
    D=[]
    i = 0
    for row in right_table.findAll("tr"):
        cells = row.findAll('td')
        if len(cells)==4 and i!=0:
            A.append(" ".join(cells[0].find(text=True).split(" ")))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
        elif i==0:
            i+=1
    return (today,len(A),A,B,C,D)