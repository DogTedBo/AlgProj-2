# ...

class UI:

    def bubble_sort_test():
        print("Case Scenarios for Bubble Sort")
        print("---------------")
        print("1. Best Case")
        print("2. Average Case")
        print("3. Worst Case")
        print("4. Exit bubble sort test")

        while True:
            case_choice = input("Select the case scenario (1 - 4): ")
            if case_choice == "1":
                print("Best Case Scenario")
                print("---------------")
                arr = generate_sorted_array(10)
                print("Original array: ", arr)
                BubbleSort(arr)
                print("Sorted array: ", arr)
                # Test the result
                assert arr == sorted(arr), "Bubble Sort failed for the best case scenario"
            elif case_choice == "2":
                print("Average Case Scenario")
                print("---------------")
                arr = generate_random_array(10)
                print("Original array: ", arr)
                BubbleSort(arr)
                print("Sorted array: ", arr)
                # Test the result
                assert arr == sorted(arr), "Bubble Sort failed for the average case scenario"
            elif case_choice == "3":
                print("Worst Case Scenario")
                print("---------------")
                arr = generate_reverse_sorted_array(10)
                print("Original array: ", arr)
                BubbleSort(arr)
                print("Sorted array: ", arr)
                # Test the result
                assert arr == sorted(arr), "Bubble Sort failed for the worst case scenario"
            elif case_choice == "4":
                break
            else:
                print("Invalid input. Please try again.")
        print("Exiting bubble sort test...")