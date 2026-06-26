from collections import defaultdict

def nice_subarray(nums ,k):
    counts = defaultdict(int)
    counts[0] = 1

    ans = 0 
    curr = 0 

    for num in nums:
        curr += num % 2
        ans += counts[curr - k]
        counts[curr] += 1
    
    return ans

print(nice_subarray([1,1,2,1,1], 3))

"""
dry run the code : --------- [1,1,2,1,1]
counts = {
0 : 1,

}
ans = 0
curr = 0


step1 : num = 1
curr  = 1
ans = 0
counts = {
0: 1,
1 : 1}


step2 : num = 1
curr = 2
ans = 0

counts = {
0: 1,
1: 1,
2: 1}


step3: num = 2
 curr = 2
 ans = 0
 counts = {
 0: 1,
 1: 1,
 2: 2}


 step4: num = 1
curr = 3
ans = 1
counts = {
0: 1,
1: 1,
2: 2,
3: 1}


step5: num = 1
curr = 4
ans = 2
counts = {
0:1,]
1:1,
2:2,
3:1,
4:1}


"""