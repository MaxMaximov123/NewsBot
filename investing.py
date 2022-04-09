import requests
import json
from pprint import pprint


def stonks():
    headres = {'content-type': 'application/json',
               'X-Retpath-Y': 'https://invest.yandex.ru/catalog/stock/',
               'x-ssr-id': '24ee17def6b261f1169bb6c734051197',
               'x-tanker-branch': 'master',
               'x-visible-uid': '883187617',
               'x-csrf-token': '148867be48da75d771a6d25aa08b179b123d57bc:1649526412',
               'Cookie': 'yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; is_gdpr=0; is_gdpr_b=CIayFBDgWSgC; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; mda=0; my=YwA=; yandex_gid=141075; _ym_d=1646636780; _ym_isad=2; Session_id=3:1648930876.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:250351.906862.f9yBA7XrLdnkaUZVJ3D9weBtfCI; sessionid2=3:1648930876.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:250351.906862.f9yBA7XrLdnkaUZVJ3D9weBtfCI; i=P4LZY/kmCKVsJpcqBDFI9VCcTVeFozSw++sP2A3eqppbiKc+AYbF4FbB/BwKkk0q9d794Pi1mldi5aD0JNIyAujqROI=; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.3.0.2430:w:d:RU:20211231; cycada=cK2JuQ9Cuu+LQ/HCCnHYPraqTBF4gvSVGzF6KKxkNI0=; stockChart.seriesType=area; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1648981370001784-11595579900118636286-vla1-4623-vla-l7-balancer-8080-BAL-6197#ybzcc.ru#newsca.native_cache; _yasc=3GfAuIorLww5mq/2zBsFANDwHlM+014IW0C0YSLiIX0quez32Ns+J5FisacwljxUvPVZIuGB77l6pA==; yabs-frequency=/5/0G0V09DlIM87GKbY/Uwi3wsa5ArFiHI40/; yp=1672495029.cld.2261448#1672495029.brd.0699000036#1657951229.szm.1_25:1536x864:1536x726#1649228778.ygu.1#1649315189.csc.1#1649185034.mct.null#1649067766.nwcst.1648982400_43_3#1649538359.mcv.0#1649538359.mcl.1695r7s#1648991592.gpauto.55_796288:49_108795:100000:3:1648984392'
               }

    json_ = {"operationName": "CatalogContentForNormal",
             "variables": {"type": "share", "searchText": None, "order": "desc", "sort": "day_trade_volume_in_rub",
                           "filters": [], "customOrder": None, "count": 1000000, "cursor": None},
             "query": "query CatalogContentForNormal($type: InstrumentType!, $searchText: String, $filters: [InstrumentFilter!]!, $sort: InstrumentListSort!, $order: SortOrder!, $customOrder: String, $count: Int!, $cursor: String) {\n  instruments {\n    list(types: [$type], query: $searchText, filters: $filters, sort: $sort, order: $order, customOrder: $customOrder, count: $count, cursor: $cursor) {\n      cursor\n      results {\n        id\n        type\n        slug\n        ticker\n        displayName\n        logoId\n        taxFree\n        commissionFree\n        favorite\n        marketData {\n          id\n          accruedInterest\n          price\n          priceStep\n          lotSize\n          currencyCode\n          percentChange: yearlyPercentChange\n          absoluteChange: yearlyAbsoluteChange\n          dailyPercentChange: percentChange\n          dailyAbsoluteChange: absoluteChange\n          __typename\n        }\n        ... on ShareInstrumentItem {\n          stockRiskLevel\n          stockRiskScoreFormatted\n          __typename\n        }\n        ... on EtfInstrumentItem {\n          stockRiskLevel\n          stockRiskScoreFormatted\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}

    r = requests.post("https://invest.yandex.ru/graphql?operation=CatalogContentForNormal", json=json_,
                      headers=headres)
    cont = json.loads(r.text)
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
            dang.append(int(i['stockRiskScoreFormatted']) if i['stockRiskScoreFormatted'] else 11)
            cur.append(i['marketData']['currencyCode'])
            price.append(i['marketData']['price'])
    except Exception:
        pass
        # print('-----------')
    # pprint(name)
    return list(zip(name, logoId, yeardinamic, daydinamic, dang, price, cur, lot))