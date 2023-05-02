class Node:
    def __init__(self,val):
        self.val = val
        self.nextVal = None
class linked_list:
    def __init__(self):
        self.head = None

    def insertAtMid(self, mid, newData):
        if mid is None:
            print("nothing can be inserted")
            return
        newNode = Node(newData)
        newNode.nextVal = mid.nextVal
        mid.nextVal = newNode

    def removeItem(self, itemToBeRemoved):
        headval = self.head

        if headval:
            if headval.val == itemToBeRemoved:
                self.head = headval.next
                headval = None
                return
            
        while headval:
            if headval.val == itemToBeRemoved:
                break
            prev = headval
            headval = headval.nextVal

        if headval == None:
            return
        
        prev.nextVal = headval.nextVal
        headval = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end = ", ")
            temp = temp.nextVal

linkedList = linked_list()
linkedList.head = Node("Anusha")
linkedList2 = Node("Mydhili")
linkedList3 = Node("Prathap")
linkedList.head.nextVal = linkedList3
linkedList3.nextVal = linkedList2
linkedList.insertAtMid(linkedList3,"Kiran")
linkedList.removeItem("Prathap")
linkedList.display()