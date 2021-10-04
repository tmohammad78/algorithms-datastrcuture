class employe():
    
    def __init__(self):
        pass
    
    def travers(self,tuple):
        dictionary = dict()
        for key,value in tuple:
            if(key == value):
                continue
            if key not in dictionary:
                dictionary[key]=[]
            if value not in dictionary:
                dictionary[value]=[key]
            else:
                dictionary[value].append(key)
        return dictionary
    
    def sum(self,dictionary):
        newDict = dict()
        for key,value in dictionary.items():
            newDict[key] = len(dictionary[key])
            for value in dictionary[key]:
                newDict[key] += len(dictionary[value])
            print("{} : {}".format(key,newDict[key]))
    
    def solving(self,tuple):
        dictionary = self.travers(tuple)
        self.sum(dictionary)


t = (("A", "C"),("B", "C"),("C", "F"),("D", "E"),("E", "F"),("F", "F"))
solution = employe()
solution.solving(t)