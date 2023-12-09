def find_uniq(arr):
    # Convert the list to a set to get unique elements
    unique_elements = set(arr)
    print("Unique elements:", unique_elements)

    # Iterate through unique elements and find the one that occurs only once in the original list
    for element in unique_elements:
        count = arr.count(element)
        print(f"Count of {element}:", count)
        if count == 1:
            print("Unique number found:", element)
            return element

# Test cases
print(find_uniq([1, 1, 1, 2, 1, 1]))  # Output: 2
print(find_uniq([0, 0, 0.55, 0, 0]))  # Output: 0.55

