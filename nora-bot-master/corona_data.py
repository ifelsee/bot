import urllib.request
import bs4 as bs 
global image_url
global image_urls
def corona():
    sauce = urllib.request.urlopen("https://covid19.saglik.gov.tr").read()

    soup = bs.BeautifulSoup(sauce,"html.parser")

    images = soup.find("div",{"row"})
    image_number = 1
    image = images.find_all("img")
    for src in image :
        if image_number == 1:
            image_url = "https://covid19.saglik.gov.tr/"+src.get("src")
            image_number = image_number+1
        if image_number == 2:
            image_urls = "https://covid19.saglik.gov.tr/"+src.get("src")


    image_number = 1

   

    return  image_url,image_urls

