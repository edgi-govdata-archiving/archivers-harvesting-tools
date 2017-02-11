# Python scraper

This is [diafygi](https://github.com/diafygi)'s scraping script for the
[2017 DataRescueSFBay event](https://github.com/DataRescueSFBay/DataRescueSFBay-Event).

There's several commented out sections that have example scripts to get
started for various types of situations. Just uncomment the section that
you need and start coding!

## How to use

* Install the dependencies (recommended to use a python3 virtualenv).
```
pip install -r requirements.txt
```
* Update `scraper.py` with whatever code you need to download the files.

* Run the scraper.
```
python3 scraper.py --output ../../data/
```

* Zip up the results folder
```
zip -r output.zip /path/to/dir
```

* Upload to http://www.archivers.space/

## How to upload to S3 via command line

* Get temporary S3 credentials and upload path from http://www.archivers.space/

* Export the AWS credentials
```
export AWS_ACCESS_KEY_ID=AAAAAA
export AWS_SECRET_ACCESS_KEY=BBBBBBBB
export AWS_SESSION_TOKEN=CCCCCCCCC
````

* Upload to S3 (`aws` should already be installed from the `requirements.txt`)
```
aws s3 cp output.zip s3://drp-upload/remote/ADD_UUID_HERE.zip --region us-east-1
```

## How to get Selenium working

If you use `webdriver.Firefox()`, you need to download `geckodriver` to your PATH.
* Download your OS's version of `geckodriver` here: https://github.com/mozilla/geckodriver/releases
* Copy the `geckodriver` executable to your virtualenv's `/bin` directory.

If you use `webdriver.Chrome()`, you need to download `chromedriver` to your PATH.
* Download your OS's version of `chromedriver` here: https://sites.google.com/a/chromium.org/chromedriver/downloads
* Copy the `chromedriver` executable to your virtualenv's `/bin` directory.
