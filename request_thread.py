import threading
import requests
from bs4 import BeautifulSoup
from lxml import html
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

class RequestThread(threading.Thread):
  def __init__(self, url):
    threading.Thread.__init__(self)
    self.url = url
    self.result = None
  
  def run(self):
    try:
      headers = {'Accept-Encoding': 'gzip, deflate, br', 'User-Agent': user_agent, 'accept': accept}
      res = requests.get(self.url, timeout=5, headers=headers)

      tree = html.fromstring(res.content)
      #needed_data = tree.xpath('//*[@id="MD"]/table/tbody/tr[20]/td[2]/ul')
      needed_data = tree.xpath('//*[@id="MD"]/table/tbody')
      print(needed_data)
      self.result = {self.url.split(':')[-1]:needed_data}
    except(requests.exceptions.Timeout):
      print(f"{self.url} timeout ...")