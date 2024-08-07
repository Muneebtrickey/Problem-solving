# creating generator to find the factors

def factor(n):
    k = 1
    while k * k < n:  # we need to iterate through the square root
        if  n % k == 0:
            yield k      # if n = 100 and k is 2 so 2 is a factor
            yield n // k  # and 100 // 2 == 50 which is also a factor
        
        k += 1
    
    if k * k == n:   # special case if the k is equal to the square root so yield the k.     

        yield k     
    


for factor in factor(100):
    print(factor)
