import os
import random
import sys
import time


class HeapSort:
    def __init__(self, arr):
        self.arr = arr
    
    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[i] < self.arr[left]:
            largest = left

        if right < n and self.arr[largest] < self.arr[right]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def sort(self):
        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(i, 0)
