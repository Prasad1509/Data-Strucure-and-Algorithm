class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else None
    def peek(self): return self.items[0] if self.items else None
    def is_empty(self): return len(self.items) == 0
    def print_queue(self): print(self.items)
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.print_queue()    
q.dequeue()
q.print_queue()    

print(q.peek())    


