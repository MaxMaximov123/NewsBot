import requests
import json
from bs4 import BeautifulSoup as BS
from pprint import pprint


def stonks():
    head = {
        'Cookie': 'yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; is_gdpr=0; is_gdpr_b=CIayFBDgWSgC; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; my=YwA=; mda=0; yandex_gid=141075; _ym_d=1657999835; skid=5722487791658000552; cycada=pn7dPAA87YcIEQNMa/t7HWV3w12CTyq6a42PNbX6EBw=; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.7.1.806:w:d:RU:20211231; i=ZeXOPwF9mBUbSJR1TPJwa8NmPfHZRN45ur0vVxW93ToMjp/S3B6T0AUMkuP1yHpeIP5jQ3zMr0N6NZUgmui7H0yFaNs=; yabs-frequency=/5/0m0Z0AfEr6Ae5DDY/sLLbIOQoDsUiHoTAvh6atJgbHe17BW00/; Session_id=3:1659078720.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:10255969.288888.lM51MS7c_nLObuCYLdwg9r3YP-Y; sessionid2=3:1659078720.5.0.1640959007634:roHMsg:27.1.2:1.499:1|883187617.0.2|3:10255969.575573.1u8pun8XAl3XWNQFX_AWteXfLXI; _ym_isad=2; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1659079140739048-2886573687781822595-sas2-0820-842-sas-l7-balancer-8080-BAL-5861#ybzcc.ru#newsca.native_cache; _yasc=ljczxdeOIl2aaB2ZeR2gBYzaKYMTqN4dp1ZD6SjCZQxbF7laY4J/qLFxqdBw9dETyn/prg==; _ym_visorc=w; yp=1659165090.uc.ru#1659165090.duc.ru#1681416026.cld.2261448#1681416026.brd.0699000036#1660591832.ygu.1#1973359832.skin.d#1660678244.csc.1#1659090090.gpauto.55_877647:49_746201:140:1:1659082890#1659186218.mcv.6#1659186218.mcl.1695r7s#1659186218.szm.1_125:1536x864:1707x833'}
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
    # print(a)
    headres = {'content-type': 'application/json',
               'X-Retpath-Y': 'https://invest.yandex.ru/catalog/stock/',
               'x-ssr-id': '5c44dab40aac0dcbedc24a60ef434676',
               'x-tanker-branch': 'master',
               'x-visible-uid': '883187617',
               'x-csrf-token': a,
               'Cookie': 'yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; is_gdpr=0; is_gdpr_b=CIayFBDgWSgC; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; my=YwA=; i=E7SiZgCsSKojDRLVvd3cs5NToPJf70ZTx3FV19zWCvTHOSi+nWVfNy7se9HgVW/AdgqJfj7xGLRCH5PrQwBRYLBzhcc=; _ym_isad=2; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.7.0.1842:w:d:RU:20211231; Session_id=3:1657999417.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:10255369.321744.Wc-b1inzek5fXwsN7CAdngILE3U; sessionid2=3:1657999417.5.0.1640959007634:roHMsg:27.1.2:1.499:1|883187617.0.2|3:10255369.841549.Vw_TD7OaXL41e8yeK01e_YcwJcY; mda=0; yandex_gid=141075; _ym_d=1657999835; skid=5722487791658000552; cycada=NzffFr465tsdSH6K03iTH2V3w12CTyq6a42PNbX6EBw=; ys=svt.1#def_bro.1#ead.2FECB7CF#mclid.2261452#wprid.1658000956376067-16001281650361153706-sas3-0671-f04-sas-l7-balancer-8080-BAL-9333#ybzcc.ru#newsca.native_cache; yabs-frequency=/5/0G0Z03qMqsAe5DDY/LVTwO9j8VbACHo7uuLJahjcVGen78IBjJmGCfCPkZ4SZsLLbIOQoDsUCHoTAvh6atJgbHe17BW00/; _ym_visorc=w; yp=1658085614.uc.ru#1658085614.duc.ru#1681416026.cld.2261448#1681416026.brd.0699000036#1658332819.mcv.6#1658332819.mcl.1695r7s#1658573603.szm.1_125:1536x864:1692x804#1658008814.gpauto.55_877647:49_746201:140:1:1658001614#1658259035.clh.2261452#1660591832.ygu.1#1658001632.rnwcst.1#1973359832.skin.d#1660678244.csc.1; _yasc=zwGV01S7U7P/DMY3yevgipytsxjqfIBOObRocMThwUXa2qFsBsWucvJC5PLYwvXMtRBYJA=='}

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


# pprint(sorted(stonks()))
# stonks()
