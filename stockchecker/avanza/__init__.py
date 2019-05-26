import requests

from stockchecker import celery
from stockchecker.avanza.daos import AvanzaFondDAO


@celery.task
def get_avanza_fond_value(fond_id):
    url = f'https://www.avanza.se/_mobile/market/fund/{fond_id}'
    response = requests.get(url)
    dao = AvanzaFondDAO.from_dict(response.json())

    return dao.as_dict
