# array_generator.py

import random

class ArrayGenerator:
  
    def generate_sorted_array(size):
        return list(range(1, size + 1))

  
    def generate_reverse_sorted_array(size):
        return list(range(size, 0, -1))

   
    def generate_random_array(size):
        return [random.randint(1, 1000) for _ in range(size)]
