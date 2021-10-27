import urllib.request
import bs4 as bs 

def deprem():
    sauce = urllib.request.urlopen("http://www.koeri.boun.edu.tr/scripts/lasteq.asp").read()


    soup = bs.BeautifulSoup(sauce,"html.parser")

    gelen_data = soup.find_all("pre")
    gelen_data = str(gelen_data)
    gelen_data = gelen_data[200:1250]
    
    return gelen_data
