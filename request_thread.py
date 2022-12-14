import threading
import requests
from crawl_data import CrawlData

class RequestThread(threading.Thread):
  def __init__(self, url, web_crawl):
    threading.Thread.__init__(self)
    self.url = url
    self.result = None
    self.web_crawl = web_crawl
  
  def run(self):
    try:
      url_data = self.web_crawl.crawl(self.url)
      self.result = url_data
    except(requests.exceptions.Timeout):
      print(f"{self.url} timeout ...")