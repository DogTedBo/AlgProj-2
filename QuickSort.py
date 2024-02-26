# Purpose: Implement the QuickSort algorithm in Python
import os
import sys
import time
import random

class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        
    def sort(self):  # Method to sort the array
        def partition(arr, low, high):
            i = low - 1
            pivot = arr[high]

            for j in range(low, high): # Loop to iterate through the array
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i] 

            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i + 1

        def quick_sort(arr, low, high): # Method to sort the array
            if low < high: 
                pi = partition(arr, low, high)

                quick_sort(arr, low, pi - 1)
                quick_sort(arr, pi + 1, high)

        quick_sort(self.arr, 0, len(self.arr) - 1)  # Call the quick_sort method to sort the array
