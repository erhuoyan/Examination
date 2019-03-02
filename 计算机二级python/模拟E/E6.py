fr = open('SunSign.csv',"r",encoding='utf-8')
ls = []
for i in fr:
    ls.append(i.strip("\n").split(","))
fr.close()
n = input("请输入星座中文名称(例如，双子座):")
while n != '':
    flag = False
    for i in ls:
        if n == i[0]:
            print("{}座的生日位于{}-{}之间".format(chr(eval(i[-1])),i[1],i[2]))
            flag = True
            break
    if flag == False:
        print('输入星座名称有误！')
    n = input("请输入星座中文名称(例如，双子座):")
