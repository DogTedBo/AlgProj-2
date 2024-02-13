import os
import sys
import time
import random


class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
    
    def sort(self):
        n = len(self.arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

