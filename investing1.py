import requests
import json
from bs4 import BeautifulSoup as BS
from pprint import pprint
from config import urls1
import investing
from tqdm import tqdm


def stonks():
    name = []
    logoId = []
    yeardinamic = []
    daydinamic = []
    dang = []
    price = []
    cur = []
    lot = []
    country = []
    # urls = []
    # r = requests.get(f'https://ru.tradingview.com/markets/stocks-australia/market-movers-active/')
    # # pprint(r.headers)
    # html = BS(r.content, "html.parser")
    # # pprint(html)
    # info = html.find_all(class_="tv-dropdown__item")
    # for i in info:
    #     k = i.get('href')
    #     urls.append(k)
    # # pprint(info)
    # pprint(urls)
    m = 9

    for url in tqdm(urls1):
        # print(9999999999999999999)
        r = requests.get(f'https://ru.tradingview.com{url}')
        # pprint(r.headers)
        html = BS(r.content, "html.parser")
        # pprint(html)
        info = html.find_all(class_="apply-common-tooltip tickerDescription-absbzmSX")
        for i in info:
            country.append(url[16:-22])
            name.append(i.text)
        info = html.find_all(class_="apply-common-tooltip tickerName-absbzmSX")
        for i in info:
            logoId.append(i.text)
        info = html.find_all(class_="cell-s_9Ijkac right-s_9Ijkac")
        for i in info:
            # print(i.text, m)
            if m % 9 == 0:
                # print(i.text)
                price.append(i.text)
            elif (m - 1) % 9 == 0:
                daydinamic.append(i.text)
            elif (m - 2) % 9 == 0:
                yeardinamic.append(i.text)
            m += 1

        # info = html.find_all(class_="positive-f5bMRjbU")
        # for i in info:
        #     daydinamic.append(i.text)
        # info = html.find_all(class_="positive-zEOE7Eks")
        # for i in info:
        #     yeardinamic.append(i.text)
        # info = html.find_all(class_="currency-MpDQfFSW")
        # for i in info:
        #     if '0' not in i.text:
        #         print(i.text)
        #     cur.append(i.text)
        info = html.find_all(class_="container-RxISLojp buy-RxISLojp")
        for i in info:
            lot.append(i.text)
        info = html.find_all(class_="link-lkhtkaCQ")
        for i in info:
            dang.append(i.text)
        # html = html.split('\n')
    for i in [name, logoId, yeardinamic, daydinamic, dang, price, cur, lot, country]:
        i += ['Неизвестно'] * (len(name) - len(i))
    # print([len(i) for i in [name, logoId, yeardinamic, daydinamic, dang, price, cur, lot, country]])
    all_stonks = list(zip(name, logoId, yeardinamic, daydinamic, dang, price, [''] * len(name), lot, country)) + investing.stonks()
    print('СБОР АКЦИЙ ЗАВЕРШЕН')
    return all_stonks


# pprint(sorted(stonks()))
# stonks()
