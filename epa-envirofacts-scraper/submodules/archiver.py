import os
import requests
from .log import initLogger

logger = initLogger("archiver.py")

ef_service_url = "http://iaspub.epa.gov/enviro/efservice"
csv_url = "{}/{}/ROWS/{}:{}/CSV"
default_dir = os.path.join(
    os.path.dirname(__file__), os.path.pardir, os.path.pardir,
    "epa_gov_enviro_facts_archive")

def _mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        logger.info("Created dir: %s", path)

def _setup(f):
    def wrapper(*args, **kwargs):
        # set default dir if not passed in
        kwargs['data_dir'] = kwargs.get('data_dir', None) or default_dir
        _mkdir(os.path.realpath(kwargs['data_dir']))
        return f(*args, **kwargs)

    return wrapper

def _create_table_dir(f):
    def wrapper(*args, **kwargs):
        _mkdir(
            os.path.join(
                kwargs.get('data_dir', default_dir),
                kwargs.get('table_name', 'no_table_name')))
        return f(*args, **kwargs)

    return wrapper

def _has_rows(r):
    for i, r in enumerate(r.iter_lines()):
        if i >= 2: return True
    return False

def _query_range(start, batch_size):
    return (start, start + batch_size - 1)

@_create_table_dir
def _download(table_name=None,
              data_dir=default_dir,
              start=0,
              batch_size=10000,
              **kwargs):
    while 1:
        try:
            url = csv_url.format(ef_service_url, table_name,
                                 *_query_range(start, batch_size))
            req = requests.get(url, timeout=120) # secs
            logger.info("Downloaded from: %s", url)

            if not _has_rows(req):
                logger.info("Table {} has no more rows".format(table_name))
                break

            file_name = os.path.join(
                data_dir, table_name, "{}_rows_{}_{}.csv".format(
                    table_name, *_query_range(start, batch_size)))

            with open(file_name, "w") as f:
                f.write(req.text)
                logger.info("Saved %s", file_name)

            start += batch_size

        except Exception as e:
            logger.error("Failed to archive data from {}\n{}".format(url, e))

    logger.info("Done archiving table %s", table_name)

@_setup
def archive(tables, limit=None, *args, **kwargs):
    """
    Main function to archive table using https://www.epa.gov/enviro/envirofacts-data-service-api
    """
    if isinstance(tables, str):
        tables = [tables]

    for i, table in enumerate(tables):
        if not limit or i < limit:
            _download(table_name=table, **kwargs)
        else:
            break

if __name__ == '__main__':
    archive(['ef_l_destruction_dev_details'])
