import threading
import requests
from crawl_data import CrawlData

class RequestThread(threading.Thread):
  def __init__(self, url):
    threading.Thread.__init__(self)
    self.url = url
    self.result = None
    self.web_crawl = CrawlData()
  
  def run(self):
    try:
      pass
    except(requests.exceptions.Timeout):
      print(f"{self.url} timeout ...")