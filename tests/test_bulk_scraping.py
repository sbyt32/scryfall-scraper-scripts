# from scryfall_scraper_scripts import bulk_scraping

# # bulk_scraping.scrape_oracle_cards(params={})
# from scryfall_scraper_scripts import scraper

# # with scraper.BulkScraper() as bulk:
# #     bulk.s
# def scrape_oracle_cards(params=None, **kwargs):
#     r""" Scrape oracle data.

#     :param bulk_type: adasdsd
#     :param zipped: Return either as an dict or write to the current directory.
#     """
#     bulk = scraper.BulkScraper()
#     bulk.scrape_bulk_data("oracle", params=params, **kwargs)

from scryfallscraper import sets

print(sets.scrape_by_code("mmq"))