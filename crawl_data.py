from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

from datetime import datetime
import traceback

class CrawlData():
  def crawl(self, url):
    useragent = UserAgent()
    random_useragent = useragent.random

    options = Options()
    options.add_argument(f'user-agent={random_useragent}')

    self.driver = webdriver.Chrome(chrome_options=options, service=Service("./chromedriver"))

    self.driver.get(url)
    url_data = {}
    try:
      ul = self.driver.find_elements(By.XPATH, '//*[@id="MD"]/table/tbody/tr[20]/td[2]/ul/li') #.get_attribute('innerHTML')
      name = self.driver.find_elements(By.XPATH, '//*[@id="MD"]/table/tbody/tr[6]/td[2]/ul/li/span/span')[0].get_attribute('innerHTML')
      url_data["name"] = name

      for li in ul:
        li_soup = BeautifulSoup(str(li.get_attribute("innerHTML")), 'html.parser')
        li_data = li_soup.span.a.string

        if ("SMILE" in li_data):
          url_data["smiles"] = li_data
          break
    except:
      with open("./log/crawl_error.txt", "a") as f:
        f.write(datetime.today().strftime("%d/%m/%Y %H:%M:%S") + ": url error " + url + "\n" + traceback.format_exc() + "\n")
    self.close()
    return url_data

  def close(self):
    self.driver.close()
    #for handle in self.driver.window_handles:
    #  self.driver.switch_to.window(handle)
    #  self.driver.close()

if (__name__ == '__main__'):
  c = CrawlData()
  c.crawl('https://bio2rdf.org/drugbank:DB06605')
