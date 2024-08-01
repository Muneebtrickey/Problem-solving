# problem:

"""
we need to check that all the numbers in a list are distant or not?
"""


# approch 1:


def checking_distant(List):
    for i in range(len(List)):
        for j in range(i+1 , len(List)):
            if List[i] == List[j]:
                return False    # because two values are same 
    return True


print(checking_distant([4,2,3,5]))  # True
print(checking_distant([2,3,4,4,5])) # return False 





# second approch count the numbers

def count_numbers_to_check_distant(List):
    for item in List:
        counter = List.count(item)

        if counter > 1:
            return False
    return True

print(count_numbers_to_check_distant([2,3,4,5])) # this return True
print(count_numbers_to_check_distant([2,3,4,4,5])) # this return False



# 3rd approch using set 


def checking_distant_set(list):
    if len(list) == len(set(list)):
        return True
    return False

print(checking_distant_set([3,2,5,7])) # return True
print(checking_distant_set([3,2,4,5,4]))  # return False
