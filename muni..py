a = [1,2,3]
b = [4 ,5,6]
zipped = zip(a,b)

# lets unzip 

c , d = zip(*zipped)
print(c)
print(d)