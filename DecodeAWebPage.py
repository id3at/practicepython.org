from bs4 import BeautifulSoup
import  requests

source = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/kraków;wp?rd=0")
src = source.content

source1 =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Krak%C3%B3w&d=0")
src1 = source1.content


soup = BeautifulSoup(src, 'lxml')
soup1 = BeautifulSoup(src1, 'lxml')

oferta = []
czas = []
firma = []
adres = []

for article in soup.find_all("h3", class_="offer-details__title"):
    oferta.append(article.text)
    tag = article.find("a", class_="offer-details__title-link")
    adres.append(tag.attrs["href"])
    
for article in soup.find_all("a", class_="offer-company__name"):
    firma.append(article.text)

for article in soup1.find_all("h2", class_="p-job-title"):
    oferta.append(article.text)
    tag = article.find("a" )
    adres.append(f'https://www.infopraca.pl{tag.attrs["href"]}')


for article in soup1.find_all("h3", class_="p-name company"):
    firma.append(article.text)


for t in soup.find_all("span", class_="offer-actions__date"):
    data = t.text
    czas.append(data)

for t in soup1.find_all("span", class_="last-update"):
    data2 = t.text
    czas.append(data2)


for t in range(len(oferta)):
    print(oferta[t].strip())
    print(firma[t].strip())
    print(adres[t].strip())
    print(czas[t].strip())
    print()
input()
