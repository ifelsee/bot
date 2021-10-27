import urllib.request
import bs4 as bs 
import pipreqs

def saat():

    sauce = urllib.request.urlopen("https://www.timeanddate.com/worldclock/turkey/istanbul").read()

    soup = bs.BeautifulSoup(sauce,"html.parser")

    gelen_data = soup.find_all("span",{"id":"ct"})

    saat = gelen_data[0].text

    return saat

dss = "Users\Burak\AppData\Local\Programs\Python\Python38\Scripts"

print(pipreqs.__package__)