# Diafygi's python scraper

This is diafygi's scraping script for the 2017 DataRescueSFBay event.
https://github.com/DataRescueSFBay/DataRescueSFBay-Event

There's a bunch of commented out sections that have example scripts to get
started for various types of situations. Just uncomment the section that
you need and start coding!

## How to use

1. Install the dependencies (recommended to use a virtualenv).
```
pip install selenium==3.0.2 beautifulsoup4==4.5.3 lxml==3.7.2 pdfminer.six==20160614
```

2. Update `scraper.py` with whatever code you want (using your favorite).


3. Run the scraper.
```
python scraper --output ../data/
```

