import numpy as np
class Table():
    def __init__(self,name,dbname):
        self.name = name
        self.dbname = dbname
    def add_data(self,headers = None, data = None):
        if data and headers:
            self.data = ['NULL' if type(i) is str and (i.count('-') == len(i) or i == '.---') else i for i in data]
            self.data = [str(i).replace(',',';') for i in self.data]
            self.headers = headers
        elif data is not list and headers is not list:
            raise Exception("All the data needs to be in the form of a list")
        else:
            raise Exception("All the data is not present")
    def add_duplicate_data(self,gameid,atbatid = None,runnerid = None,pitchid = None):
        dictionary = {}
        for i,j in zip(self.headers,self.data):
            if i in dictionary:
                dictionary[i].append(j)
            else:
                dictionary[i] = [j]   
        once = [(i,j) for i,j in dictionary.items() if len(j) == 1]
        twice = [(i,j) for i,j in dictionary.items() if len(j) > 1]
        raw_data = np.array([i[1] for i in twice]).T
        for i in raw_data.tolist():
            self.data = [i[1][0] for i in once]
            self.headers = [i[0] for i in once]
            for k in twice:
                self.headers.append(k[0])
            for j in i:
                self.data.append(j)
        #print(*(i for i in [(self.name,'gameid',gameid),(self.name,'atbatid',atbatid),
        #(self.name,'runnerid',runnerid),(self.name,'pitchid',pitchid)] if i))
        yield self.insert(**{'gameid':gameid,'atbatid':atbatid,'runnerid':runnerid,'pitchid':pitchid}) 
    def insert(self,gameid,atbatid = None,runnerid = None,pitchid = None):
        if atbatid is not None:
            header = 'atbatid,'
            atbatid = "'{}',".format(str(atbatid))
        else:
            header,atbatid='',''
        if runnerid is not None:
            header_run = 'runnerid,'
            runnerid = "'{}',".format(str(runnerid))
        else:
            header_run,runnerid = '',''
        if pitchid is not None:
            header_pitch = 'pitchid,'
            pitchid = "'{}',".format(str(pitchid))
        else:
            header_pitch,pitchid = '',''
        if self.data and self.headers:
            query =  "INSERT INTO {}_{} (gameid,{}{}{}{}) VALUES ('{}',{}{}{}{})\n".format(
                self.dbname,self.name,header,header_run,header_pitch,','.join(list(self.headers)),gameid,atbatid,runnerid,pitchid,','.join(["'"+str(i).replace("'","''")+"'" for i in list(self.data)])
                )
            query = query.replace("'NULL'",'NULL')
            return query
