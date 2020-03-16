from selenium import webdriver
import re
from datetime import datetime,timedelta
import time
class ids():
    def __init__(self,startdate):
        if type(startdate) is str:
            raise Exception("This is not a datetime object")
        else:
            self.date = startdate
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-logging')
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome('C:\\Users\\rdonnelly\\Documents\\GitHub\\chromedriver.exe',options=options)
    def get_ids(self):
        self.driver.get('https://www.mlb.com/scores/{}'.format(self.date.strftime('%Y-%m-%d')))
        time.sleep(5)
        results = []
        pattern = 'https:\/\/www\.mlb\.com\/gameday\/(\d+)\/final\/box'
        for i in self.driver.find_elements_by_tag_name('a'):
            if re.match(pattern,str(i.get_attribute('href'))):
                results.append(re.findall(pattern,str(i.get_attribute('href')))[0])
        return results
    def next_day(self):
        self.date = self.date + timedelta(days=1)
    def prev_day(self):
        self.date = self.date - timedelta(days=1)