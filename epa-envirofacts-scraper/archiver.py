import os
import logging
import requests
from log import initLogger

logger = initLogger("archiver.py")

efservice_url = "http://iaspub.epa.gov/enviro/efservice"
csv_url = "{}/{}/ROWS/{}/CSV"
archive_dir = "epa_gov_enviro_facts_archive"

def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        logger.info("Created dir: %s", path)

def setup(f):
    def wrapper(*args, **kwargs):
        mkdir(archive_dir)
        r = f(*args, **kwargs)
        return r
    return wrapper

def create_table_dir(f):
    def wrapper(*args, **kwargs):
        table = args[0]
        dir_name = "{}/{}".format(archive_dir, table)
        mkdir(dir_name)
        r = f(*args, **kwargs)
        return r
    return wrapper

def has_rows(r):
    count = 0
    result = False
    for a in r.iter_lines():
        count += 1
        if count > 1:
            result = True
            break
    return result

@create_table_dir
def download(table):
    start = 0
    end = batch_size = 10000
    while True:
        try:
            cursor_pos = "{}:{}".format(start, end)
            url = csv_url.format(efservice_url, table, cursor_pos)
            req = requests.get(url)
            logger.info("Downloaded from: %s", url)
            if not has_rows(req):
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

@setup
def archive(tables):
    """
    Main function to archive table using https://www.epa.gov/enviro/envirofacts-data-service-api
  """
    if isinstance(tables, str):
        tables = [tables]

    for table in tables:
        download(table)

if __name__ == '__main__':
    #Example table_name
    archive(['ef_l_destruction_dev_details'])
