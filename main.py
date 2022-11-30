from crawl_data import CrawlData
from utils import read_url_from_file
from bs4 import BeautifulSoup
#from request_thread import RequestThread

def main():
  urls = read_url_from_file('drug.txt')[:2]
  web_crawl = CrawlData()

  #url_data = []
  url_data = []

  for url in urls:
    data = web_crawl.crawl(url)
    if data:
      url_data.append(data)

  with open('./result.txt', 'a') as f:
    for data in url_data:
      f.writelines(f"{data['name']}, {data['smiles']}\n")

  #MAINTAINING
  #threads = [RequestThread(url, web_crawl) for url in urls]
  #count = 0
  #for thread in threads:
  #  thread.start()
  #  if count == 5: 
  #    count = 0
  #    web_crawl.close_all()
  #  count += 1
  #for thread in threads:
  #  thread.join()
  #for thread in threads:
  #  print(thread.result)
  
main()
