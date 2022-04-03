import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint
import json
from config import urls
import time

headres = {'content-type': 'application/json',
           'X-Retpath-Y': 'https://invest.yandex.ru/catalog/stock/',
           'x-ssr-id': '8e52a78926a8e05fbe014274094f5c9d',
           'x-tanker-branch': 'master',
           'x-visible-uid': '883187617',
           'x-csrf-token': '805a024c50c4e1ea46103f07593f97a007831c3f:1648980103',
           'Cookie': 'yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; is_gdpr=0; is_gdpr_b=CIayFBDgWSgC; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; mda=0; my=YwA=; yandex_gid=141075; _ym_d=1646636780; _ym_isad=2; Session_id=3:1648930876.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:250351.906862.f9yBA7XrLdnkaUZVJ3D9weBtfCI; sessionid2=3:1648930876.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:250351.906862.f9yBA7XrLdnkaUZVJ3D9weBtfCI; i=P4LZY/kmCKVsJpcqBDFI9VCcTVeFozSw++sP2A3eqppbiKc+AYbF4FbB/BwKkk0q9d794Pi1mldi5aD0JNIyAujqROI=; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.3.0.2430:w:d:RU:20211231; cycada=cK2JuQ9Cuu+LQ/HCCnHYPraqTBF4gvSVGzF6KKxkNI0=; stockChart.seriesType=area; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1648981370001784-11595579900118636286-vla1-4623-vla-l7-balancer-8080-BAL-6197#ybzcc.ru#newsca.native_cache; _yasc=3GfAuIorLww5mq/2zBsFANDwHlM+014IW0C0YSLiIX0quez32Ns+J5FisacwljxUvPVZIuGB77l6pA==; yabs-frequency=/5/0G0V09DlIM87GKbY/Uwi3wsa5ArFiHI40/; yp=1672495029.cld.2261448#1672495029.brd.0699000036#1657951229.szm.1_25:1536x864:1536x726#1649228778.ygu.1#1649315189.csc.1#1649185034.mct.null#1649067766.nwcst.1648982400_43_3#1649538359.mcv.0#1649538359.mcl.1695r7s#1648991592.gpauto.55_796288:49_108795:100000:3:1648984392'
           }

json_ = {"operationName": "CatalogContentForNormal",
        "variables": {"type": "share", "searchText": None, "order": "desc", "sort": "day_trade_volume_in_rub",
                      "filters": [], "customOrder": None, "count": 1000000, "cursor": None},
        "query": "query CatalogContentForNormal($type: InstrumentType!, $searchText: String, $filters: [InstrumentFilter!]!, $sort: InstrumentListSort!, $order: SortOrder!, $customOrder: String, $count: Int!, $cursor: String) {\n  instruments {\n    list(types: [$type], query: $searchText, filters: $filters, sort: $sort, order: $order, customOrder: $customOrder, count: $count, cursor: $cursor) {\n      cursor\n      results {\n        id\n        type\n        slug\n        ticker\n        displayName\n        logoId\n        taxFree\n        commissionFree\n        favorite\n        marketData {\n          id\n          accruedInterest\n          price\n          priceStep\n          lotSize\n          currencyCode\n          percentChange: yearlyPercentChange\n          absoluteChange: yearlyAbsoluteChange\n          dailyPercentChange: percentChange\n          dailyAbsoluteChange: absoluteChange\n          __typename\n        }\n        ... on ShareInstrumentItem {\n          stockRiskLevel\n          stockRiskScoreFormatted\n          __typename\n        }\n        ... on EtfInstrumentItem {\n          stockRiskLevel\n          stockRiskScoreFormatted\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}


def stonks():
    r = requests.post("https://invest.yandex.ru/graphql?operation=CatalogContentForNormal", json=json_,
                      headers=headres)
    cont = json.loads(r.text)
    # pprint(r.text)
    a = cont['data']['instruments']['list']['results']
    name = []
    logoId = []
    yeardinamic = []
    daydinamic = []
    dang = []
    price = []
    cur = []
    for i in a:
        # pprint(i)
        name.append(i['displayName'])
        logoId.append(i['ticker'])
        yeardinamic.append(i['marketData']['percentChange'])
        daydinamic.append(round(i['marketData']['dailyPercentChange'], 2))
        dang.append(int(i['stockRiskScoreFormatted']) if i['stockRiskScoreFormatted'] else 11)
        cur.append(i['marketData']['currencyCode'])
        price.append(i['marketData']['price'])
        #print('-----------')
    #pprint(name)
    for i in sorted(list(zip(name, logoId, yeardinamic, daydinamic, dang, price, cur)), key=lambda x: (x[-3], x[-1], x[0])):
        print(i)



headers = {'cookie': 'news_lang=ru; nc=search-visits-per-week=1:1645123721000#tips=1645798458637%3Bfavorites-button:1; yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; is_gdpr=0; is_gdpr_b=CIayFBDgWSgC; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; mda=0; font_loaded=YSv1; my=YwA=; yandex_gid=141075; _ym_d=1646636780; _ym_isad=2; Session_id=3:1648930876.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:250351.906862.f9yBA7XrLdnkaUZVJ3D9weBtfCI; sessionid2=3:1648930876.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:250351.906862.f9yBA7XrLdnkaUZVJ3D9weBtfCI; i=P4LZY/kmCKVsJpcqBDFI9VCcTVeFozSw++sP2A3eqppbiKc+AYbF4FbB/BwKkk0q9d794Pi1mldi5aD0JNIyAujqROI=; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.3.0.2430:w:d:RU:20211231; yabs-frequency=/5/0G0V09DlIM87GKbY/Uwi3wsa5ArFiHI40/; _yasc=nI/LzQHjTvQRb0qP7l8ZKzhNBODFqnYlUbLFvZzVMSxe2Z7zl3ihfI2WqB53dTJb4s1eKbDKSQkPug==; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1648989185386508-3330288641589190498-vla1-4623-vla-l7-balancer-8080-BAL-6258#ybzcc.ru#newsca.native_cache; _ym_visorc=w; yp=1672495029.cld.2261448#1672495029.brd.0699000036#1657951229.szm.1_25:1536x864:1536x726#1649228778.ygu.1#1649315189.csc.1#1649185034.mct.null#1649067766.nwcst.1648982400_43_3#1649538359.mcv.0#1649538359.mcl.1695r7s#1649001192.gpauto.55_796288:49_108795:100000:3:1648993992; cycada=zyYNyq0LxmtTDlf5OyTyALaqTBF4gvSVGzF6KKxkNI0=',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36'}

def get_news(url):
    try:
        r = requests.get(url, headers=headers)
        html = BS(r.text, "html.parser")
        # print(html)
        if url == "https://yandex.ru/news":
            html = html.find(class_="mg-grid__row mg-grid__row_gap_8 news-top-flexible-stories news-app__top")
        news = html.find_all(class_="mg-card__title")
        ur = html.find_all(class_="mg-card__link")
        # print(news, ur)
        return news, ur
    except Exception as error:
        print(error)
        print("bad")
        return [], ""

pprint(get_news(urls[0]))