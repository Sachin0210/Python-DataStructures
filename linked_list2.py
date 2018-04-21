class Node(object):
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = None

print("a = {} and next -> {}".format(a.value, a.nextNode.value))
print("b = {} and next -> {}".format(b.value, b.nextNode.value))
print("c = {} and next -> {}".format(c.value, c.nextNode.value))
print("d = {} and next -> {}".format(d.value, d.nextNode.value))
