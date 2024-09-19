# bad recursion 
#finding the element uniqueness

def unique3(S , start , stop):
    
    if stop - start <= 1:
        return True
    
    elif not unique3(S, start , stop-1):
        return False
    
    elif not unique3(S, start+1 , stop):
        return False
    
    else:
        return S[start] != S[stop-1]
    


List = [1,2,3,4,5]
start  = 0
stop = len(List)

print(unique3(List, start , stop))
