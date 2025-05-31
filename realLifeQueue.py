queue = []

def serve_customer():
    if queue:
        print("Serving", queue.pop(0))
    else:
        print("No one in queue")

queue.append("Alice")
queue.append("Bob")
serve_customer()  
serve_customer() 
serve_customer() 
