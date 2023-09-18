hashmap = {}
def countConstruct(words, target):
    if target in hashmap:
        return hashmap[target]
    if len(target)==0:
        return 1
    a = 0
    for x in words:
        if x==target[0:len(x)]:
            a += countConstruct(words, target[len(x):])
    hashmap[target] = a
    return hashmap[target]

# a = countConstruct(["abc", "ab", "c", "d", "e", "f", "cd","ef"], "abcdef")

a = countConstruct(["e", "ee", "eee","eeee", "eeeee", "eeeeee"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef")

print(a)