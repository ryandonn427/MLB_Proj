import requests
from bs4 import BeautifulSoup
from connect import Connect
from datetime import datetime
from pytz import timezone

teams_raw = open('teams.txt','r').readlines()
teams = [j.replace('\n','').lower() for j in [i for i in teams_raw] if '-' in j]
class Tweet():
    def __init__(self,team,username,time,text):
        self.team = ' '.join([i[0].upper() + i[1:].lower() for i in team.split('-')])
        self.username = username
        self.time = datetime.now(timezone('EST')).strftime('%h %d %H:%M') 
        self.text = text.replace('\n','').replace('  ','')
    def print_list(self):
        print([self.team,self.username,self.time,self.text])
    def insert(self):
        query = """
        INSERT INTO twitter (team,username,time,tweet) VALUES (
            '{}','{}','{}','{}'
        ) ON CONFLICT DO NOTHING
        """.format(self.team,self.username.replace("'","''"),self.time,self.text.replace("'","''"))
        return query
def get(team):
    a = Connect()
    a.connect()
    page = 1
    with open('twitter_scrape_file.txt','a') as file:
        while True:
            re = requests.get('https://sportspyder.com/teams/{}/tweeter_types/3/tweets?page={}'.format(team,page))
            bs = BeautifulSoup(re.content,'html.parser')
            tweets = bs.find_all('div',attrs = {'class':'twitter_content'})
            if len(tweets) == 0 : return
            for i in tweets:
                t = Tweet(
                    team,
                    i.find('span',attrs= {'class':'username'}).text,
                    i.find('span',attrs={'class':'time'}).text,
                    i.find('div',attrs={'class':'text'}).text
                )
                file.write(str(t.time))
                file.write('\n')
                a.insert(t.insert())
            page+=1
            print(page)
    

for i in teams:
    get(i)
    
