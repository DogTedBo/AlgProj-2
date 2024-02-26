import os
import sys
import time
import random


class BubbleSort: # Class to implement bubble sort
    def __init__(self, arr): # Constructor to initialize the array
        self.arr = arr
    
    def sort(self): # Method to sort the array
        n = len(self.arr) # Length of the array
        for i in range(n-1): # Loop to iterate through the array
            for j in range(0, n-i-1): # Loop to iterate through the array
                if self.arr[j] > self.arr[j+1]: # If the current element is greater than the next element
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j] # Swap the elements

