# Purpose: Merge Sort algorithm implementation
import os
import sys
import time
import random

class MergeSort: # Class to implement merge sort
    def __init__(self, arr): # Constructor to initialize the array    
        self.arr = arr # Initialize the array
        
    def sort(self):  # Method to sort the array
        arr = self.arr  
        if len(arr) > 1: 
            mid = len(arr)//2 
            L = arr[:mid] 
            R = arr[mid:] 

            # Recursively sort both halves
            self.arr = L 
            self.sort() 
            self.arr = R 
            self.sort() 

            i = j = k = 0 # Initialize the index variables

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
            # Check if any elements are right
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
