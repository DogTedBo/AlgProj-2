# Description: This file contains the implementation of the heap sort algorithm.
import os
import random
import sys
import time


class HeapSort: # Class to implement heap sort
    def __init__(self, arr): # Constructor to initialize the array
        self.arr = arr
    
    def heapify(self, n, i): # Method to heapify the array
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[i] < self.arr[left]: # If the left child is greater than the root
            largest = left # Set the largest to the left child

        if right < n and self.arr[largest] < self.arr[right]: # If the right child is greater than the largest 
            largest = right # Set the largest to the right child

        if largest != i: # If the largest is not the root
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i] # Swap the root and the largest
            self.heapify(n, largest) # Heapify the array

    def sort(self): # Method to sort the array
        n = len(self.arr) # Length of the array

        for i in range(n // 2 - 1, -1, -1): # Loop to iterate through the array
            self.heapify(n, i) # Heapify the array

        for i in range(n - 1, 0, -1): # Loop to iterate through the array
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i] # Swap the root and the last element
            self.heapify(i, 0) # Heapify the array
