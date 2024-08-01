# 

#by using list comprehension we can construct the list like
# this


L = [i * (i-1) for i in range(1,11)]
print(L)





# another approach

List = [(i * (i + 1))//2 for i in range(10) ]


another_list = [2 * i for i in List]
print(another_list)