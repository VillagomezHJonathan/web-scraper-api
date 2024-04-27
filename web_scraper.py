import requests
from bs4 import BeautifulSoup

class WebScraper():
    def __init__(self, url):
        self.url = url
        res = requests.get(self.url, headers=requests.utils.default_headers())
        self.soup = BeautifulSoup(res.content, 'html.parser')
    
    def get_elements(self, selector):
        elems = self.soup.select(selector)
        return [e.get_text() for e in elems]
    
    def get_table(self, dict):
        table_arr = []
        for key, val, i in dict.items():
            # elems = self.get_elements(val)
            table_arr.append(i)   
        # table_arr = []
        # for i in range(len(dict)):
        #     table_arr.append(i)
        
        return table_arr