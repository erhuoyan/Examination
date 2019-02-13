# CalHamlet.py
def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()                               # 全部字母转为小写
    for chr in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(chr, " ")                  # 将文本中特殊字符替换为空格
    return txt
hamletTxt = getText()
words = hamletTxt.split()                           # 返回列表，默认以空格分割  
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1           # word在counts中加1 word不在counts中返回0后加1
items = list(counts.items())                          # 返回counts所有键值对，转换为列表
items.sort(key = lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))