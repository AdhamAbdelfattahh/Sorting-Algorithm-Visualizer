import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Define sorting algorithms

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

# Quick Sort
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            yield arr
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        yield arr
        return i + 1

    if low < high:
        pi = yield from partition(arr, low, high)
        yield from quick_sort(arr, low, pi - 1)
        yield from quick_sort(arr, pi + 1, high)

# Merge Sort
def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)

    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort(arr, start, mid)
        yield from merge_sort(arr, mid, end)
        left, right = arr[start:mid], arr[mid:end]
        i = j = 0
        for k in range(start, end):
            if i >= len(left):
                arr[k] = right[j]
                j += 1
            elif j >= len(right):
                arr[k] = left[i]
                i += 1
            elif left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            yield arr

# Function to update the bars in the graph
def update_plot(arr, bars):
    for rect, val in zip(bars, arr):
        rect.set_height(val)

# Function to visualize sorting
def visualize_sorting(algorithm, arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, align='edge')
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * len(arr)))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def init():
        update_plot(arr, bars)
        return bars

    def update(arr):
        update_plot(arr, bars)
        return bars

    ani = animation.FuncAnimation(fig, update, frames=algorithm, init_func=init, interval=50, repeat=False, save_count=200)
    plt.show()

# Driver code to test sorting algorithms
if __name__ == "__main__":
    n = 50  # Number of elements
    arr = [random.randint(1, n) for _ in range(n)]
    
    print("Select sorting algorithm: \n1. Bubble Sort\n2. Quick Sort\n3. Merge Sort")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        algorithm = bubble_sort(arr.copy())
        print("Visualizing Bubble Sort")
    elif choice == 2:
        algorithm = quick_sort(arr.copy())
        print("Visualizing Quick Sort")
    elif choice == 3:
        algorithm = merge_sort(arr.copy())
        print("Visualizing Merge Sort")
    else:
        print("Invalid choice!")
        exit()

    visualize_sorting(algorithm, arr)
