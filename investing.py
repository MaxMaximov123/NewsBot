import requests
import json
from bs4 import BeautifulSoup as BS
from pprint import pprint


def stonks():
    head = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'invest.yandex.ru',
        'If-None-Match': 'W/"446cb-XBOh/QJACgpX8eltc7AWg8ARV3c"',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.148 YaBrowser/22.7.2.899 Yowser/2.5 Safari/537.36',
        'Cookie': 'yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; is_gdpr=0; is_gdpr_b=CIayFBDgWSgC; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; my=YwA=; mda=0; yandex_gid=141075; _ym_d=1657999835; skid=5722487791658000552; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.7.2.899:w:d:RU:20211231; yabs-frequency=/5/2m0Z0CR2wsAe5DDY/; cycada=EAe8j3MLNd4V3whoMNWAQSfKy+ZxuPsLMvq5e/TxuI4=; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1659870280624392-7467880278375897754-sas6-5261-bf6-sas-l7-balancer-8080-BAL-457#ybzcc.ru#newsca.native_cache; i=UdhLa3rD6iH/7Ty7RH3YoNcs3nCrb4rozT35KignVTkMRqv09BM7oK777IQdLPxkfkJmVcl3qQhi4P6bcVSwvE+N/yI=; Session_id=3:1659870292.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:10256407.393485.0Fu41h6Z4lUD_klMk8ujWPJvCyc; sessionid2=3:1659870292.5.0.1640959007634:roHMsg:27.1.2:1.499:1|883187617.0.2|3:10256407.452383.k9dOKhBq4tOrWvq-2n03kWZBQSw; _ym_isad=2; _ym_visorc=b; yp=1659956613.uc.ru#1659956613.duc.ru#1681416026.cld.2261448#1681416026.brd.0699000036#1660591832.ygu.1#1973359832.skin.d#1660678244.csc.1#1659878013.gpauto.55_877659:49_746181:140:1:1659870813#1660475091.mcv.6#1660475091.mcl.1695r7s#1660475092.szm.1_125:1536x864:1707x833; _yasc=We33CXVBOPQt0+IwU87W3HsyahApucvV74uhunapa7nv6FyWJTwzL8+XYmJt0kfQxaytfkyF'
        }
    r = requests.get('https://invest.yandex.ru/catalog/stock/', headers=head)
    # pprint(r.headers)
    html = str(BS(r.content, "html.parser").contents)
    a = ''
    html = html.split('\n')
    # pprint(html)
    for i in html:
        if 'TOKEN' in i.upper():
            # print(i.split('"'))
            a = i.split('"')[1]
    headres = {'content-type': 'application/json',
               'X-Retpath-Y': 'https://invest.yandex.ru/catalog/stock/',
               'x-ssr-id': '5c44dab40aac0dcbedc24a60ef434676',
               'x-tanker-branch': 'master',
               'x-visible-uid': '883187617',
               'x-csrf-token': a,
               'Cookie': 'yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; is_gdpr=0; is_gdpr_b=CIayFBDgWSgC; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; my=YwA=; mda=0; yandex_gid=141075; _ym_d=1657999835; skid=5722487791658000552; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.7.2.899:w:d:RU:20211231; yabs-frequency=/5/2m0Z0CR2wsAe5DDY/; cycada=EAe8j3MLNd4V3whoMNWAQSfKy+ZxuPsLMvq5e/TxuI4=; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1659870280624392-7467880278375897754-sas6-5261-bf6-sas-l7-balancer-8080-BAL-457#ybzcc.ru#newsca.native_cache; i=UdhLa3rD6iH/7Ty7RH3YoNcs3nCrb4rozT35KignVTkMRqv09BM7oK777IQdLPxkfkJmVcl3qQhi4P6bcVSwvE+N/yI=; Session_id=3:1659870292.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:10256407.393485.0Fu41h6Z4lUD_klMk8ujWPJvCyc; sessionid2=3:1659870292.5.0.1640959007634:roHMsg:27.1.2:1.499:1|883187617.0.2|3:10256407.452383.k9dOKhBq4tOrWvq-2n03kWZBQSw; _ym_isad=2; _ym_visorc=b; yp=1659956613.uc.ru#1659956613.duc.ru#1681416026.cld.2261448#1681416026.brd.0699000036#1660591832.ygu.1#1973359832.skin.d#1660678244.csc.1#1659878013.gpauto.55_877659:49_746181:140:1:1659870813#1660475091.mcv.6#1660475091.mcl.1695r7s#1660475092.szm.1_125:1536x864:1707x833; _yasc=We33CXVBOPQt0+IwU87W3HsyahApucvV74uhunapa7nv6FyWJTwzL8+XYmJt0kfQxaytfkyF'
               }

    json_ = {"operationName": "CatalogContentForNormal",
             "variables": {"type": "share", "searchText": None,
                           "order": "desc", "sort": "day_trade_volume_in_rub", "filters": [], "customOrder": None,
                           "count": 99999, "cursor": "{\"id\":7971,\"dayTradeVolumeInRub\":9368735.0000000000}"},
             "query": "query CatalogContentForNormal($type: InstrumentType!, $searchText: String, $filters: [InstrumentFilter!]!, $sort: InstrumentListSort!, $order: SortOrder!, $customOrder: String, $count: Int!, $cursor: String) {\n  instruments {\n    list(types: [$type], query: $searchText, filters: $filters, sort: $sort, order: $order, customOrder: $customOrder, count: $count, cursor: $cursor) {\n      cursor\n      results {\n        id\n        type\n        slug\n        ticker\n        displayName\n        logoId\n        favorite\n        marketData {\n          id\n          accruedInterest\n          price\n          priceStep\n          lotSize\n          currencyCode\n          percentChange: yearlyPercentChange\n          absoluteChange: yearlyAbsoluteChange\n          dailyPercentChange: percentChange\n          dailyAbsoluteChange: absoluteChange\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
    r = requests.post("https://invest.yandex.ru/graphql?operation=CatalogContentForNormal", json=json_,
                      headers=headres)
    cont = json.loads(r.text)
    # pprint(cont)
    # pprint(r.text)
    name = []
    logoId = []
    yeardinamic = []
    daydinamic = []
    dang = []
    price = []
    cur = []
    lot = []
    try:
        a = cont['data']['instruments']['list']['results']
        for i in a:
            name.append(i['displayName'])
            logoId.append(i['ticker'])
            yeardinamic.append(i['marketData']['percentChange'])
            lot.append(i['marketData']['lotSize'])
            daydinamic.append(round(i['marketData']['dailyPercentChange'], 2))
            dang.append(int(i['stockRiskScoreFormatted']) if i.get('stockRiskScoreFormatted', 0) else 11)
            cur.append(i['marketData']['currencyCode'])
            price.append(i['marketData']['price'])
    except Exception as er:
        pass
        pprint(er)
    # pprint(name)
    return list(zip(name, logoId, yeardinamic, daydinamic, dang, price, cur, lot))


# pprint(len(sorted(stonks())))
# stonks()
