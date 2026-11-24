
size = 10
table = [-1] * size

def insert(key):
    index = key % size

    start = index

    while table[index] != -1:
        index = (index + 1) % size

        if index == start:
            print("Hash table is full")
            return

    table[index] = key
    print("Inserted successfully")

def display():
    print("Hash Table:")

    for i in range(size):
        print(i, ":", table[i])

n = int(input("Enter number of keys: "))

for i in range(n):
    key = int(input("Enter key: "))
    insert(key)

display()
