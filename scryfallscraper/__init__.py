"""
Do you really like Scryfall API? Yeah, same.

bulk_scraping: Scrape from Scryfall's large bulk data.
sets: Scrape set metadata.
"""

# from importlib.metadata import version

# try:
#     __version__ = version("scryfallscraper")
# except:
#     __version__ = "UNKNOWN"


import traceback

try:
    from scryfallscraper.bulk_scraping import functions as bulk_scraping
    from scryfallscraper.compression import functions as compression
    from scryfallscraper.sets import functions as scrape_sets
except Exception:
    traceback.print_exc()
