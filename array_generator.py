# array_generator.py

import random

class ArrayGenerator:   # Class to generate arrays of different types
  
    def generate_sorted_array(size):  # Generate sorted array
        return list(range(1, size + 1))

  
    def generate_reverse_sorted_array(size): # Generate reverse sorted array
        return list(range(size, 0, -1))

   
    def generate_random_array(size):
        return [random.randint(1, 1000) for _ in range(size)] # Generate random array
