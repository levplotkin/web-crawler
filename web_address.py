from urllib.parse import urlparse

import validators


class WebAddress:

    def is_valid_url(self, page_address):
        return validators.url(page_address)

    def is_same_domain(self, page_address, domain):
        return urlparse(page_address).netloc == domain

    def get_domain(self, url):
        return urlparse(url).netloc
