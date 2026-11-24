
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            print("Deleted:", self.head.data)
            self.head = self.head.next

    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

l = LinkedList()

while True:
    print("\n1.Insert Beginning")
    print("2.Insert End")
    print("3.Delete Beginning")
    print("4.Display")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter book ID: "))
        l.insert_begin(data)

    elif ch == 2:
        data = int(input("Enter book ID: "))
        l.insert_end(data)

    elif ch == 3:
        l.delete_begin()

    elif ch == 4:
        l.display()

    elif ch == 5:
        break

    else:
        print("Invalid choice")
