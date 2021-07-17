import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.theguardian.com/uk")

soup = BeautifulSoup(page.content, "html.parser")

# print(soup.prettify())

# list(soup.children)
# [type(item) for item in list(soup.children)]

# html = list(soup.children)[3]
# list(html.children)[3]

a_tags = soup.find_all("a", class_="js-headline-text")

# soup.find_all('a')[0].get_text()

for a_tag in a_tags:
    print(a_tag.get_text())

page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, "html.parser")
soup

soup.find_all("p", class_="outer-text")
soup.find_all(class_="outer-text")
soup.find_all(id="first")
soup.select("p")

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.YO9HsRNKjUI")
soup = BeautifulSoup(page.content, "html.parser")
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

img = tonight.find("img") #finding the thing
desc = img["title"] #finding the thing inside the thing
print(desc)

period_tags = seven_day.select("img")
desc = img["alt"]

[print(pt["alt"]) for pt in period_tags]

documents = ['doc1', 'doc2', 'doc3']
