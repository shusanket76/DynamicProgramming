res=[0]
def countConstruct(target, wordArr):
    if len(target)==0:
        res[0]=res[0]+1
        return 

    for x in wordArr:
        if x == wordArr[:len(x)]:
            countConstruct(target[:len(x)], wordArr)
    print(res)


a = countConstruct("abcdef", ["ab","abc","cd","def","abcd"])
print(a)