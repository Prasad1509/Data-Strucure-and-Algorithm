size = 5
q = [None]*size
front = rear = -1

def enqueue(val):
    global front, rear
    if (rear + 1) % size == front:
        print("Queue is Full")
    elif front == -1:
        front = rear = 0
        q[rear] = val
    else:
        rear = (rear + 1) % size
        q[rear] = val

def dequeue():
    global front, rear
    if front == -1:
        print("Empty")
    elif front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size
