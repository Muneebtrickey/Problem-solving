vowels = ["a","e","i","o","u","A","E","I","O","U"]
def checking_vowels(s):
    total_vowels = 0
    for vowel in vowels:
        if vowel in s:
            total_vowels += (s.count(vowel))
    
    return total_vowels




# approch 2

def checking_vowels_approch2(s):
    total_vowels = 0
    for character in s:
        if character in vowels:
            total_vowels += 1
    
    return total_vowels





s = "mynameismuneeb"

print(checking_vowels(s))
print(checking_vowels_approch2(s))





