from connect import Connect
a = Connect()
a.connect()
a.insert("SELECT DISTINCT gameid,datetime FROM gameData_datetime")
with open("games_inserted_already.txt","w") as file:
    for i in a.cur.fetchall():
        file.write(str(i[0])+'\n')