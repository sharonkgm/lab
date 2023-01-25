class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.last = None
    def append(self,data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
list = Linkedlist()
a = int(input("enter the no.of elements to add : "))
for i in range(a):
    data = int(input("enter the elements : "))
    list.append(data)
print("linked list is :")
list.display()

