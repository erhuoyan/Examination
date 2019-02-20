def getInput():
    try:
        word = input()
        N = eval(word)
        if N != int(word):
            word = input()
    except:
        return getInput()# 可以是多行代码
    return N  # 只能是单行代码

print(getInput())