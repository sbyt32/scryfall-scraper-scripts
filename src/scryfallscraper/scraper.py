import json
import os
import datetime
from typing import Union, Optional
from scryfallscraper import util


class Scraper:
    r"""
    :param zipped: Return either zipped up or as an object
    :param scrape_type: What sort of scrape is it? Used for files
    :param url: The URL

    """

    def __init__(
        self,
        scrape_type: str,
        url: str,
        zipped: bool = False,
    ) -> None:
        self.zipped = zipped
        self.scrape_type = scrape_type
        self.url = url

    def get_bulk_data_link(self) -> dict:
        if w := util.send_request(self.url):
            return w

    def write_json_data(self, data: Union[dict, list], path: str) -> None:
        with open(path, "w") as bulk_data_fp:
            json.dump(data, bulk_data_fp)

    def check_dir_exist(self) -> None:
        path: str = f"data/{self.scrape_type}"
        if not os.path.exists(path):
            os.makedirs(path)

    def scrape_data(self) -> Optional[dict]:
        r"""
        All-Purpose Scraper!
        """
        data = self.get_bulk_data_link()
        if self.zipped:
            file_name = f"{self.scrape_type}/{util.parse_time(str(datetime.datetime.now(datetime.timezone.utc)))}"
            self.check_dir_exist()
            util.compress_obj(data, file_name)
        else:
            return data

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        pass
