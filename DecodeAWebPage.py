"""
Autor: Tomasz Głuc
Wyszukiwajka :D
"""

from bs4 import BeautifulSoup
import  requests

################################
source = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/kraków;wp?rd=0")
src = source.content
soup = BeautifulSoup(src, 'lxml')

sourcekro = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/krosno;wp?rd=0")
srckro = sourcekro.content
soupkro = BeautifulSoup(srckro, 'lxml')

sourcesan = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/sanok;wp?rd=0")
srcsan = sourcesan.content
soupsan = BeautifulSoup(srcsan, 'lxml')

sourcerzesz = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/rzeszów;wp?rd=0")
srcrzesz = sourcerzesz.content
souprzesz = BeautifulSoup(srcrzesz, 'lxml')

sourcejas = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/jasło;wp?rd=0")
srcjas = sourcejas.content
soupjas = BeautifulSoup(srcjas, 'lxml')

sourceboch = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/bochnia;wp?rd=0")
srcboch = sourceboch.content
soupboch = BeautifulSoup(srcboch, 'lxml')

sourcetar = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/tarnów;wp?rd=0")
srctar = sourcetar.content
souptar = BeautifulSoup(srctar, 'lxml')

sourceskaw = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/skawina;wp?rd=0")
srcskaw = sourceskaw.content
soupskaw = BeautifulSoup(srcskaw, 'lxml')

sourcewado = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/wadowice;wp?rd=0")
srcwado = sourcewado.content
soupwado = BeautifulSoup(srcwado, 'lxml')

sourceandry = requests.get("https://www.pracuj.pl/praca/operator%20cnc;kw/andrychów;wp?rd=50")
srcandry = sourceandry.content
soupandry = BeautifulSoup(srcandry, 'lxml')

#################################

source1 =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Kraków&d=50")
src1 = source1.content
soup1 = BeautifulSoup(src1, 'lxml')

source1kro =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Krosno&d=50")
src1kro = source1kro.content
soup1kro = BeautifulSoup(src1kro, 'lxml')

source1jasl =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Jasło&d=50")
src1jasl = source1jasl.content
soup1jasl = BeautifulSoup(src1jasl, 'lxml')

source1san =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Sanok&d=50")
src1san = source1san.content
soup1san = BeautifulSoup(src1san, 'lxml')

source1Rzesz =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Rzeszów&d=50")
src1Rzesz = source1Rzesz.content
soup1Rzesz = BeautifulSoup(src1Rzesz, 'lxml')

source1tarn =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Tarnów&d=50")
src1tarn = source1tarn.content
soup1tarn = BeautifulSoup(src1tarn, 'lxml')

source1bochn =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Bochnia&d=0")
src1bochn = source1bochn.content
soup1bochn = BeautifulSoup(src1bochn, 'lxml')

source1skaw =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Skawina&d=3")
src1skaw = source1skaw.content
soup1skaw = BeautifulSoup(src1skaw, 'lxml')

source1wado =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Wadowice&d=10")
src1wado = source1wado.content
soup1wado = BeautifulSoup(src1wado, 'lxml')

source1adnry =  requests.get("https://www.infopraca.pl/praca?q=operator+cnc&lc=Andrychów&d=0")
src1adnry = source1adnry.content
soup1adnry = BeautifulSoup(src1adnry, 'lxml')

#################################################
oferta = []
czas = []
firma = []
adres = []
"""
pracujpl
"""
def pracujpl(x):
    
    for article in x.find_all("h3", class_="offer-details__title"):
        oferta.append(article.text)
        tag = article.find("a", class_="offer-details__title-link")
        adres.append(tag.attrs["href"])
        
    for article in x.find_all("a", class_="offer-company__name"):
        firma.append(article.text)
    
    for t in x.find_all("span", class_="offer-actions__date"):
        data = t.text
        czas.append(data)

###############################################################

"""
infopraca
"""
def infopraca(x):
    for article in x.find_all("h2", class_="p-job-title"):
        oferta.append(article.text)
        tag = article.find("a" )
        adres.append(f'https://www.infopraca.pl{tag.attrs["href"]}')
    
    for article in x.find_all("h3", class_="p-name company"):
        firma.append(article.text)
    
    for t in x.find_all("span", class_="last-update"):
        data2 = t.text
        czas.append(data2)
#######################################################################

pracujpl(soup)
pracujpl(soupkro)
pracujpl(soupsan)
pracujpl(souprzesz)
pracujpl(soupjas)
pracujpl(soupboch)
pracujpl(souptar)
pracujpl(soupskaw)
pracujpl(soupwado)
pracujpl(soupandry)

infopraca(soup1)
infopraca(soup1kro)
infopraca(soup1jasl)
infopraca(soup1san)
infopraca(soup1Rzesz)
infopraca(soup1tarn)
infopraca(soup1bochn)
infopraca(soup1skaw)
infopraca(soup1wado)
infopraca(soup1adnry)

for t in range(len(oferta)):
    print(oferta[t].strip())
    print(firma[t].strip())
    print(adres[t].strip())
    print(czas[t].strip())
    print()
input()
