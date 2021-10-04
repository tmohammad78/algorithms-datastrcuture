
class SortPath():
    def __init__(self):
        pass

    def find(self,dictionary):
        reveresed_d = dict()
        for key,value in dictionary.items():
            reveresed_d[value]=key
        for key,value in reveresed_d.items():
            if value not in reveresed_d:
                starting = value
                break
        while(starting in dictionary):
            print(starting,"->",dictionary[starting],end=", ")
            starting = dictionary[starting]

list = dict()
list["tehran"] = "shiraz"
list["ghom"]   = "mashhad"
list["tabriz"] = "tehran"
list["shiraz"] = "ghom"
solution = SortPath()
solution.find(list)