import os 
import sys
import time
import random
from BubbleSort import BubbleSort
from array_generator import ArrayGenerator
from MergeSort import MergeSort
from QuickSort import QuickSort

class UI:

    def bubble_sort_test():
        print("Case Scenarios for Bubble Sort")
        print("---------------")
        print("1. Best Case")
        print("2. Average Case")
        print("3. Worst Case")
        print("4. Exit bubble sort test")

        while True:
            case_choice = input("Select the case (1-4): ")
            if case_choice == "1":
                 # Best case scenario
                print("Best case scenario")
                size = int(input("Enter the size of the array: "))
                arr = ArrayGenerator.generate_sorted_array(size)  # Use ArrayGenerator to generate sorted array
                bubble_sort_instance = BubbleSort(arr)  # Pass array as parameter to the constructor
                start_time = time.perf_counter()
                bubble_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
            elif case_choice == "2":
                # Average case scenario
                print("Average case scenario")
                size = int(input("Enter the size of the array: "))
                arr = ArrayGenerator.generate_random_array(size)  # Use ArrayGenerator to generate random array
                bubble_sort_instance = BubbleSort(arr)  # Pass array as parameter to the constructor
                start_time = time.perf_counter()
                bubble_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
            elif case_choice == "3":
                # Worst case scenario
                print("Worst case scenario")
                size = int(input("Enter the size of the array: "))
                arr = ArrayGenerator.generate_reverse_sorted_array(size)  # Use ArrayGenerator to generate reverse sorted array
                bubble_sort_instance = BubbleSort(arr)  # Pass array as parameter to the constructor
                start_time = time.perf_counter()    
                bubble_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
            elif case_choice == "4":
                break

 #test for merge sort


def main():
    print("Select the sorting algorithm you want to test.")
    print("-------------------------")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    print("4. Heap Sort")
    print("5. Exit")

    while True:
        choice = input("Select the sorting algorithm (1 - 5): ")
        if choice == "1":
            UI.bubble_sort_test()
        elif choice == "2":
            UI.merge_sort_test()
        elif choice == "3":
            UI.quick_sort_test()
        elif choice == "4":
            UI.heap_sort_test()
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")
     

if __name__ == "__main__":
    main()
    


   
