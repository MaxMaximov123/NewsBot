token = "5294280651:AAFQPsoq83YaVFuVchNRwBDnR4KSCUqQWRc"
token1 = "5149866452:AAGx1cymIUtKcOqWwajMOr5RNj7I5QdKlZA"
token2 = '5663602666:AAENpFtmuiFjiHLp2BB-yEg3wnqmF2ltw78'

login = "maxss.k2n@yandex.ru"
pasword = "Blanik2007"


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}

proxies = {
    "http": '112.246.105.237:8888',
    "https": '58.55.254.222:7082'
}


links = {"Овен♈️": "https://horo.mail.ru/prediction/aries/today/",
         "Телец♉️": "https://horo.mail.ru/prediction/taurus/today/",
         "Близнецы♊️": "https://horo.mail.ru/prediction/gemini/today/",
         "Рак♋️": "https://horo.mail.ru/prediction/cancer/today/",
         "Лев♌️": "https://horo.mail.ru/prediction/leo/today/",
         "Дева♍️": "https://horo.mail.ru/prediction/virgo/today/",
         "Весы♎️": "https://horo.mail.ru/prediction/libra/today/",
         "Скорпион♏️": "https://horo.mail.ru/prediction/scorpio/today/",
         "Стрелец♐️": "https://horo.mail.ru/prediction/sagittarius/today/",
         "Козерог♑️": "https://horo.mail.ru/prediction/capricorn/today/",
         "Водолей♒️": "https://horo.mail.ru/prediction/aquarius/today/",
         "Рыбы♓️": "https://horo.mail.ru/prediction/pisces/today/"}


urls = ["https://yandex.ru/news/rubric/culture",
        "https://yandex.ru/news/rubric/computers",
        "https://yandex.ru/news",
        "https://yandex.ru/news/region/kazan",
        "https://yandex.ru/news/rubric/koronavirus",
        "https://yandex.ru/news/rubric/politics",
        "https://yandex.ru/news/rubric/business",
        "https://yandex.ru/sport?utm_source=yxnews&utm_medium=desktop",
        "https://yandex.ru/news/rubric/incident"]


cookies = 'news_lang=ru; nc=search-visits-per-week=1:1645123721000#tips=1645798458637%3Bfavorites-button:1; yandexuid=1979425991640958970; yuidss=1979425991640958970; ymex=1956318975.yrts.1640958975; _ym_uid=164095897515273997; is_gdpr=0; is_gdpr_b=CIayFBDgWSgC; L=ckx/fVN5cHZzbXJyfwJCVgZoAnpwAnByWio7IAR6Hlcr.1640959007.14843.312683.efc4def33cbaaa53ad367a64d4da598e; yandex_login=maxss.k2n; gdpr=0; mda=0; font_loaded=YSv1; my=YwA=; yandex_gid=141075; _ym_d=1646636780; _ym_isad=2; Session_id=3:1648930876.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:250351.906862.f9yBA7XrLdnkaUZVJ3D9weBtfCI; sessionid2=3:1648930876.5.0.1640959007634:roHMsg:27.1.2:1|883187617.0.2|3:250351.906862.f9yBA7XrLdnkaUZVJ3D9weBtfCI; i=P4LZY/kmCKVsJpcqBDFI9VCcTVeFozSw++sP2A3eqppbiKc+AYbF4FbB/BwKkk0q9d794Pi1mldi5aD0JNIyAujqROI=; sae=0:710DC4EF-8F5B-449A-8665-0C14D23D50E8:p:22.3.0.2430:w:d:RU:20211231; yabs-frequency=/5/0G0V09DlIM87GKbY/Uwi3wsa5ArFiHI40/; ys=svt.1#def_bro.1#ead.2FECB7CF#wprid.1648986756778026-6320314446020442131-vla1-4623-vla-l7-balancer-8080-BAL-7425#ybzcc.ru#newsca.native_cache; yp=1672495029.cld.2261448#1672495029.brd.0699000036#1657951229.szm.1_25:1536x864:1536x726#1649228778.ygu.1#1649315189.csc.1#1649185034.mct.null#1649067766.nwcst.1648982400_43_3#1649538359.mcv.0#1649538359.mcl.1695r7s#1648994592.gpauto.55_796288:49_108795:100000:3:1648987392; _yasc=0fI9qmrQ9yhJAksSwGPy/B2yZivBy3AV+KOmc+dwdeaqDMPY/PIQ2D4H9LcyM/90m9UYHFAhICQOfA==; cycada=FDvjM1vMh8RHU7xa8j/ZL7aqTBF4gvSVGzF6KKxkNI0='

json = '''{"operationName":"CatalogContentForNormal","variables":{"type":"share","searchText":null,"order":"desc","sort":"day_trade_volume_in_rub","filters":[],"customOrder":null,"count":1000000,"cursor":null},"query":"query CatalogContentForNormal($type: InstrumentType!, $searchText: String, $filters: [InstrumentFilter!]!, $sort: InstrumentListSort!, $order: SortOrder!, $customOrder: String, $count: Int!, $cursor: String) {\n  instruments {\n    list(types: [$type], query: $searchText, filters: $filters, sort: $sort, order: $order, customOrder: $customOrder, count: $count, cursor: $cursor) {\n      cursor\n      results {\n        id\n        type\n        slug\n        ticker\n        displayName\n        logoId\n        taxFree\n        commissionFree\n        favorite\n        marketData {\n          id\n          accruedInterest\n          price\n          priceStep\n          lotSize\n          currencyCode\n          percentChange: yearlyPercentChange\n          absoluteChange: yearlyAbsoluteChange\n          dailyPercentChange: percentChange\n          dailyAbsoluteChange: absoluteChange\n          __typename\n        }\n        ... on ShareInstrumentItem {\n          stockRiskLevel\n          stockRiskScoreFormatted\n          __typename\n        }\n        ... on EtfInstrumentItem {\n          stockRiskLevel\n          stockRiskScoreFormatted\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}'''


urls1 = [
 '/markets/stocks-usa/market-movers-active/',
 '/markets/stocks-argentina/market-movers-active/',
 '/markets/stocks-bahrain/market-movers-active/',
 '/markets/stocks-belgium/market-movers-active/',
 '/markets/stocks-brazil/market-movers-active/',
 '/markets/stocks-united-kingdom/market-movers-active/',
 '/markets/stocks-hungary/market-movers-active/',
 '/markets/stocks-venezuela/market-movers-active/',
 '/markets/stocks-vietnam/market-movers-active/',
 '/markets/stocks-germany/market-movers-active/',
 '/markets/stocks-hong-kong/market-movers-active/',
 '/markets/stocks-greece/market-movers-active/',
 '/markets/stocks-denmark/market-movers-active/',
 '/markets/stocks-egypt/market-movers-active/',
 '/markets/stocks-israel/market-movers-active/',
 '/markets/stocks-india/market-movers-active/',
 '/markets/stocks-indonesia/market-movers-active/',
 '/markets/stocks-iceland/market-movers-active/',
 '/markets/stocks-spain/market-movers-active/',
 '/markets/stocks-italy/market-movers-active/',
 '/markets/stocks-canada/market-movers-active/',
 '/markets/stocks-qatar/market-movers-active/',
 '/markets/stocks-china/market-movers-active/',
 '/markets/stocks-colombia/market-movers-active/',
 '/markets/stocks-latvia/market-movers-active/',
 '/markets/stocks-lithuania/market-movers-active/',
 '/markets/stocks-luxembourg/market-movers-active/',
 '/markets/stocks-malaysia/market-movers-active/',
 '/markets/stocks-mexico/market-movers-active/',
 '/markets/stocks-nigeria/market-movers-active/',
 '/markets/stocks-netherlands/market-movers-active/',
 '/markets/stocks-new-zealand/market-movers-active/',
 '/markets/stocks-norway/market-movers-active/',
 '/markets/stocks-uae/market-movers-active/',
 '/markets/stocks-peru/market-movers-active/',
 '/markets/stocks-poland/market-movers-active/',
 '/markets/stocks-portugal/market-movers-active/',
 '/markets/stocks-russia/market-movers-active/',
 '/markets/stocks-romania/market-movers-active/',
 '/markets/stocks-ksa/market-movers-active/',
 '/markets/stocks-serbia/market-movers-active/',
 '/markets/stocks-singapore/market-movers-active/',
 '/markets/stocks-slovakia/market-movers-active/',
 '/markets/stocks-thailand/market-movers-active/',
 '/markets/stocks-taiwan/market-movers-active/',
 '/markets/stocks-turkey/market-movers-active/',
 '/markets/stocks-philippines/market-movers-active/',
 '/markets/stocks-finland/market-movers-active/',
 '/markets/stocks-france/market-movers-active/',
 '/markets/stocks-chile/market-movers-active/',
 '/markets/stocks-switzerland/market-movers-active/',
 '/markets/stocks-sweden/market-movers-active/',
 '/markets/stocks-estonia/market-movers-active/',
 '/markets/stocks-south-africa/market-movers-active/',
 '/markets/stocks-korea/market-movers-active/',
 '/markets/stocks-japan/market-movers-active/'
         ]
