# web-crawler

crawler keeps visited pages data in memory, in future it can be switched to database

crawler keeps queue of links in memory, in future it can be switched to queue management system

report saved to local file (tsv) at the end of crawler process in future it can be replaced by streaming to show the results during the process


#### components: 
- user parameters validator (cli_validator.py)
- crawler (web_crawler.py)
- page parser (web_page.py)
- report writer (report_writer.py)


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