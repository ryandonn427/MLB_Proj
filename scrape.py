#import everything
import requests
from table import Table
from jsonParse import jsonParse
#download the json data
class Scrape():
    def __init__(self,id):
        self.id = id
        self.tables_visited = []
    def get_raw_data(self):
        self.re = requests.get('https://statsapi.mlb.com/api/v1.1/game/{}/feed/live?language=en'.format(self.id))
        return self.re.json()
    def create_simple_table(self,name,dbname,path = None):
        new_table = Table(name,dbname)
        full_path = self.get_raw_data()
        for i in path:
            full_path = full_path[i] 
        if type(full_path) is list:
            raise Exception("Your dictionary object is actually a list")
        full_dict = {key:value for (key,value) in full_path.items()}
        
        for i in full_dict:
            if type(full_dict[i]) is dict:
                path.append(full_dict[i])
                continue
                #raise Exception("Your data is in the form of a dictionary")
        new_table.add_data(headers = full_dict.keys(),data = full_dict.values())
        self.tables_visited.append(name)
        return new_table

