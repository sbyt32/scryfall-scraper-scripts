from typing import Optional
from scryfallscraper.bulk_scraping.util import BulkScraper

"""
Wanna scrape the Scryfall bulk section? Here it is!
"""


def scrape_oracle_cards(zipped: Optional[bool] = False) -> Optional[dict]:
    r"""Scrape one Scryfall card object for each Oracle ID | ~(100MB).
    https://scryfall.com/docs/api/bulk-data

    :param zipped: Return either as an dict or make a gzip in the current directory (False, Default).
    """
    with BulkScraper() as scraper:
        return scraper.scrape_data("oracle_cards", zipped=zipped)


def scrape_unique_artwork(zipped: Optional[bool] = False) -> Optional[dict]:
    r"""Scrape one Scryfall card object for unique card arts! | ~(140MB).
    https://scryfall.com/docs/api/bulk-data

    :param zipped: Return either as an dict or make a gzip in the current directory (False, Default).
    """

    with BulkScraper() as scraper:
        return scraper.scrape_data("unique_artwork", zipped=zipped)


def scrape_default_cards(zipped: Optional[bool] = False) -> Optional[dict]:
    r"""Scrape every single card object, returns English or the only printed language. | ~(300MB).
    https://scryfall.com/docs/api/bulk-data

    :param zipped: Return either as an dict or make a gzip in the current directory (False, Default).
    """
    with BulkScraper() as scraper:
        return scraper.scrape_data("default_cards", zipped=zipped)


def scrape_all_cards(zipped: Optional[bool] = False) -> Optional[dict]:
    r"""Scrape one Scryfall card object for each card, in each language (when possible) | ~(1.50GB).
    https://scryfall.com/docs/api/bulk-data

    :param zipped: Return either as an dict or make a gzip in the current directory (False, Default).
    """
    with BulkScraper() as scraper:
        return scraper.scrape_data("all_cards", zipped=zipped)


def scrape_rulings(zipped: Optional[bool] = False) -> Optional[dict]:
    r"""A JSON file containing all Rulings on Scryfall. Each ruling refers to cards via an `oracle_id`. | ~(15MB).
    https://scryfall.com/docs/api/bulk-data

    :param zipped: Return either as an dict or make a gzip in the current directory (False, Default).
    """
    with BulkScraper() as scraper:
        return scraper.scrape_data("rulings", zipped=zipped)
