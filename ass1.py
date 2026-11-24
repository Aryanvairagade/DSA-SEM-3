
stack = []

def push():
    book = input("Enter book name: ")
    stack.append(book)
    print("Book returned successfully")

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Arranged book:", stack.pop())

def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top book:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack:", stack[::-1])

while True:
    print("\n1.Push  2.Pop  3.Peek  4.Display  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
