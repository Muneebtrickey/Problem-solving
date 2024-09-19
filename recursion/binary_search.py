# binary search



def binary_search(data , target):
    low  , high = 0 , len(data) - 1

    while low < high:
        mid = ((low) + (high)) // 2

        if data[mid] == target:
            return mid
        
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1 # if the target is not found


print(binary_search([1,2,3,4,5,6,7,8,9], 3))




# binary search using  recursion 


def binary_search_using_recursion(data, target , low , high):


    if low > high:
        return False
    else:

        mid =  ((low) + (high)) // 2

        if data[mid] == target:
            return True
        
        elif data[mid] < target:
            return binary_search_using_recursion(data, target, mid+1 , high)
        else:
            return binary_search_using_recursion(data, target, low, mid-1)



print(binary_search_using_recursion([1,2,3,4,5,6,7], 9 , 0 ,6))