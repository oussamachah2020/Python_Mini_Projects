# Binary Search 

def Binary_Search(arr, high, low, x):
    mid = (high + low) // 2
    
    if high >= low:
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return Binary_Search(arr, mid - 1, low, x)
        else: 
            return Binary_Search(arr, high, mid + 1, x)
    else:
        return -1
    
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5

result = Binary_Search(arr, len(arr)-1, 0, x)

if result != -1:
    print("it's in element of index", str(result))
else:
    print("not matched")