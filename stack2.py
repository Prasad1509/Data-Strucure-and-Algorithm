class Stack:
    def __init__(self):
        self.items = []

    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None
    def is_empty(self): return len(self.items) == 0
    def print_stack(self): print(self.items)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.print_stack()    

s.pop()
s.print_stack()   

print(s.peek())   
