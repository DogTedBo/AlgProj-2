# quick_sort.py

class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        
    def sort(self):  # Corrected method signature
        def partition(arr, low, high):
            i = low - 1
            pivot = arr[high]

            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i + 1

        def quick_sort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)

                quick_sort(arr, low, pi - 1)
                quick_sort(arr, pi + 1, high)

        quick_sort(self.arr, 0, len(self.arr) - 1)  # Access the array using self
