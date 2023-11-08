import random
import time


def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quick_sort(arr, low, high):
    if low < high:
        pivot = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pivot - 1)
        deterministic_quick_sort(arr, pivot + 1, high)


def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)


def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, high)


if __name__ == "__main__":
    try:
        n = int(input("Enter the number of elements: "))
        arr = []
        for i in range(n):
            element = int(input(f"Enter element {i + 1}: "))
            arr.append(element)

        deterministic_arr = arr.copy()
        randomized_arr = arr.copy()
                     
        print("\nSorting using Deterministic Quick Sort:")
        start_time = time.time()
        deterministic_quick_sort(deterministic_arr, 0, n - 1)
        end_time = time.time()
        print("Sorted array:", deterministic_arr)
        print("Time taken: {:.6f} seconds".format(end_time - start_time))

        print("\nSorting using Randomized Quick Sort:")
        start_time = time.time()
        randomized_quick_sort(randomized_arr, 0, n - 1)
        end_time = time.time()
        print("Sorted array:", randomized_arr)
        print("Time taken: {:.6f} seconds".format(end_time - start_time))

    except ValueError:
        print("Please enter a valid integer.")
