import argparse, os

from submodules.archiver import archive
from submodules.scraper import get_table_names
from submodules.log import initLogger

logger = initLogger("__main__.py")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="directory to store archived datasets to.", default=None)
    parser.add_argument("-l", "--limit", help="limit the number of tables to download.", type=int, default=None)
    args = parser.parse_args()

    logger.info("Starting archiving process")
    archive(get_table_names(), limit=args.limit, data_dir=args.output)
    logger.info("Done archiving process")

if __name__ == '__main__':
    main()
