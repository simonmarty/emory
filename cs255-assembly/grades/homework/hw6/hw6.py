a = [1,2,3,5,5,6,7]
k = 3

def binarySearch(array, low, high, key):
    if high >= low:
        midpoint = low + (high-low) // 2
        val = array[midpoint]
        if val == key:
            return midpoint
        elif val > key:
            return binarySearch(array, low, midpoint - 1, key)
        else:
            return binarySearch(array, midpoint + 1, high, key)
    else:    
        return -1

print(binarySearch(a, 0, len(a)-1, k))