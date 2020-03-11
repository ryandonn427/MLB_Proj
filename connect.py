import psycopg2

class Connect():
        def connect(self):
                dbname = 'mlb'
                user = 'postgres'
                host = 'mlb.cgnkztpljiz8.us-east-2.rds.amazonaws.com'
                port = 5432
                password = 'LJq3VBgsamIUOcJfwHf7'
                conn = psycopg2.connect("dbname={} user={} password={} host={} port={}".format(dbname,user,password,host,port))
                cur = conn.cursor()
                self.conn,self.cur = conn,cur
                self.conn.autocommit=True
        def insert(self,query):
                self.cur.execute(query)
                #self.conn.commit()
        def truncate(self,table):
                self.cur.execute("TRUNCATE {};".format(table))
                self.conn.commit()
                print("Truncated {}".format(table))
"""
Create the table twitter using the below string and then execute the below commands
CREATE TABLE twitter (
        team varchar(21),
        username text ,
        time varchar(10) ,
        tweet text
)

cur.execute(query)
conn.commit()

"""

"""
ALTER TABLE twitter ADD PRIMARY KEY (username,tweet)
ALTER TABLE twitter ALTER COLUMN time TYPE varchar(20)
"""

a = Connect()
a.connect()
#a.insert("ALTER TABLE gameData_players ALTER COLUMN primaryPositioncode TYPE varchar(2)")
#a.insert("SELECT * FROM liveData_plays_pitch LIMIT 100")
#print(a.cur.fetchall())