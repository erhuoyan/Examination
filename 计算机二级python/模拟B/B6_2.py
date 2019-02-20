import jieba
fr = open("天龙八部-网络版.txt","r",encoding="utf-8")
fw = open("天龙八部-词语统计.txt","w",encoding="utf-8")
txt = fr.read()
fr.close()
words = jieba.lcut(txt)
count = {}
for word in words:
    count[word] = count.get(word,0) + 1
del count[' ']
del count['\n']
ls = []
for key in count:
    ls.append("{}:{}".format(key,count[key]))
fw.write(",".join(ls))
fw.close()