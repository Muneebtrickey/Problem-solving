# list = [0,2,6,12,20,30,42,56,72,90]

#by using list comprehension we can construct the list like
# this

List = [i * (i-1) for i in range(1,11)]
print(List)