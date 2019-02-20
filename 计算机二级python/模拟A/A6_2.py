def frtxt():
    fr = open('论语-提取版.txt', 'r')
    txt = fr.readlines()
    fr.close()
    return txt

def fwtxt(line):
    fw = open("论语-原文.txt", 'w')
    fw.write(line)
    fw.close

def mdtxt(txt):
    lines = ""
    for line in txt:
        for i in range(1,23):
            line = line.replace('({})'.format(i),"")
        lines = lines + line                
    return lines
oldtxt = frtxt()
newtxtline = mdtxt(oldtxt)
fwtxt(newtxtline)
