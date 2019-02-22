def getList(name):
    f = open(name+"-字符统计.txt","r",encoding="utf-8")
    words = f.read().split(',')
    for i in range(len(words)):
        words[i] = words[i].split(':')[0]
    f.close()
    return words

def main():
    fw = open('相同字符.txt','w',encoding='utf-8')
    ls1 = getList('命运')
    ls2 = getList('寻梦')
    ls3 = []
    for c in ls1:
        if c in ls2:
            ls3.append(c)
    fw.write(','.join(ls3))
    fw.close()
main()