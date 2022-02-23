import requests
from bs4 import BeautifulSoup as BS


r = requests.get("https://invest.yandex.ru/catalog/currency/")
html = BS(r.content, "html.parser")

a = html.find_all(class_="JGT__mSaFfXxcOb2oGto")
for i in a:
    print(i.text)
print()
b = html.find_all(class_="FKk_VD_UBO4sS_Tt6IHI")
for i in b:
    print(i.text)