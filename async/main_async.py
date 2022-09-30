"""ASYNC APPLICATION LAUNCH FILE"""

import time
import aiohttp
import asyncio

import controller_async as controller
import settings

# script start time
start_time = time.time()


async def gather_data(max_page: int) -> list:
    """Returns the gathered data from all pages of the site."""

    async with aiohttp.ClientSession() as session:
        tasks = []

        for number in range(1, max_page + 1):
            page_url = f'{settings.URL_TO_PAGE}page-{number}/{settings.URL_PAST_PAGE}'
            task = asyncio.create_task(
                controller.get_page_data(page_url, session, number, max_page))
            tasks.append(task)

        data = await asyncio.gather(*tasks)

    return data


def main() -> None:
    # maximum page on the site
    max_page = controller.get_max_pagination(settings.URL_WITHOUT_PAGE)

    gather = asyncio.run(gather_data(max_page))

    result = []
    for res in gather:
        result += res

    controller.write_csv(result)
    controller.write_db(result)

    finish_time = time.time() - start_time
    print(f'Script running time: {finish_time}')


if __name__ == '__main__':
    main()
