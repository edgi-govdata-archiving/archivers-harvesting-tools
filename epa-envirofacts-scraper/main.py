from log import initLogger
from archiver import archive
from scraper import get_table_name

logger = initLogger("main.py")

def main():
    logger.info("Starting archiving process")
    j = 0
    for table in get_table_name():
        j = +1
        archive(table)
        if j == 10:
            break
    logger.info("Done archiving process")

if __name__ == '__main__':
    main()
