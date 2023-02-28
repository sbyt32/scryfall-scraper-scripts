import json
import os
from typing import Union, Optional
from scryfallscraper import scraper


def scrape_all_sets(zipped: Optional[bool] = False):
    r"""Scrape set data: https://scryfall.com/docs/api/sets/all

    :param zipped: Return either as an dict or make a gzip in the current directory (False, Default).
    """

    with scraper.Scraper(
        url=f"https://api.scryfall.com/sets/",
        scrape_type="sets",
        zipped=zipped,
    ) as set_scrape:
        return set_scrape.scrape_data()


def scrape_by_code(set: str, zipped: Optional[bool] = False):
    r"""Scrape set data by code: https://scryfall.com/docs/api/sets/code


    :param zipped: Return either as an dict or make a gzip in the current directory (False, Default).
    """
    set_len = len(set)
    if set_len > 5 or set_len < 3:
        raise ValueError("Set Name is Too Short!")

    with scraper.Scraper(
        url=f"https://api.scryfall.com/sets/{set}",
        scrape_type="sets",
        zipped=zipped,
    ) as set_scrape:
        return set_scrape.scrape_data()


def scrape_by_tcgplayer_id(tcgplayer_id: str, zipped: Optional[bool] = False):
    r"""Scrape set data by TCGPlayer ID: https://scryfall.com/docs/api/sets/tcgplayer


    :param zipped: Return either as an dict or make a gzip in the current directory (False, Default).
    """

    with scraper.Scraper(
        url=f"https://api.scryfall.com/sets/tcgplayer/{tcgplayer_id}",
        scrape_type="sets",
        zipped=zipped,
    ) as set_scrape:
        return set_scrape.scrape_data()


def scrape_by_scryfall_id(scryfall_id: str, zipped: Optional[bool] = False):
    r"""Scrape set data by TCGPlayer ID: https://scryfall.com/docs/api/sets/tcgplayer


    :param zipped: Return either as an dict or make a gzip in the current directory (False, Default).
    """
    scry_length = len(scryfall_id)
    if scry_length < 10:
        # ? So I don't know if there is a standardized format for it.
        raise ValueError("Set Name is Too Short!")

    with scraper.Scraper(
        url=f"https://api.scryfall.com/sets/{scryfall_id}",
        scrape_type="sets",
        zipped=zipped,
    ) as set_scrape:
        return set_scrape.scrape_data()
