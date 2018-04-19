class Stack(object):
	def __init__(self):
		self.stk = []
	
	def has_values(self):
		return(self.stk != [])
	
	def push(self,item):
		self.stk.append(item)
	
	def pop(self):
		self.stk.pop()

	def size(self):
		return(len(self.stk))
s = Stack()

#Test Cases:

print("Pushing Some elemnts in the Stack:")
s.push(20)
s.push(15)
s.push(10)
s.push(5)

print("Checking does stack has some values inside in it:")
print(s.has_values())

print("Before Poping size:")
print(s.size())

print("After Poping an element size:")
s.pop()
print(s.size())
