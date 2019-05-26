import json
import unittest

from stockchecker.avanza.daos import AvanzaFondDAO


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
