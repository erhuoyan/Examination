names = ['命运','寻梦']
for name in names :
    fr = open(name+"-网络版.txt","r",encoding="utf-8")
    fw = open(name+"-字符统计.txt","w",encoding="utf-8")
    txt = fr.read()
    d = {}
    for word in txt:
        d[word] = d.get(word,0) + 1
    del d['\n']
    ls = list(d.items())
    ls.sort(key = lambda x:x[1],reverse = True)
    for i in range(100):
        ls[i] = "{}:{}".format(ls[i][0],ls[i][1])
    fw.write(",".join(ls[:100]))
    fr.close()
    fw.close()