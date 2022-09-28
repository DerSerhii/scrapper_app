"""SETTINGS OF APPLICATION"""

# settings database
DB_PATH = 'postgresql+psycopg2://postgres:postgres@localhost/kijiji'

# settings parsing URL
URL_TO_PAGE = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/'
URL_PAST_PAGE = 'c37l1700273/'
URL_WITHOUT_PAGE = URL_TO_PAGE + URL_PAST_PAGE

# file for CSV-data recording
RESULT_CSV = 'result.csv'

# settings Request Headers
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
              'image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
