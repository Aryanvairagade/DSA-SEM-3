
def heapify(arr, n, i, is_max):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if is_max:
        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

    else:
        if left < n and arr[left] < arr[largest]:
            largest = left

        if right < n and arr[right] < arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, is_max)


def heap_sort(arr, is_max):
    n = len(arr)

    # Build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, is_max)

    # Sorting
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, is_max)

    return arr


arr = list(map(int, input("Enter numbers: ").split()))

print("Original Array:", arr)

print("Ascending Order (Max Heap):",
      heap_sort(arr.copy(), True))

print("Descending Order (Min Heap):",
      heap_sort(arr.copy(), False))
