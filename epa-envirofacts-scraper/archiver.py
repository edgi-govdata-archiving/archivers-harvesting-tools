import os
import logging
import requests

logging.getLogger("requests").setLevel(logging.WARNING)
logger = logging.getLogger("archiver")
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)-15s %(filename)s(%(lineno)d) %(message)s")

ef_service_url = "http://iaspub.epa.gov/enviro/efservice"
archive_dir = "epa_gov_enviro_facts_archive"
csv_url = "{}/{}/ROWS/{}/CSV"


def _setup(f):

    def wrapper(*args, **kwargs):
        if not os.path.isdir(archive_dir):
            os.mkdir(archive_dir)
        r = f(*args, **kwargs)
        return r

    return wrapper


def _create_table_dir(f):

    def wrapper(*args, **kwargs):
        table = args[0]
        dir_name = "{}/{}".format(archive_dir, table)
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
            logger.info("Created dir: %s", dir_name)
        r = f(*args, **kwargs)
        return r

    return wrapper

def _has_rows(r):
    count = 0
    rows = False
    for a in r.iter_lines():
        count += 1
        if count > 2:
            rows = True
            break
    return rows

@_create_table_dir
def _download(table):
    start = 0
    end = batch_size = 10000
    while 1:
        try:
            cursor_pos = "{}:{}".format(start, end)
            url = csv_url.format(ef_service_url, table, cursor_pos)
            req = requests.get(url)
            logger.info("Downloaded from: %s", url)
            if not _has_rows(req):
                logger.info("Table {} has no more rows".format(table))
                break
            file_name = "{}/{}/{}_rows_{}_{}.csv".format(archive_dir, table,
                                                         table, start, end)
            with open(file_name, "w") as file:
                file.write(req.text)
                logger.info("Saved %s", file_name)
            start = end + 1
            end += batch_size
        except:
            logger.error("Failed to archive data from {}".format(url))

    logger.info("Done archiving table %s", table)


@_setup
def archive(tables):
    """
    Main function to archive table using https://www.epa.gov/enviro/envirofacts-data-service-api
  """
    if isinstance(tables, str):
        tables = [tables]

    for table in tables:
        _download(table)


if __name__ == '__main__':
    archive(['ef_l_destruction_dev_details'])
