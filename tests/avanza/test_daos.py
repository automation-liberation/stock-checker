import json
import unittest

from stockchecker.avanza.daos import AvanzaFondDAO, AvanzaStockDAO


class AvanzaFondDAOTest(unittest.TestCase):
    fond_response = """{
    "riskLevel": "MIDDLE",
    "hasInvestmentFees": true,
    "name": "Swedbank Robur Ny Teknik A",
    "id": "1933",
    "description": "Fonden placerar huvudsakligen i aktier i svenska och nordiska mindre och medelstora bolag. Placeringarna koncentreras till bolag vars produkter och/eller tjänster har ett högt teknikinnehåll. Exempel på branscher där fonden placerar är IT/telekommunikation, läkemedel/medicinsk teknik, miljöteknik och industriteknik. Fonden kan placera upp till 30 procent av fondförmögenheten på marknader utanför Norden. Fonden får använda sig av derivatinstrument i strävan att öka fondens avkastning. Fonden har en långsiktig placeringshorisont och en aktiv investeringsstrategi som fokuserar på bolagsval inom ovan nämnda placeringsinriktning. Fonden följer även fondbolagets policy för ansvarsfulla investeringar, läs mer om policyn i fondens informationsbroschyr. Fonden lämnar normalt ingen utdelning, utan vinster återinvesteras i fonden.",
    "isin": "SE0000709123",
    "sellable": true,
    "risk": 5,
    "sharpeRatio": 1.7,
    "domicile": "Sverige",
    "administrators": "Ingemar Syhrén, Johan Söderström ",
    "standardDeviation": 16.59,
    "tradingCurrency": "SEK",
    "managementFee": 1.25,
    "prospectus": "http://doc.morningstar.com/document/622e04ec2483d21b317006214d459da3.msdoc/?clientid=avanza&key=3728b8f503435715",
    "buyFee": 0,
    "capital": 15470760000,
    "normanAmount": 0,
    "rating": 3,
    "sellFee": 0,
    "startDate": "1996-11-11",
    "loanFactor": 70,
    "buyable": true,
    "NAVLastUpdated": "2019-05-24T00:00:00.000+0200",
    "NAV": 861.71,
    "changeSinceOneDay": 0.17,
    "changeSinceOneWeek": -0.67,
    "changeSinceOneMonth": -1.94,
    "changeSinceThreeMonths": 5.99,
    "changeSinceSixMonths": 15.82,
    "changeSinceTurnOfTheYear": 20.08,
    "changeSinceOneYear": 2.44,
    "changeSinceThreeYears": 103.53,
    "changeSinceFiveYears": 250.26,
    "changeSinceTenYears": 696.7,
    "relatedFunds": [
        {
            "name": "Öhman Global Growth",
            "id": "372",
            "changeSinceOneYear": 10.72
        },
        {
            "name": "BGF World Technology A2",
            "id": "431",
            "changeSinceOneYear": 19.2
        },
        {
            "name": "GAM Star Technology A USD Acc",
            "id": "644315",
            "changeSinceOneYear": 11.21
        },
        {
            "name": "Fidelity Global Technology A-Dis-EUR",
            "id": "379",
            "changeSinceOneYear": 15.89
        },
        {
            "name": "MS INVF Asia Opportunity A",
            "id": "691674",
            "changeSinceOneYear": 1.35
        }
    ],
    "fundCompany": {
        "name": "Swedbank Robur"
    },
    "numberOfOwners": 73295,
    "autoPortfolio": false,
    "type": "Branschfond",
    "otherFees": "",
    "subCategory": "Branschfond, ny teknik"
}"""

    def test_create(self):
        dao = AvanzaFondDAO.from_dict(json.loads(self.fond_response))
        self.assertEqual(dao.id, "1933")
        self.assertEqual(dao.name, "Swedbank Robur Ny Teknik A")
        self.assertEqual(dao.NAV, 861.71)


class AvanzaStockDAOTest(unittest.TestCase):
    stock_response = """{
    "priceOneWeekAgo": 29.25,
    "priceOneMonthAgo": 27.41,
    "priceSixMonthsAgo": 18.46,
    "priceAtStartOfYear": 18.46,
    "priceOneYearAgo": 14.98,
    "priceThreeYearsAgo": 5.07,
    "priceFiveYearsAgo": 4.22,
    "priceThreeMonthsAgo": 26.36,
    "marketPlace": "NASDAQ",
    "currency": "USD",
    "buyPrice": 31.12,
    "sellPrice": 31.13,
    "highestPrice": 32.04,
    "lowestPrice": 31.07,
    "change": 0.76,
    "changePercent": 2.5,
    "totalVolumeTraded": 47225235,
    "totalValueTraded": 0,
    "lastPrice": 31.13,
    "lastPriceUpdated": "2019-07-01T19:53:00.838+0200",
    "shortSellable": false,
    "isin": "US0079031078",
    "tradable": true,
    "tickerSymbol": "AMD",
    "loanFactor": 60,
    "flagCode": "US",
    "quoteUpdated": "2019-07-01T19:53:09.515+0200",
    "hasInvestmentFees": false,
    "name": "Advanced Micro Devices Inc",
    "id": "529720",
    "country": "USA",
    "keyRatios": {
        "priceEarningsRatio": 97.47,
        "directYield": 0
    },
    "numberOfOwners": 3589,
    "superLoan": false,
    "pushPermitted": false,
    "dividends": [],
    "relatedStocks": [
        {
            "lastPrice": 45.37,
            "priceOneYearAgo": 46.19,
            "flagCode": "US",
            "name": "Applied Materials Inc",
            "id": "3575"
        },
        {
            "lastPrice": 297.55,
            "priceOneYearAgo": 242.74,
            "flagCode": "US",
            "name": "Broadcom Inc",
            "id": "369636"
        },
        {
            "lastPrice": 188.3,
            "priceOneYearAgo": 134.4,
            "flagCode": "US",
            "name": "Red Hat Inc",
            "id": "63187"
        },
        {
            "lastPrice": 40.08,
            "priceOneYearAgo": 52.45,
            "flagCode": "US",
            "name": "Micron Technology Inc",
            "id": "214533"
        },
        {
            "lastPrice": 47.98,
            "priceOneYearAgo": 49.73,
            "flagCode": "US",
            "name": "Intel Corp",
            "id": "3658"
        }
    ],
    "company": {
        "sector": "Teknik",
        "stocks": [
            {
                "totalNumberOfShares": 1081600723,
                "name": "Advanced Micro Devices Inc"
            }
        ],
        "chairman": "John E. Caldwell",
        "totalNumberOfShares": 1081600723,
        "description": "Advanced Micro Devices, förkortat AMD, är ett amerikanskt bolag inriktade mot utveckling av industriella halvledare. Produkterna används inom olika affärs- och konsumentmarknader, där bolaget utvecklar diverse mikroproccessorer för datorer och övriga hårdvaror. Verksamhet innehas på global nivå, med huvudkontor i Sunnyvale.",
        "marketCapital": 32848213957,
        "marketCapitalCurrency": "USD",
        "name": "Advanced Micro Devices",
        "id": "100799",
        "CEO": "Lisa Su"
    },
    "orderDepthLevels": [
        {
            "sell": {
                "percent": 100,
                "price": 31.13,
                "volume": 5740
            },
            "buy": {
                "percent": 19.390243902439025,
                "price": 31.12,
                "volume": 1113
            }
        }
    ],
    "marketMakerExpected": false,
    "orderDepthReceivedTime": "2019-07-01T19:53:09.515+0200",
    "latestTrades": [],
    "marketTrades": false,
    "annualMeetings": [],
    "companyReports": [
        {
            "reportType": "INTERIM",
            "eventDate": "2019-04-30"
        }
    ],
    "brokerTradeSummary": {
        "orderbookId": "529720",
        "items": [
            {
                "buyVolume": 43317121,
                "sellVolume": 43317121,
                "brokerCode": "Anonyma",
                "netBuyVolume": 0
            }
        ]
    }
}"""

    def test_create(self):
        dao = AvanzaStockDAO.from_dict(json.loads(self.stock_response))
        self.assertEqual(dao.id, "529720")
        self.assertEqual(dao.name, "Advanced Micro Devices Inc")
        self.assertEqual(dao.sellPrice, 31.13)
