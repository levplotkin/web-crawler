import logging
from logging import getLogger

import click

from cli_validator import validate_positive_int, validate_url
from report_writer import save_report
from web_page import Page

log = getLogger(__name__)


@click.command()
@click.option('--root', help='url to crawl', required=True, type=str, callback=validate_url)
@click.option('--depth', help='recursion depth limit, --depth 1 meaning only root page will be scanned  ',
              required=True, type=int, callback=validate_positive_int, )
@click.option('--mode', help='local or cluster', default="local", type=str)
@click.option('--output', help='path to output file', default="result.tsv", type=str)
def run_crawler(root: str, depth: int, mode: str, output: str):
    log.info(f"start crawler for {root}, depth is {depth}, mode: {mode}")

    current_links_queue, further_links_queue, visited_pages = _init(root)
    start_depth = depth + 1
    while depth > 0:
        log.info(f"current queue size: {current_links_queue}")
        for link in current_links_queue:
            links_in_page = process_page(current_depth(depth, start_depth), link, visited_pages)
            enqueue_links(links_in_page, further_links_queue)

        log.info(f"current count of visited pages {len(visited_pages)}")

        current_links_queue = list(filter(lambda x: x not in visited_pages, further_links_queue))
        further_links_queue = set()
        depth -= 1

    save_report(output, visited_pages)


def current_depth(depth, start_depth):
    return start_depth - depth


def enqueue_links(links_in_page, further_links_queue):
    log.info(f"current in further queue: {len(further_links_queue)}, queued links: {len(links_in_page)}")
    further_links_queue.update(links_in_page)


def process_page(depth, link, visited_pages):
    page = Page(link)
    rank = page.calculate_rank()
    links_in_page = page.get_all_links()
    visited_pages[link] = (depth, rank)
    log.info(f"visited {link} rank: {rank}, depth: {depth}")
    return links_in_page


def _init(root):
    tmp_links_queue = set()
    visited_pages = dict()
    links_queue = _init_links_queue(root)
    return links_queue, tmp_links_queue, visited_pages


def _init_links_queue(root):
    links_queue = set()
    links_queue.add(root)
    return links_queue


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    log = getLogger(__name__)
    run_crawler()
