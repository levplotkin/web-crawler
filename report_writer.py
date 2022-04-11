import csv
from logging import getLogger

log = getLogger(__name__)


def save_report(output, visited_pages):
    with open(output, 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(['url', 'depth', 'ratio'])  # header
        for url, (depth, rank) in visited_pages.items():
            tsv_writer.writerow([url, depth, rank])
    log.info(f"finished crawling, result saved to {output}")
