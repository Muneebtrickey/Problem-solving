"""
Example 3: 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true, because all characters appear twice.
 Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
"""


def check_occurance(s):
    dic = {}
    check_set = set()

    for char in s:
        dic[char] = dic.get(char, 0) + 1
    

    for value in dic.values():
        check_set.add(value)

    return len(check_set) == 1


print(check_occurance('abacbc'))