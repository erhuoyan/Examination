fo = open('SunSign.csv','r',encoding='utf-8')
ls = []
for i in fo:
    ls.append(i.strip('\n').split(','))
fo.close()

while True:
    n = input()
    flag = False
    if n == 'exit':
        break
    for line in ls:
        if line[0]==n:
            print("{}座的生日位于{}-{}之间。".format(chr(eval(line[3])),line[1],line[2]))
            flag = True
    if flag == False:
        print("输入星座名称有误！")
