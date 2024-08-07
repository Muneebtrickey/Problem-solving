# problem 

"""
our task is to find the factor in increasing order using the most efficent generator approch. 

"""


# finding the factor in increasing order

def factor(n):
    k = 1 
    pairs  = []
    while k * k < n:
        if n % k == 0:
            yield k
            pairs.append((n//k))
        
        k += 1
    
    if k * k == n:
        yield k 
        for item in reversed(pairs):
            yield item



print(list(factor(100)))
        
        