class Node:
    def __init__(self):
        self.data   =   None
        self.next   =   None

    def set_data(self,data):
        self.data   =   data

    def set_next(self,next):
        self.next   =   next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

#Create Object of the class.

ch  = Node()
ch1 = Node()  #To implement next node

#Test Cases

ch.set_data(12)
ch1.set_data(4)
ch.set_next(ch1)
print(ch.get_data())
print(ch.get_next().data)
