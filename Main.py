import os 
import sys
import time
from BubbleSort import BubbleSort
from MergeSort import MergeSort
from QuickSort import QuickSort

from array_generator import ArrayGenerator

class UI:
    def print_menu():
        print("\033[43m\033[30mWelcome to Sorting Algorithm Tester\033[0m")
        print("\033[1m\033[95mMain Menu\033[0m")
        print("\033[32m1. Bubble Sort\033[0m")
        print("\033[34m2. Merge Sort\033[0m")
        print("\033[36m3. Quick Sort\033[0m")
        print("\033[31m4. Exit\033[0m")
        
        choice = input("\033[1mEnter your choice (1-4):\033[0m ")
        if choice == "1":
            UI.bubble_sort_test()
        elif choice == "2":
            UI.merge_sort_test()
        elif choice == "3":
            UI.quick_sort_test()
        elif choice == "4":
            print("\033[1m\033[95mGoodbye!\033[0m")
            sys.exit()
        else:
            print("\033[91mInvalid input\033[0m")
            UI.print_menu()
 
    def bubble_sort_test():
        print("\033[1m\033[95mCase Scenarios for Bubble Sort\033[0m")
        print("---------------")
        print("\033[94m1. Best Case\033[0m")
        print("\033[94m2. Average Case\033[0m")
        print("\033[94m3. Worst Case\033[0m")
        print("\033[94m4. Exit bubble sort test\033[0m")
        
        while True:
            case_choice = input("\033[1mSelect the case (1-4):\033[0m ")
            if case_choice == "1":
                print("Best case scenario")
                # Best case scenario
                size = int(input("\033[1mEnter the size of the array:\033[0m "))
                arr = ArrayGenerator.generate_sorted_array(size)
                bubble_sort_instance = BubbleSort(arr)
                start_time = time.perf_counter()
                bubble_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
                UI.bubble_sort_test()
            elif case_choice == "2":
                print("Average case scenario")
                # Average case scenario
                size = int(input("\033[1mEnter the size of the array:\033[0m "))
                arr = ArrayGenerator.generate_random_array(size)
                bubble_sort_instance = BubbleSort(arr)
                start_time = time.perf_counter()
                bubble_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
                UI.bubble_sort_test()
            elif case_choice == "3":
                # Worst case scenario
                print("Worst case scenario")
                size = int(input("\033[1mEnter the size of the array:\033[0m "))
                arr = ArrayGenerator.generate_reverse_sorted_array(size)
                bubble_sort_instance = BubbleSort(arr)
                start_time = time.perf_counter()
                bubble_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
                UI.bubble_sort_test()
            elif case_choice == "4":
                # go to main menu
                UI.print_menu()
            else:
                print("\033[91mInvalid input\033[0m")


    def merge_sort_test():
        print("\033[1m\033[95mCase Scenarios for Merge Sort\033[0m")
        print("---------------")
        print("\033[94m1. Best Case\033[0m")
        print("\033[94m2. Average Case\033[0m")
        print("\033[94m3. Worst Case\033[0m")
        print("\033[94m4. Exit merge sort test\033[0m")

        while True:
            case_choice = input("\033[1mSelect the case (1-4):\033[0m ")
            if case_choice == "1":
                print("Best case scenario")
                # Best case scenario
                size = int(input("\033[1mEnter the size of the array:\033[0m "))
                arr = ArrayGenerator.generate_sorted_array(size)
                merge_sort_instance = MergeSort(arr)
                start_time = time.perf_counter()
                merge_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
                UI.merge_sort_test()
            elif case_choice == "2":
                print("Average case scenario")
                # Average case scenario
                size = int(input("\033[1mEnter the size of the array:\033[0m "))
                arr = ArrayGenerator.generate_random_array(size)
                merge_sort_instance = MergeSort(arr)
                start_time = time.perf_counter()
                merge_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
                UI.merge_sort_test()
            elif case_choice == "3":
                # Worst case scenario
                print("Worst case scenario")
                size = int(input("\033[1mEnter the size of the array:\033[0m "))
                arr = ArrayGenerator.generate_reverse_sorted_array(size)
                merge_sort_instance = MergeSort(arr)
                start_time = time.perf_counter()
                merge_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
                UI.merge_sort_test()
            elif case_choice == "4":
                # go to main menu
                UI.print_menu()
            else:
                print("\033[91mInvalid input\033[0m")

    def quick_sort_test():
        print("\033[1m\033[95mCase Scenarios for Quick Sort\033[0m")
        print("---------------")
        print("\033[94m1. Best Case\033[0m")
        print("\033[94m2. Average Case\033[0m")
        print("\033[94m3. Worst Case\033[0m")
        print("\033[94m4. Exit quick sort test\033[0m")

        while True:
            case_choice = input("\033[1mSelect the case (1-4):\033[0m ")
            if case_choice == "1":
                print("Best case scenario")
                # Best case scenario
                size = int(input("\033[1mEnter the size of the array:\033[0m "))
                arr = ArrayGenerator.generate_sorted_array(size)
                quick_sort_instance = QuickSort(arr)
                start_time = time.perf_counter()
                quick_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
                UI.quick_sort_test()
            elif case_choice == "2":
                print("Average case scenario")
                # Average case scenario
                size = int(input("\033[1mEnter the size of the array:\033[0m "))
                arr = ArrayGenerator.generate_random_array(size)
                quick_sort_instance = QuickSort(arr)
                start_time = time.perf_counter()
                quick_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
                UI.quick_sort_test()
            elif case_choice == "3":
                # Worst case scenario
                print("Worst case scenario")
                size = int(input("\033[1mEnter the size of the array:\033[0m "))
                arr = ArrayGenerator.generate_reverse_sorted_array(size)
                quick_sort_instance = QuickSort(arr)
                start_time = time.perf_counter()
                quick_sort_instance.sort()
                end_time = time.perf_counter()
                elapsed_time_ms = (end_time - start_time) * 1000
                print(f"For N = {len(arr)}, it takes {elapsed_time_ms:.4f} milliseconds")
                UI.quick_sort_test()
            elif case_choice == "4":
                # go to main menu
                UI.print_menu() 
            else:
                print("\033[91mInvalid input\033[0m")


if __name__ == "__main__":
    UI.print_menu()
    
    

