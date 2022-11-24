### Various Problems Using Recursion ###

## Binary Search using Python 3

class RecursiveSolution:
 
    # Returns index of x in arr if present, else -1
    def binary_search(self, arr:list, low:int, high:int, x:int):
    
        # Check base case
        if high >= low:
    
            mid = (high + low) // 2 
    
            # If element is present at the middle itself
            if arr[mid] == x:
                return mid
    
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
    
            # Else the element can only be present in right subarray
            else:
                return self.binary_search(arr, mid + 1, high, x)
    
        else:
            # Element is not present in the array
            return -1


## Testing The Solution 
test = RecursiveSolution()

# Binary Search Test 
index = test.binary_search([ 2, 3, 4, 10, 40 ], 0, 4, 10)
result = "Found at index " + str(index) if index != -1 else "Not Found"
print(result)
    
    
    
