hashmap = {}
def allConstruct(words, target):
    if target in hashmap:
        return hashmap[target]
    if len(target)==0:
        return [[]]
    result  =[]
    for x in words:
        if x == target[0:len(x)]:
            a = allConstruct(words, target[len(x):])
            if len(a)>=1:
                for y in a:
                    y.insert(0,x)
                    result.append(y)
    hashmap[target] = result
    return hashmap[target]

a = allConstruct(["abc", "ab", "c", "d", "e", "f", "cd","ef"], "abcdef")

# a = allConstruct(["e", "ee", "eee","eeee", "eeeee", "eeeeeef"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef")

print(a)