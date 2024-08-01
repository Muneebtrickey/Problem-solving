# Approach 1


import random

List = ["muneeb","anees","jaish","imran","saad","saayid"]
index_list = []
while True:
    item = random.randint(0,len(List)-1)
    if item not in index_list:
        index_list.append(item)
    
    if len(index_list) == len(List):
        break

shuffle_list = []

for item in index_list:
    shuffle_list.append(List[item])

print("original list:", List)
print("shuffle_list", shuffle_list)




# approch 2


List2 = ["a","b","c","d","e","f"]
print("Original list: ", List2)
def shuffle(List2):
    length = len(List2)
    for i in range(length):
        j = random.randint(0,length-1)
        List2[i], List2[j] = List2[j], List2[i]
    
    return List2

print(shuffle(List2))