# Scryfall Scraper Scripts

Do you see yourself scraping the Scryfall database often?

Me, too! Here is a collection of scripts to help you with that.

*Note: I am not affiliated with the Scryfall Team. Follow their rules:* https://scryfall.com/docs/api

## Things You Can Do (right now)
> More to come later.

### Bulk Scraping
https://scryfall.com/docs/api/bulk-data
```
scrape_oracle_cards()   # oracle_cards on Scryfall.
scrape_unique_artwork() # unique_artwork on Scryfall.
scrape_default_cards()  # default_cards on Scryfall.
scrape_all_cards()      # all_cards on Scryfall.
scrape_rulings()        # rulings on Scryfall.
```

### Set data
https://scryfall.com/docs/api/sets
```    
scrape_all_sets()       # all sets
scrape_by_code()        # one set by set code
scrape_by_scryfall_id() # one set by scryfall id
scrape_by_tcgplayer_id()# one set by tcgplayer id
```

### Compression
Not a Scryfall Scrape, but nifty tools you may need.
```
compress_dir()          # Compress a directory a bunch of .gz files
```