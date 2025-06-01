class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ->") 
            current=current.next
        print("None")

ll=LL()
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_beginning(3)
ll.insert_at_beginning(4)
ll.insert_at_beginning(5)
ll.display()           
                                                        