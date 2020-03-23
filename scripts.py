from scrape import Scrape
from table import Table
from jsonParse import jsonParse
import time
from get_gameids import ids
from datetime import datetime
from connect import Connect
from combining_statements import get_bulk_queries
import clean_up_ids

games= []


#for j in [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]:
#dates = ids(datetime(year=j,month=2,day=22))
dates = ids(datetime(year=2017,month=8,day=29))
for i in range(60):
    print(dates.date)
    for j in dates.get_ids():
        games.append(j)
        
    dates.next_day()
    
dates.driver.close()

total,counter = len(set(games)),0

games = [i for i in games if i not in [j.replace('\n','') for j in open('games_inserted_already.txt','r').readlines()]]

with open('queries.txt','w') as queries:
    for game in set(games):
        a = Scrape(game)
        #The below is to create tables gameData.datetime,gameData.flags,
        #gameData.game,gameData.officialScorer,gameData.primaryDatacaster,
        #gameData.status,gameData.weather
        
        try:
            b = jsonParse(a.get_raw_data()['gameData']['datetime'])
            b.parse()
            c = Table('datetime','gameData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except:
            print((game,"Issue with datetime"))
        
        try:
            b = jsonParse(a.get_raw_data()['gameData']['flags'])
            b.parse()
            c = Table('flags','gameData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except Exception as e:
            print((e,game,"Issue with flags"))
        try:    
            b = jsonParse(a.get_raw_data()['gameData']['game'])
            b.parse()
            c = Table('game','gameData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except:
            print((game,"Issue with game"))
        
        try:
            b = jsonParse(a.get_raw_data()['gameData']['officialScorer'])
            b.parse()
            c = Table('officialScorer','gameData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except:
            print((game,"Issue with officialScorer"))
        
        try:
            b = jsonParse(a.get_raw_data()['gameData']['primaryDatacaster'])
            b.parse()
            c = Table('primaryDatacaster','gameData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except:
            print((game,"Issue with primaryDatacaster"))
        
        try:
            b = jsonParse(a.get_raw_data()['gameData']['status'])
            b.parse()
            c = Table('status','gameData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except:
            print((game,"Issue with status"))
        
        try:
            b = jsonParse(a.get_raw_data()['gameData']['weather'])
            b.parse()
            c = Table('weather','gameData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except:
            print((game,"Issue with weather"))
        #To create the gameData.players table
        for i in a.get_raw_data()['gameData']['players']:
            try:
                    
                b = jsonParse(a.get_raw_data()['gameData']['players'][i])
                b.parse()
                c = Table('players','gameData')
                c.add_data(b.keys,b.values)
                queries.write(c.insert(a.id))
            except Exception as e:
                print((e,game,"Issue with players",c.insert(a.id)))
        #To create the gameData.probablePitchers

        for i in a.get_raw_data()['gameData']['probablePitchers']:
            try:
                b = jsonParse(a.get_raw_data()['gameData']['probablePitchers'][i])
                b.parse()
                c = Table('probablePitchers','gameData')
                c.add_data(b.keys,b.values)
                c.headers.insert(0,'ha')
                c.data.insert(0,i)
                queries.write(c.insert(a.id))
            except:
                print((game,"Issue with probablePitchers"))        

        # To add gameData.team data
        for i in a.get_raw_data()['gameData']['teams']:
            try:
                b = jsonParse(a.get_raw_data()['gameData']['teams'][i])
                b.parse()
                c = Table('teams','gameData')
                c.add_data(b.keys,b.values)
                queries.write(c.insert(a.id))
            except:
                print((game,"Issue with teams"))
        #To add gameData.venue data

        try:
            b = jsonParse(a.get_raw_data()['gameData']['venue'])
            b.parse()
            c = Table('venue','gameData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except:
            print((game,"Issue with venue"))
        #This is for the liveData.plays.Allplays
        #We have to loop through each at bat
        atbatid = 0
        for i in a.get_raw_data()['liveData']['plays']['allPlays']:
            #liveData.plays.Allplays.result
            try:
                b= jsonParse(i['result'])
                b.parse()
                c = Table('plays_result','liveData')
                c.add_data(b.keys,b.values)
                queries.write(c.insert(a.id,atbatid=atbatid))
            except:
                print((game,"Issue with result"))
            #liveData.plays.Allplays.about
            try:
                b = jsonParse(i['about'])
                b.parse()
                c = Table('plays_about','liveData')
                c.add_data(b.keys,b.values)
                queries.write(c.insert(a.id,atbatid=atbatid))
            except:
                print((game,"Issue with about"))            
            #liveData.plays.Allplays.count    
            try:
                b = jsonParse(i['count'])
                b.parse()
                c = Table('plays_count','liveData')
                c.add_data(b.keys,b.values)
                queries.write(c.insert(a.id,atbatid=atbatid))
            except:
                print((game,"Issue with count"))    
            #liveData.plays.Allplays.matchup (except hot cold zones)
            
            try:
                b = jsonParse(i['matchup'])
                b.parse()
                data = [(i,j) for i,j in zip(b.keys,b.values) if 'HotColdZone' not in i]
                b.keys,b.values = [i[0] for i in data],[i[1] for i in data]
                c = Table('plays_matchup','liveData')
                c.add_data(b.keys,b.values)
                queries.write(c.insert(a.id,atbatid=atbatid))
            except:
                print((game,"Issue with matchup"))        

            #liveData.plays.Allplays.matchup.hotcold
            for zone in ['batterHotColdZones','pitcherHotColdZones']:
                try:
                    b = jsonParse(i['matchup'][zone])
                    b.parse()
                    b.keys = [b.keys[i:i+4] for i in range(len(b.keys))][::4]  
                    b.values = [b.values[i:i+4] for i in range(len(b.values))][::4]
                    if batter in zone:  
                        c = Table('plays_hotcold_batter','liveData')
                    else:
                        c = Table('plays_hotcold_pitcher','liveData')
                    for j,k in zip(b.keys,b.values):
                        c.add_data(j,k)
                        queries.write(c.insert(a.id,atbatid=atbatid))
                except Exception as e:
                    pass
                    #print((game,"Issue with hold cold"))    
            #created the livedata.runners data
            runnerid = 0
            for j in i['runners']:
                try:
                    b = jsonParse(j)
                    b.parse()
                    c = Table('plays_runners','liveData')
                    c.add_data(b.keys,b.values)
                    for k in c.add_duplicate_data(a.id,atbatid=atbatid,runnerid=runnerid):
                        queries.write(k)
                except:
                    print((game,"Issue with runners"))
                finally:
                    runnerid+=1        
            #playevent data
            
            pitchid = 0
            for j in i['playEvents']:
                try:
                    b = jsonParse(j)
                    b.parse()
                    c = Table('plays_pitch','liveData')
                    c.add_data(b.keys,b.values)
                    queries.write(c.insert(a.id,atbatid=atbatid,pitchid=pitchid))
                except:
                    print((game,"Issue with pitch"))
                finally:
                    pitchid+=1
            
            
            atbatid+=1

        #to get the linescore 
        try:
            b = jsonParse(a.get_raw_data()['liveData']['linescore']['teams']['away'])
            b.parse()
            b.keys.insert(0,'ha')
            b.values.insert(0,'away')
            c = Table('linescore','liveData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except:
            print((game,"Issue with linescore"))
        try:
            b = jsonParse(a.get_raw_data()['liveData']['linescore']['teams']['home'])
            b.parse()
            b.keys.insert(0,'ha')
            b.values.insert(0,'home')
            c = Table('linescore','liveData')
            c.add_data(b.keys,b.values)
            queries.write(c.insert(a.id))
        except:
            print((game,"Issue with linescore"))
    
        #get the losing and winning pitchers
        try:
            for i in a.get_raw_data()['liveData']['decisions']:
                try:
                    b = jsonParse(a.get_raw_data()['liveData']['decisions'][i])
                    b.parse()
                    b.keys.insert(0,'wl')
                    b.values.insert(0,i)
                    c = Table('decision','liveData')
                    c.add_data(b.keys,b.values)
                    queries.write(c.insert(a.id))
                except:
                    print((game,"Issue with decision"))
        except:
            print(game,"No decision")
        #get the officials

        for i in a.get_raw_data()['liveData']['boxscore']['officials']:
            try:
                b = jsonParse(i)
                b.parse()
                c = Table('officials','liveData')
                c.add_data(b.keys,b.values)
                queries.write(c.insert(a.id))
            except:
                print((game,"Issue with official"))
        counter+=1
        print("{} Games to go".format(total-counter))

dates.prev_day()
open('dates.txt','a').write(str(dates.date)+'\n')
#Start the next insert at the date written in dates.txt plus one day
#For example:05/2/19 in dates.txt, would tell you to start at 5/3/19

conn = Connect()
conn.connect()
with open('errors.txt','a') as f:
    for i in get_bulk_queries():
        try:
            conn.insert(i)
        except Exception as e:
            f.write(str(e))
            f.write('\n')           
        

