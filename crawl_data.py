from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CrawlData():
  def __init__(self):
    self.driver = webdriver.Chrome(service=Service("./chromedriver"))

  def crawl(self, url):
    self.driver.get(url)
    url_data = {url: {}}
    ul = self.driver.find_elements(By.XPATH, '//*[@id="MD"]/table/tbody/tr[20]/td[2]/ul/li') #.get_attribute('innerHTML')
    name = self.driver.find_elements(By.XPATH, '//*[@id="MD"]/table/tbody/tr[6]/td[2]/ul/li/span/span')[0].get_attribute('innerHTML')
    url_data[url]["name"] = name

    for li in ul:
      li_soup = BeautifulSoup(str(li.get_attribute("innerHTML")), 'html.parser')
      li_data = li_soup.span.a.string

      if ("SMILE" in li_data):
        url_data[url]["smiles"] = li_data
        break

if (__name__ == '__main__'):
  c = CrawlData()
  c.crawl('https://bio2rdf.org/drugbank:DB06605')
