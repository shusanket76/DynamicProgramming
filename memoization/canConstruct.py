hasmap = {}
def canConstruct(word, wordArr):
    if word in hasmap:
        return False
    if len(word)==0:
        return True
    for x in wordArr:
        if x==word[:len(x)]:
            a = canConstruct(word[len(x):], wordArr)
            if a is True:
                return True
    hasmap[word] = False
    return False


a = canConstruct("abcdef", ["ab","abcd","cd","def","abcd"])
b = canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee"])
print(b)