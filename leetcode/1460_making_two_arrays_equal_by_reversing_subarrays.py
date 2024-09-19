# the problem of the leetcode solving the problem with different approches and also mention  the time and space complexity. 


"""
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.

"""



# approch 1

"""
sort both the array and then compare if both are equal return true else false
"""
from typing import List 

def isequal1(target: List[int], arr : List[int]) -> bool:

    # first of all we will check that if the length is not same return false

    if len(target) != len(arr):
        return False

    # sort both the arrays
    target.sort()
    arr.sort()

    # now compare both the array if they are equal return true else false

    if target == arr:
        return True
    else:
        return False
    


# checking 
# print(isequal1([1,2,3,4],[4,3,2,1]))


"""Time complexity: the time complexity is 0(n log n)"""
"""space complexity: The space complexity is 0(n) because it depends on the length of array"""









# approch 2 

"""
The second approch is that we will measure the occurance of both array and then compare both the dic of 
occurance if the both are equal so return true else false. 

"""

def isequal2(target: List[int], arr : List[int]) -> bool:

    # this step is must in every approch 
    
    if len(target) != len(arr):
        return False
    
    # now we will create dictionary for the target array and store the occurance of it. 
    dic_target = {}

    # now we will apply loop on the target array and add the occurance in a dictionary

    for i in range(len(target)):
        # now we will check that if the item in not present in the dic so add the item and if present increment it. 
        dic_target[target[i]] = dic_target.get(target[i], 0) + 1     # if the target is  present increment if not add it 

    
    # now we will create the dictionary for the arr 
    dic_arr = {}

    # now we will apply loop on the arr and add the occurance in the dictionary

    for i in range(len(arr)):
        dic_arr[arr[i]] = dic_arr.get(arr[i], 0) + 1
    

    # now we will compare both the target and arr if they are equal return True else False

    if dic_target == dic_arr:
        return True
    else:
        return False
    


# checking the isequla2 funciton 
print(isequal2([1,2,3,4],[4,3,2,1]))




"""Time complexity: The time complexity of this approch is 0(n) because we are adding the occurane in both dictionary which depend on the length of the arrays  and the we compare the two dictionary which also take 0(n)
so the time complexity of this approch is O(n). 
"""


"""
Space Complexity: 
        The space complexity of this approch is also 0(n) because we are storing the whole arrary in the dictionary if the length of the dictionary is high its space complexity is also come O(n). 

"""







# Approch 3 

"""
In this approch we wil be only take one dictionary in which we the occranc of the arr will be stored 
and then we will apply loop on the target and then check that if the element of the target is 
present in the dictioanry so if the element is not present we will return False and if present
we will decrement the occurance of that element in the arr dictionary if the occurance is equal to 0
we will remove the element for  the element and then in the last  if the dictionary is empty so we will
return True.
"""

def isequal3(target,arr):

    # first of all we will check that if the length is not equal return False
    
    if len(target) != len(arr):
        return False
    
    # now we will create a dictionary for the arr and store the occurance of element in the array

    dic_arr = {}
    
    for i in range(len(arr)):
        dic_arr[arr[i]] = dic_arr.get(arr[i],0) + 1

    # now we will apply loop on the target 
    
    for item in target:
        # now we wil check that if the item not in dic so return false 
        if item not in dic_arr:
            return False
        else:
            dic_arr[item] = dic_arr[item] - 1
            if dic_arr[item] == 0:
                del dic_arr[item]
        
    
    if dic_arr:
        return False
    else:
        return True
    


print(isequal3([1,2,3,4], [2,3,4,1]))




# approch 4

"""
In this i will use the Counter from the collections and this counter counts the occuranc and then compare both the list of the occurance is same it return True else False 
"""

# now importing the Counter from the collections
from collections import Counter


def isequal4(target : List[int],arr : List[int]) -> bool:

    if len(target) != len(arr):
        return False
    
    return Counter(target) == Counter(arr)


# now we are testing the approch 4

print(isequal4([1,2,3,4],[4,3,2,1]))





# approch 5

"""
In this apporch  i will use the list because we will take benefits from the constraints. in the constraints the length of the array will be 1000 so i  will take a list and the list will contains only
zeros and then i will apply loop and at the same index i will add element to the array and in the same
index i will decrement it and in the last i will check that if the list have not all zeros so return False else return True. 


"""


def canBeequal(target : List[int], arr : List[int]) -> bool:

    # first of all we will check that if the length is not same return false

    if len(target) != len(arr):
        return False
    
    # now i will create a list and this list will have 1001 zeros

    count_arr = [0] * 1001

    # now i will find the length of one array , i take target you can
    # also take arr
    n = len(target)

    # now i will apply loop and then i will add the target element first
    # and after add the target element  in the same index i will minus the 
    # arr element in the same index. 
    # for example if a add 4  from the target at the index 0 on the count_arr
    # in the next step i will minus the element of arr from count arr at 
    # the same index


    for i in range(n):
        count_arr[target[i]] += 1   # here we are adding the target element
        count_arr[arr[i]] -= 1  # here we are decrement the arr element
    

    # after completion of the loop if the target and arr have one different
    # element so the count_arr will not have all zeros

    for count in count_arr:
        if count != 0:
            return False
    

    return True



# now we are testing the CanBeequal


print(canBeequal([1,2,3,4],[4,3,2,1]))



# approch 6

"""
In this approch we are  comparing the list with the help of reversing sub arrays. 
"""

def canBeequal2(target : List[int], arr : List[int]) -> bool:

    # this step is must because it save us time

    if len(target) != len(arr):
        return False

    # first of all i will take three variables and these variable will help me to copy the sub array
    start = 0
    end = 0

    # now in the variable the length of the array will be stored. 
    length_array = len(target)

    # now i will apply loop and in the loop i will give the condition that if end < length_arry

    while end < length_array:  # if the end is equal or greate the loop will be terminated 

        # now i will check that if the arr[startt] is equal to the target[end] so make a copy
        # and reverse the subarrays

        if arr[end] == target[start]:

            # so we will take a copy of it
            copy = arr[start: end + 1] # here we add 1 because we also want to add the equal value


            # now we will apply the loop the reverse the above copy subarrays and add it in the
            # original array

            for i in range(start, end+1): # the loop will start from the start because we only 
                # the subarray in the original arr
                arr[i] = copy[end-i]  # here it will reverse the element
            

            # after reverse the element so we will go the next element for this we will 
            # update the start pointer as well as the end pointer

            start += 1
            end = start

        else:
            # if the element are not same in the arr and target so we simply update the end
            end += 1
    

    # in the last we will check that if both the target and arr are equal so return true else
    # return False

    return target == arr


print(canBeequal2([1,2,3,4],[2,4,1,3]))




    







