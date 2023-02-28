import json
import os
import datetime
import traceback
from typing import Union, Optional
from scryfallscraper.util import util


class BulkScraper:
    r"""

    :param zipped: Return either zipped up or as an object
    :param scrape_type: What sort of scrape is it? Used for files
    :param url: The URL

    """

    def __init__(self) -> None:
        self.bulk_data_links = util.send_request("https://api.scryfall.com/bulk-data")[
            "data"
        ]

    def write_json_data(self, data: Union[dict, list], path: str) -> None:
        with open(path, "w") as bulk_data_fp:
            json.dump(data, bulk_data_fp)

    def check_dir_exist(self, bulk_type: str) -> None:
        if not os.path.exists(f"data/{bulk_type}"):
            os.makedirs(f"data/{bulk_type}")

    def scrape_data(self, bulk_type: str, zipped: bool = True) -> Optional[dict]:
        r"""Scrape the data

        :param zipped: Return either as an dict or write to the current directory.
        """

        for bulk_data_info in self.bulk_data_links:
            if bulk_data_info["type"] == bulk_type:
                file_name: str = f"{util.parse_time(bulk_data_info['updated_at'])}"
                path = f"{bulk_type}/{file_name}"
                scraped_data = util.send_request(bulk_data_info["download_uri"])

                self.check_dir_exist(bulk_type)
                if zipped:
                    util.compress_obj(scraped_data, path)
                else:
                    return scraped_data
                break

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        pass
