class Node:
    #creating a node

    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# create an object from derived class
llist = LinkedList()
llist.head = Node("Pawan Kalyan ")
second = Node("Srinivasan B ")
third = Node("NIhar ")
fourth = Node("Ranjan ")

#connetcing the nodes
llist.head.next = second
second.next = third
third.next = fourth

# print
while llist.head!=None:
    print(llist.head.item)
    llist.head = llist.head.next