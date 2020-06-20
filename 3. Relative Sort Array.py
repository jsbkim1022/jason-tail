arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]

dict_ = {}
diff = []
num = 0
result = []
for i in arr1:
    if i not in arr2:
        diff.append(i)
diff.sort()
for i in arr2:
    dict_[i] = arr1.count(i)
print(dict_)

for i in range(len(arr2)):
    result.extend([arr2[i]] * dict_[arr2[i]])

result.extend(diff)
print(result)
