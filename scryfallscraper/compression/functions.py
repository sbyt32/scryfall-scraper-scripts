import gzip
import shutil
import os
import glob
from typing import Optional


def compress_dir(zip_path: Optional[str] = "", f_path: Optional[str] = "") -> None:
    """
    Compress a whole directory! I hope it works!

    f_path: Location of the .json files to compress. Default current directory.
    zip_path: Location of the .gz file. Default current directory.
    """
    if not f_path:
        f_path = ""

    files: list = [os.path.basename(files) for files in glob.glob(f"{f_path}*.json")]
    if not os.path.exists(zip_path):
        zip_path = "./"

    for file in files:
        file_path = f"{zip_path}{file}.gz"
        if not os.path.exists(file_path):
            with gzip.open(file_path, "wb") as compressed_fp:
                shutil.copyfileobj(open(f"{f_path}{file}", "rb"), compressed_fp)
