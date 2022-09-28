""" APPLICATION LOGIC """

import csv
import math
import re
import requests
import datetime as dt

from bs4 import BeautifulSoup
from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from models import Rent
from settings import DB_PATH


def clean(text: str) -> str:
    """Return cleaned data."""
    return text.replace('\t', '').replace('\n', '').strip()


def write_csv(result) -> None:
    """Writing parsing data to a file CSV"""

    with open(settings.RESULT_CSV, 'w') as file:
        writer = csv.writer(file)
        for item in result:
            writer.writerow(
                (item['title'],
                 item['image'],
                 item['date'],
                 item['city'],
                 item['beds'],
                 item['description'],
                 item['price'],
                 item['currency'],
                 )
            )


def write_db(result) -> None:
    """Writing parsing data to a database"""

    engine = create_engine(DB_PATH, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.bulk_insert_mappings(Rent, result)
    session.commit()


def serializer_date(date: str) -> str:
    """Return the date in the format str(dd-mm-yyyy)."""
    # such requirements, I would have translated to 'datatime.datatime'

    regex = r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[" \
            r"2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(" \
            r"?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(" \
            r"?:1[6-9]|[2-9]\d)?\d{2})$"

    date_now = dt.datetime.now().strftime("%d-%m-%Y")

    return date.replace('/', '-') if re.match(regex, date) else date_now


def serializer_price(price: str) -> tuple:
    """Return tuple where the first element is the price (float or None)
       and the second element is the currency value
       (if there is a price else input text).
    """
    price_number = re.findall(r"-?\d+\.?\d*", price.replace(',', ''))

    return (float(price_number[0]), price[0]) if price_number else (None, price)


def get_max_pagination(page_url: str) -> int:
    """Return maximum pagination."""

    request = requests.get(page_url)
    soup = BeautifulSoup(request.content, 'lxml')

    pagination_str = soup.find('span',
                               attrs={'class': 'resultsShowingCount-1707762110'}).text
    pagination = [int(s) for s in re.findall(r"-?\d+\.?\d*", pagination_str)]

    return math.ceil(pagination[2]/pagination[1])


def get_page_data(page_url: str) -> list[dict[str, Any]]:
    """Return a list of data dictionaries for the given page."""

    request = requests.get(page_url, headers=settings.HEADERS)
    print(f'Request: {request.status_code}')
    soup = BeautifulSoup(request.content, 'lxml')

    table = soup.find('main')
    rows = table.find_all('div', attrs={'class': 'search-item'})
    result = []

    for row in rows:
        title = clean(row.find('div', attrs={'class': 'title'}).text)
        image = row.find('div', attrs={'class': 'image'}).find('img').get('data-src')
        city = clean(row.find('div', attrs={'class': 'location'}).find('span').text)
        date = clean(row.find('div', attrs={'class': 'location'})
                     .find(attrs={'class': 'date-posted'}).text
                     )
        beds = clean(row.find('div', attrs={'class': 'rental-info'})
                     .find(attrs={'class': 'bedrooms'}).text
                     )
        description = clean(row.find('div', attrs={'class': 'description'}).text)
        price = clean(row.find('div', attrs={'class': 'price'}).text)

        item = {
            'title': title,
            'image': image,
            'city': city,
            'date': serializer_date(date),
            'beds': beds,
            'description': description,
            'price': serializer_price(price)[0],
            'currency': serializer_price(price)[1],
        }
        result.append(item)

    return result
