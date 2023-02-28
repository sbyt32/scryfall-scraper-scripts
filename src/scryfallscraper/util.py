import re
import requests
import shutil
import gzip
import json
from typing import Union, Optional


def send_request(url: str) -> Union[list, dict]:
    """
    Get some data from Scryfall.
    """
    resp = requests.get(url)
    if not resp.status_code == 200:
        raise ConnectionError(resp.text)
    return resp.json()


def parse_time(time: str) -> Optional[str]:
    """
    Make the last updated time return either a filename friendly string, or None.
    """
    # Match the time.
    regex_pattern = re.compile(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}.*[0-9]{2}:[0-9]{2}:[0-9]{2}", re.IGNORECASE
    )
    fetch_time = regex_pattern.search(time)
    if fetch_time:
        fn_replacers: list[tuple[str, str]] = [("T", "_"), (":", ""), (" ", "_")]
        file_name = fetch_time.group()
        for rm, new in fn_replacers:
            file_name = file_name.replace(rm, new)
        return file_name
    return None


def compress_obj(data: dict, path: str):
    path = f"{path}.gz"
    data_bytes = json.dumps(data).encode("utf-8")
    with gzip.open(f"data/{path}", "wb") as compressed_fp:
        compressed_fp.write(data_bytes)
