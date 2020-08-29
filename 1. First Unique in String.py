from collections import Counter

s = "loveleetcode"
counts = Counter(s)
# Hash Table 
# Counter({'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1})

# To return Index, using enumerate.
def FirstUniqueString(s):
    for index_, ch in enumerate(s):  #
        if counts[ch] == 1:
            return index_
    return -1


print(FirstUniqueString(s))
print(s[FirstUniqueString(s)])

print(FirstUniqueString(s))