import logging
import requests

from stockchecker import celery
from stockchecker.avanza.daos import AvanzaFondDAO


logger = logging.getLogger()


@celery.task
def get_avanza_fond_value(fond_id):
    url = f'https://www.avanza.se/_mobile/market/fund/{fond_id}'
    response = requests.get(url)
    dao = AvanzaFondDAO.from_dict(response.json())
    logger.info(f"Checking {dao.name}")

    return dao.as_dict
