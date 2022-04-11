# web-crawler

### command example

```
python3 web_crawler.py --root https://medium.com/ --depth 3
```
CLI arguments:
```
$ python3 web_crawler.py --help
Usage: web_crawler.py [OPTIONS]

Options:
  --root TEXT      url to crawl  [required]
  --depth INTEGER  recursion depth limit, --depth 1 meaning only root page
                   will be scanned    [required]
  --mode TEXT      local or cluster
  --output TEXT    path to output file
  --help           Show this message and exit.

```

### web-crawler todo

- ~~command line arguments parsing~~
- ~~fetch web page content~~
- ~~HTTP and HTTPS support (if protocol part of the URL is missing from the URL parameter (e.g. when the URL is www.wikipedia.com, no http:// or https://) you can decide how to handle it.)~~
- ~~get list of links~~
- ~~calculate page rank~~
- ~~recursive crawling~~
- ~~caching~~
- treat errors
- tests
- ~~data structure to keep the registry of links~~
- dockerize
- configuration
- parallelize the process
- distributed solution