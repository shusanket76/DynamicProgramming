def allConstruct(target, wordbank, hasmap={}):
    if target in hasmap:
        return hasmap[target][:]
    if len(target)==0:
        return [[]]
    allcon = []
    for x in wordbank:
        if x==target[0:len(x)]:
            a = allConstruct(target[len(x):], wordbank)
            if a is not None:
                for b in a:
                    b.insert(0, x)
                    allcon.append(b[:])
    hasmap[target]=allcon
    return allcon
# a = allConstruct("abcdef", ["ab", "abc","cd", "def", "abcd", "ef", "c"])
a = allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeer", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])

print(a)