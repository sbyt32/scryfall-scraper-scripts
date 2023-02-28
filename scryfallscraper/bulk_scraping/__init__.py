r"""
Scrape Bulk Magic Card Data from Scryfall!
Warning: Most data here is > 100MB.

Documentation: https://scryfall.com/docs/api/bulk-data
"""
from .functions import (
    scrape_oracle_cards,
    scrape_unique_artwork,
    scrape_default_cards,
    scrape_all_cards,
    scrape_rulings,
)
