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
        if self.length==0 or index==self.length :
            TejasArray.append(self,value)
        elif index >= self.length+1:
            print("Not a valid index")
            return
        else:
            strValue=value
            for i in range (self.length, index-1, -1):
                if i==index:
                    self.data[i]=strValue
                    self.length+=1
                    print(self.data)
                    return
                else:
                    self.data[i]=self.data[i-1]
        print(self.length)
        print(self.data)

    def get(self, index):
        if index > self.length-1:
            print ("Not a valid index ")
            return
        else:
            print(self.data[index])

    def pop(self, index="-1"):
        if index=="-1" or index == self.length-1:
            strPopItem=self.data[self.length-1]
            del self.data[self.length-1]
            self.length-=1
            print(strPopItem)
            print(self.data)
            print(self.length)
            return strPopItem
        elif index > self.length-1:
            print ("Not a valid index ")
            return
        else:
            for i in range (index, self.length-1):
                if i == index:
                    strPopItem=self.data[i]
                self.data[i]=self.data[i+1]
            del self.data[self.length-1]
            self.length-=1
            print(strPopItem)
            print(self.data)
            print(self.length)
            return

    def sort(self):
        counter=0
        while counter < self.length:
            for i in range(self.length-1):
                if self.data[i]>self.data[i+1]:
                    self.data[i+1], self.data[i] = self.data[i], self.data[i+1]
            counter+=1
        print(self.data)
        return self.data


SampleArray=TejasArray()
SampleArray.append(80)
SampleArray.append(10)
SampleArray.append(1000)
SampleArray.insert(3, 2000)
#SampleArray.insert(0, 'a')
#SampleArray.insert(2, 'b')
#SampleArray.insert(4, 'c')

#SampleArray.get(3)
#SampleArray.pop()
#SampleArray.pop(3)
#SampleArray.pop(2)
SampleArray.sort()
