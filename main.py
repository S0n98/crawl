from utils import read_url_from_file
from request_thread import RequestThread
from bs4 import BeautifulSoup

def main():
  urls = read_url_from_file('drug.txt')

  threads = [RequestThread(url) for url in urls]
  threads[0].start()
  threads[0].join()
  print(threads[0].result)
  return
  for thread in threads:
    thread.start()
  for thread in threads:
    thread.join()
  for thread in threads:
    print(thread.result)
  
main()

