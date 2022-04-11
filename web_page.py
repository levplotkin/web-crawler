import typing
from logging import getLogger

import bs4
import requests

import web_address

log = getLogger(__name__)


class Page:
    def __init__(self, url: str):
        self.url = url
        self.content = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
        self.web_address = web_address.WebAddress()
        self.cache: typing.Dict[str, typing.Any] = dict()

    def calculate_rank(self) -> float:
        "Calculate the rank of the page as ratio of same domain links to all links"
        domain = self.web_address.get_domain(self.url)
        external_links_count = len(self.___get_external_links(domain))
        all_links_count = len(self.___get_all_links())

        rank = 0 if all_links_count == 0 else (all_links_count - external_links_count) / all_links_count
        return rank

    def get_all_links(self) -> typing.List[str]:
        domain = self.web_address.get_domain(self.url)

        self_links = self.___get_self_links(domain)
        external_links = self.___get_external_links(domain)
        relative_links = self.___get_relative_links()
        relative_links_full = []
        for relative_link in relative_links:
            relative_links_full.append(self.url + relative_link)

        return self_links + relative_links_full + external_links

    def ___get_all_links(self) -> typing.List[str]:
        if "all_links" in self.cache:
            return self.cache["all_links"]

        html_anchors = self.content.find_all('a')
        try:
            links = [attributes['href'] for attributes in html_anchors]
        except KeyError:
            log.error("KeyError: 'href' not found in html_anchors")
            links = []
        self.cache["all_links"] = links
        return links

    def ___get_relative_links(self) -> typing.List[str]:
        links = self.___get_all_links()
        return list(filter(lambda page_address: not self.web_address.is_valid_url(page_address), links))

    def ___get_self_links(self, domain: str) -> typing.List[str]:
        links = self.___get_all_links()

        return list(filter(
            lambda page_address: self.web_address.is_valid_url(page_address) and self.web_address.is_same_domain(
                page_address, domain), links))

    def ___get_external_links(self, domain: str) -> typing.List[str]:
        links = self.___get_all_links()
        return list(filter(
            lambda page_address: self.web_address.is_valid_url(page_address) and not self.web_address.is_same_domain(
                page_address, domain), links))
