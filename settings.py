"""SETTINGS OF APPLICATION"""

# settings database
DB_PATH = 'postgresql+psycopg2://postgres:postgres@localhost/kijiji'

# settings parsing URL
URL_TO_PAGE = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/'
URL_PAST_PAGE = 'c37l1700273/'
URL_WITHOUT_PAGE = URL_TO_PAGE + URL_PAST_PAGE

RESULT_CSV = 'result.csv'
