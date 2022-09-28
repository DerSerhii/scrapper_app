"""APPLICATION LAUNCH FILE"""
import random
from time import sleep

import controller
import settings


def main() -> None:
    max_page = controller.get_max_pagination(settings.URL_WITHOUT_PAGE)
    result = []

    for number in range(1, max_page + 1):
        print(f'Parsing page #{number} of {max_page}', end=('.'*5))
        page_url = f'{settings.URL_TO_PAGE}page-{number}/{settings.URL_PAST_PAGE}'
        result += controller.get_page_data(page_url)
        sleep(random.randrange(10, 30))

    controller.write_csv(result)
    controller.write_db(result)


if __name__ == '__main__':
    main()
