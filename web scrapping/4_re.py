import re

# abcd, book, desk
# ca?e
# care, cafe, case, cave

p = re.compile("ca.e")

# . (ca.e) : It means one word > care, cafe, case (0) | caffe (x)
# ^ (^de) : starting of word > desk, destination (0) | fade (x)
# $ (se$) : end of word > case, base (0) | face(x)


def print_match(m):
    if m:
        print(m.group())  # matching words return
        print(m.string)  # tested words return
        print(m.start())  # starting index of the word matching
        print(m.end())  # ending index of the word
        print(m.span())  # starting index and ending index of the matching word
    else:
        print("Not matching")


m = p.match("case")  # match: find the text if matching from the start of the word
print_match(m)
# print(m.group()) # if not matching, error

m = p.match("careless")
print_match(m)  # matching

m = p.search("good care")  # search: find if there is any matching

lst = p.findall("careless")  # findall : return list form of all matching word
print(lst)

# 1. p = re.compile(" what you want")
# 2. m= p.match("comapring word")
# 3. m= p.search("comparing word")
