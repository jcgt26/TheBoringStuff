import requests
from bs4 import BeautifulSoup

#Test site https://www.scrapethissite.com/pages/simple/
if __name__ == '__main__':
    url = 'https://www.scrapethissite.com/pages/simple/'

    response = requests.get(url)

    if response.status_code == 200:
        print("OK")
    else:
        print("Error")
        pass

    soup = BeautifulSoup(response.content, "html.parser")

    countries = soup.find_all("div", class_="country")
    for country in countries:
        country_name = country.find("h3", class_="country-name").text
        print(country_name)