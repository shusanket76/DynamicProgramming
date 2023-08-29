
def allConstruct(target, wordBank):
    res = []
    if len(target) == 0:
        return [[]]
    for x in wordBank:
        if x == target[:len(x)]:
            a = allConstruct(target[len(x):], wordBank)
            if a is not None:
                for b in a:
                    b.insert(0,x)
                    res.append(b)
    return res
a = allConstruct("purple",["purp","p","ur","le","purpl"])
print(a)