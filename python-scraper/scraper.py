#! /usr/bin/env python3
# Erase the below and write a short summary of what you're scraping
description = """
Description:
This script pulls scrapes NOAA Quality Controlled Datasets from:
https://www.ncdc.noaa.gov/crn/qcdatasets.html
"""

manpage = """
This is diafygi's scraping script for the 2017 DataRescueSFBay event.
https://github.com/DataRescueSFBay/DataRescueSFBay-Event
https://github.com/edgi-govdata-archiving/harvesting-tools
-------
License:
GPLv3
-------
Dependencies:
pip install selenium==3.0.2 beautifulsoup4==4.5.3 lxml==3.7.2 pdfminer.six==20160614
-------
Command:
python3 datarescue_script --output ../data/
"""
DEFAULT_OUTPUT_DIR = "../data/"

def main(output_dir=DEFAULT_OUTPUT_DIR):
    """
    This is where you write your scraping scripts. There's a bunch of commented
    out sections that have example scripts to get started for various types of
    situations. Just uncomment the section that you need and start coding!
    """
    #######################################
    ## Html parsing using beautifulsoup4 ##
    #######################################
    # open a webpage
    # parse out the a link via css selectors
    # save that link

    ##########################################
    ## Full browser scraping using Selenium ##
    ##########################################
    # open a webpage
    # wait for the page to load
    # click on a link via css selector
    # wait for the page to load
    # save that loaded page

    ###################
    ## Dump pdf text ##
    ###################
    # open a pdf

    print("Done!")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=manpage)
    parser.add_argument('--output', '-o',
                        default=DEFAULT_OUTPUT_DIR,
                        help='output directory (default: "{}")'.format(DEFAULT_OUTPUT_DIR))
    args = parser.parse_args()
    main(output_dir=args.output)

