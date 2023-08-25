def binary_search(array, target, high, low):

    if high >= low:
        print(f"High = {high}")
        print(f"Target = {target}")

        mid = (high + low) // 2
        print(f"Mid = {mid}")

        # If element is present at the middle itself
        if array[mid] == target:
            print(" GOT THE VALUE!!!")
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif array[mid] < target:
            print("Value has been increased", array[mid])
            return binary_search(array, target, high, mid + 1)

        # Else the element can only be present in right subarray
        else:
            print("Value has been decreased")
            return binary_search(array, target, mid - 1, low)

    else:
        # Element is not present in the array
        return -1


# Test array
random = ["apple", "banana", "cat", "dog", "elephant", "frog", "giraffe", "horse", "iguana", "jackal", "kangaroo"]


# Function call
result = binary_search(random, "elephant", len(random)-1, 0)

if result != -1:
    print("Element is present at position", result + 1)
else:
    print("Element is not present in array")


person_table_return_from_sql = [("value", "value"), ("new", "new"), ("name", "phone number"), ("something", "email")]
