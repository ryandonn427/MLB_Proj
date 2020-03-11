
class jsonParse():
    def __init__(self,dictionary):
        self.dictionary = dictionary
        self.keys = []
        self.values=[]
        self.dictionary_keys= []
        self.counter = 0
    def parse(self,dictionary=None,prep = ''):
        #print(dictionary)
        if not dictionary: dictionary=self.dictionary
        if type(dictionary) is list:
          for i in dictionary:
            self.parse(i)
        else:
          for i in dictionary.keys():
              self.counter+=1
              if type(dictionary[i]) is dict:
                  if len(dictionary[i]) == 0:
                      return
                  self.dictionary_keys.append(i)
                  self.parse(dictionary[i],prep=prep+i)
              elif type(dictionary[i]) is list:
                for j in dictionary[i]:
                  self.parse(j,prep=prep+i)
              else:
                  self.keys.append(prep+i)
                  self.values.append(dictionary[i])
