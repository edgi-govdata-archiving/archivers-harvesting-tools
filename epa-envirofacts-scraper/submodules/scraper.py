import bs4
import requests
from urllib.parse import urlparse, parse_qs
from .log import initLogger

logger = initLogger("scraper.py")

def get_model_urls():
    """
    Loads the landing page (https://www.epa.gov/enviro/envirofacts-model)
    and scrapes off the URLs for each model which is well-formatted.

    Non-well formatted models are ignored in this script. They have each been
    submitted as separate tickets to https://www.archivers.space

    Returns a list of URLs
    """
    # Download the page
    model_page_url = "https://www.epa.gov/enviro/envirofacts-model"
    re = requests.get(model_page_url)

    # Convert to a bs4 to extract the relevent urls
    soup = bs4.BeautifulSoup(re.text, "html.parser")
    model_selector = 'area[href*="model"]'
    link_soup = soup.select(model_selector)

    links = [
        link['href'] for link in link_soup
        if not link['href'].startswith('http')
    ]  # Remove absolute links
    links = list(set(links))  # Remove duplicates

    return links


def get_tables_from_model_url(url, base_url='https://www.epa.gov'):
    """
    Takes in a url and recursively scrapes page for area html elements for
    subsequent pages and table API references to compile a list of tables and
    urls.

    yields output in a tuple of format:
    {
        table_name: html alt text (so far always the table name),
        table_url: link to the table api page,
        source_url: the page from which the link was scraped
    }
    """

    url = (base_url if 'https://' not in url else '') + url
    html_doc = requests.get(url).content.decode('utf-8', 'ignore')
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')

    for s in soup.select('area'):
        href_url = s.get('href')
        qs = parse_qs(urlparse(href_url).query)

        if 'p_table_name' not in qs:
            for i in get_tables_from_model_url(href_url, base_url=base_url):
                yield i
        else:
            yield {
                'table_url': href_url,
                'table_name': qs['p_table_name'][0],
                'alt_text': s.get('alt'),
                'source_url': url
            }


def get_table_names():
    """
    Returns a generator of table names which can be used against the API to download data.
    """

    model_urls = get_model_urls()

    for model_url in model_urls:
        logger.info('Pulling tables for model: {}'.format(model_url))
        for scraped_table_dict in get_tables_from_model_url(model_url):
            yield scraped_table_dict['table_name']


if __name__ == '__main__':
    ## EXAMPLE
    for j, item in enumerate(get_table_name()):
        print("%d. %s" % (j, item))
