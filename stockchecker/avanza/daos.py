from dataclasses import dataclass

from stockchecker.utils.daos import BaseDao


@dataclass
class AvanzaFondDAO(BaseDao):
    """
    The Dao for interesting information about a fund from Fond Marknaden.

    """
    id: int
    name: str
    description: str
    NAV: str
    changeSinceOneMonth: str
    changeSinceThreeMonths: str
    prospectus: str
    tradingCurrency: str


@dataclass
class AvanzaStockDAO(BaseDao):
    """
    The Dao for interesting information about a fund from Fond Marknaden.

    """
    id: int
    name: str
    description: str
    sellPrice: str
    country: str
    marketPlace: str
    currency: str
    priceOneMonthAgo: str
    priceThreeMonthsAgo: str
    relatedStocks: dict
