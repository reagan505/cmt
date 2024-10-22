#An algorithm with linear time complexity iterates over the entire input once.

#Real-World Example: Finding a specific book on a shelf by looking at each book one by one

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [4, 2, 7, 1, 3]
print(linear_search(arr, 7))  
