"""
This is a pure Python implementation of the heap sort algorithm.

For doctests run following command:
python -m doctest -v heap_sort.py
or
python3 -m doctest -v heap_sort.py

For manual testing run:
python heap_sort.py
"""


def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


if __name__ == "__main__":
    # user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [10, 21, 1, 4, 3, 7, 0, 23]
    print(heap_sort(unsorted))