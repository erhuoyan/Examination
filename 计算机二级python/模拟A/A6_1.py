def frtxt():
    fr = open('论语-网络版.txt', 'r', encoding="utf-8")
    txt = fr.readlines()
    fr.close()
    return txt

def fwtxt(line):
    fw = open("论语-提取版.txt", 'w')
    fw.write(line)
    fw.close

def mdtxt(txt):
    wflag = False
    lines = ''
    for line in txt:
        if '【' in line:
            wflag = False
        if '【原文】' in line:
            wflag = True
            continue
        if line == "\n":
            continue
        if wflag == True:
            for i in range(0,25):
                for j in range(0,25):
                    line = line.replace("{}·{}".format(i,j),"**")
            for i in range(10):
                line = line.replace("{}*".format(i),"")
            for i in range(10):
                line = line.replace("*{}".format(i),"")
            line = line.replace("*","")
            lines = lines + line                
    return lines
oldtxt = frtxt()
newtxtline = mdtxt(oldtxt)
fwtxt(newtxtline)
