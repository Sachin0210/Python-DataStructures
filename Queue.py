def Queue(object):
	def __init__(self):
		self.qu = []

	def isEmpty(self):
		self.qu == []

	def enQueue(self,item):
		self.qu.insert(0,item)

	def deQueue(self):
		self.qu.pop()
