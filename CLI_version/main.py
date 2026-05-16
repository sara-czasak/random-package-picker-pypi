import requests
from bs4 import BeautifulSoup
import random


r = requests.get("https://pypi.org/simple/")
soup = BeautifulSoup(r.text, 'html.parser')


packages = soup.find_all('a')
names = [i.text for i in packages]
