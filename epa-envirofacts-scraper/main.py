import logging

from archiver import archive
from scraper import get_table_name

logger = logging.getLogger("archiver")
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)-15s %(filename)s(%(lineno)d) %(message)s")


def main():
  logger.info("Starting archiving process")
  j = 0
  for table in get_table_name():
    j =+ 1
    archive(table)
    if j == 10:
      break

  logger.info("Done archiving process")

if __name__ == '__main__':
  main()
