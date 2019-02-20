def gettxt():
    fr = open('天龙八部-网络版.txt','r',encoding='utf-8')
    txt = fr.read()
    fr.close()
    return txt

def txt_dic(txt):
    dic = {}
    for word in txt:
        dic[word] = dic.get(word,0) + 1
    del dic[' ']
    del dic['\n']
    return dic

def dic_to_list(dic):
    ls = []
    for key in dic:
        ls.append("{}:{}".format(key, dic[key]))
    return ls

def saveCSV(ls):
    fw = open("天龙八部-汉字统计.txt","w",encoding='utf-8')
    fw.write(",".join(ls))
    fw.close

def main():
    txt = gettxt()
    d = txt_dic(txt)
    ls = dic_to_list(d)
    saveCSV(ls)

main()