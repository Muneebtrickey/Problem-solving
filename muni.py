# approach 1

def checking_distant(List):
    for i in range(len(List)):
        for j in range(i+1, len(List)):
            if List[i] == List[j]:
                return False
    
    return True

List = [1,2,3,4,5]
List1 = [1,2,3,3,3]

print(checking_distant(List))
print(checking_distant(List1))




# approch 2
# using set

def check_distant(List):
    if len(List) == len(set(List)):
        return True
    else:
        return False
    

print(check_distant(List))
print(check_distant(List1))




# approach 3 
# using the sort approach

def check_distant_by_sort(List):
    sorted_list = sorted(List)
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if sorted_list[i] == sorted_list[j]:
                return False
    return True


print(check_distant_by_sort(List))
print(check_distant_by_sort(List1))







# approach 4

def counter_check_distant(List):
    counter = 0
    for item in List:
        counter = List.count(item)

        if counter > 1:
            return False
    return True

print(counter_check_distant(List))
print(counter_check_distant(List1))

   