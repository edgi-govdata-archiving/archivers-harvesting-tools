# Diafygi's python scraper

This is [diafygi](https://github.com/diafygi)'s scraping script for the
[2017 DataRescueSFBay event](https://github.com/DataRescueSFBay/DataRescueSFBay-Event).

There's a bunch of commented out sections that have example scripts to get
started for various types of situations. Just uncomment the section that
you need and start coding!

## How to use

* Install the dependencies (recommended to use a virtualenv).
```
pip install -r requirements.txt
```
* Update `scraper.py` with whatever code you need to download the files.

* Run the scraper.
```
python3 scraper.py --output ../../data/
```

* Zip up the results folder

* Upload to http://www.archivers.space/

## [TODO] How to upload via S3

* **[TODO]** Get an S3 access token from http://www.archivers.space/

* **[TODO]** Upload to S3
```
python3 uploader.py "S3_TOKEN_HERE" output.zip
```

## How to get Selenium working

If you use `webdriver.Firefox()`, you need to download `geckodriver` to your PATH.
* Download your OS's version of `geckodriver` here: https://github.com/mozilla/geckodriver/releases
* Copy the `geckodriver` executable to your virtualenv's `/bin` directory.

If you use `webdriver.Chrome()`, you need to download `chromedriver` to your PATH.
* Download your OS's version of `chromedriver` here: https://sites.google.com/a/chromium.org/chromedriver/downloads
* Copy the `chromedriver` executable to your virtualenv's `/bin` directory.
