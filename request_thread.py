import threading
import requests
from bs4 import BeautifulSoup

class RequestThread(threading.Thread):
  def __init__(self, url):
    threading.Thread.__init__(self)
    self.url = url
    self.result = None
  
  def run(self):
    try:
      headers = {'Accept-Encoding': 'gzip'}
      res = requests.get(self.url, timeout=5, headers=headers)
      print(res.text)

      soup = BeautifulSoup(res.text, "html.parser")
      self.result = {self.url.split(':')[-1]:soup.body.get_text().strip()}
    except(requests.exceptions.Timeout):
      print(f"{self.url} timeout ...")