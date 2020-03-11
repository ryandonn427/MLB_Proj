from connect import Connect
tables = [
    'gameData_weather',
'gameData_status',
'gameData_primaryDatacaster',
'gameData_officialScorer',
'gameData_game',
'gameData_flags',
'gameData_datetime',
'liveData_plays_hotcold_pitcher',
'liveData_plays_hotcold_batter',
'liveData_officials',
'liveData_decision',
'liveData_linescore',
'liveData_plays_pitch',
'liveData_plays_runners',
'liveData_plays_matchup',
'liveData_plays_count',
'liveData_plays_about',
'liveData_plays_result',
'gameData_venue',
'gameData_teams',
'gameData_probablePitchers',
'gameData_players',
]

a = Connect()
a.connect()
data=[]
with open('queries.txt','r') as file:
    for i in file.readlines():
        if 'INSERT INTO gameData_datetime' in i:
            data.append(i.split('VALUES (')[1].split(',')[0].replace("'",''))



for j in tables:
    a.insert("DELETE FROM {} WHERE gameid IN ({});".format(str(j),str(','.join(data))))
    print("deleted {}".format(j))
