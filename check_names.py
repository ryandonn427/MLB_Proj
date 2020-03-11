import time
tables = {}
tables_nums = {}
def check_string(query):
    headers = query.split('VALUES (')[0].split(' (')[1].replace(')','')
    data = query.split('VALUES (')[1].replace(');','')
    headers = [str(i) for i in headers.split(',')]
    data = [str(i).replace('"','') for i in data.split(',')]
    for i,j in zip(headers,data):
        print(i,j)
query = """
INSERT INTO gameData_teams (gameid,id,name,link,season,venueid,venuename,venuelink,teamCode,fileCode,abbreviation,teamName,locationName,firstYearOfPlay,leagueid,leaguename,leaguelink,sportid,sportlink,sportname,shortName,recordgamesPlayed,recordwildCardGamesBack,recordleagueGamesBack,recordspringLeagueGamesBack,recordsportGamesBack,recorddivisionGamesBack,recordconferenceGamesBack,recordleagueRecordwins,recordleagueRecordlosses,recordleagueRecordpct,parentOrgName,parentOrgId,allStarStatus,active) VALUES ('585638','366','Detroit Tigers Futures','/api/v1/teams/366','2019','2511','Publix Field at Joker Marchant Stadium','/api/v1/venues/2511','dfs','t366','DFS','Tigers Futures','Detroit','2001','590','Futures Game','/api/v1/league/590','21','/api/v1/sports/21','Minor League Baseball','Tigers Futures','1',NULL,NULL,NULL,NULL,NULL,NULL,'0','1','.000','Detroit Tigers','116','F','True')
"""
check_string(query)
def create_sets():
    with open('queries_test.txt','r') as file:
        for i in file.readlines():
            vals = i.split(')')[0].split('(')[1].split(',')
            nums = i.split(')')[1].split('(')[1].split(',')
            table = i.split('INSERT INTO ')[1].split(' (')[0]
            if table in tables:
                tables[table].append(set(vals))
            else:
                tables[table] = [set(vals)]
            if table in tables_nums:
                tables_nums[table].append(set(nums))
            else:
                tables_nums[table] = [set(nums)]
def get_list_names(table):
    pitch = []
    for i in tables[table]:
        #print(table,len(i))
        for j in i:
            pitch.append(j)
    return set(pitch)

def check_names():
    for i in tables:
        for j in get_list_names(i):
            print(j)

    for i in tables_nums:
        print(i)