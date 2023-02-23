import json
import os
from typing import Union, Optional
from scryfall_scraper_scripts import util

"""
Wanna scrape the Scryfall bulk section? Here it is!
"""


def _get_bulk_data_link():
    return util.send_request("https://api.scryfall.com/bulk-data")["data"]


def _write_json_data(data: Union[dict, list], path: str) -> None:
    with open(path, "w") as bulk_data_fp:
        json.dump(data, bulk_data_fp)


def _check_dir_exist(bulk_type: str) -> None:
    if not os.path.exists(bulk_type):
        os.makedirs(bulk_type)


def _scrape_data(bulk_type: str) -> None:
    bulk_data_link = _get_bulk_data_link()
    for bulk_data_info in bulk_data_link:
        if bulk_data_info["type"] == bulk_type:
            file_name: str = f"{util.parse_time(bulk_data_info['updated_at'])}.json"
            path = f"{bulk_type}/{file_name}"
            scraped_data = util.send_request(bulk_data_info["download_uri"])

            _check_dir_exist(bulk_type)
            _write_json_data(scraped_data, path)

            break


def scrape_oracle_cards() -> None:
    _scrape_data("oracle_cards")


def scrape_unique_artwork() -> None:
    _scrape_data("unique_artwork")


def scrape_default_cards() -> None:
    _scrape_data("default_cards")


def scrape_all_cards() -> None:
    _scrape_data("all_cards")


def scrape_rulings() -> None:
    _scrape_data("rulings")
