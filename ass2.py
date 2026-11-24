
queue = []
size = 5

def enqueue():
    if len(queue) == size:
        print("Queue is full")
    else:
        customer = input("Enter customer name: ")
        queue.append(customer)
        print("Customer added")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Customer served:", queue.pop(0))

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)

while True:
    print("\n1.Enqueue  2.Dequeue  3.Display  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")
