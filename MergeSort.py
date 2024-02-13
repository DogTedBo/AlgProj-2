# merge_sort.py

class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        
    def sort(self):  # Corrected method signature
        arr = self.arr  # Access the array using self
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            # Recursively sort both halves
            self.arr = L
            self.sort()
            self.arr = R
            self.sort()

            i = j = k = 0

            # Merge the sorted halves
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Check if any elements are left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
