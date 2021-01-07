#DataStructures (Programming Fundamentals)
#1.Arrays
class TejasArray:
    def __init__(self):
        self.data={}
        self.length=0
    def append(self, value):
        self.data[self.length]=value
        self.length+=1
        print(self.data)
    def insert(self, index, value):
        if self.length==0 or index==self.length + 1 :
            TejasArray.append(self,value)
        elif index > self.length+1:
            print("Not a valid index")
            return
        else:
            strValue=value
            for i in range (self.length, index-1, -1):
                if i==index:
                    self.data[i]=strValue
                    print(self.data)
                    return
                else:
                    self.data[i]=self.data[i-1]
            self.length+=1
    def get(self):
    def pop(self):
    def remove(self):
    def sort(self):


SampleArray=TejasArray()
SampleArray.append(10)
SampleArray.append(30)
SampleArray.append(40)
SampleArray.insert(0, 20)
