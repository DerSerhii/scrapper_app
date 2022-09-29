# SCRAPING APP

This is a test application that collects the necessary data from the pages of the website [www.kijiji.ca](https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273?ad=offering), including pagination.

---

## Getting started

Download the code base on your local machine. You may prefer to use virtual environment to separate the project's dependencies from other packages you have installed.

To install dependencies use `pip`:
```
pip install -r requirements.txt
```
To run the app do
```
python main.py
```

## Database

An installed **PostgreSQL** is required for operation.

Settings file: `settings.py`

Database can be created by running the file: `db_create.py` in packadge `utils` <br>
Teable can be created by running the file: `models.py`
