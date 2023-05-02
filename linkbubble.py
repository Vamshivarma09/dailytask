class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def bubbleSort(self):
        if self.head is None:
            return
        end = None
        while end!=self.head:
            prev = None
            current= self.head
            while current.next !=end:
                nextNode = current.next
                if current.data> nextNode.data:
                    current.next = nextNode.next
                    nextNode.next = current
                    if prev: 
                        prev.next = nextNode
                    else:
                        self.head = nextNode
                    current, nextNode = nextNode, current
                prev = current
                current = nextNode
            end = current


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = "\n")
            temp = temp.next
        print()        



linked_list = LinkedList()
linked_list.add(int(input("Enter the Value: ")))
linked_list.add(int(input("Enter the Value: ")))
linked_list.add(int(input("Enter the Value: ")))
linked_list.add(int(input("Enter the Value: ")))
linked_list.add(int(input("Enter the Value: ")))
linked_list.add(int(input("Enter the Value: ")))

print("before sorting of linked list: \n")
linked_list.display()

linked_list.bubbleSort()

print("after sorting of linked list: \n")
linked_list.display()