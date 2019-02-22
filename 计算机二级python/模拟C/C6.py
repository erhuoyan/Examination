import random
random.seed(0x1010)
p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
s = []
excludes = ''
while len(s) < 10:
    pwd = ''
    for i in range(10):
        pwd += p[random.randint(0, len(p)-1)]
    if pwd[0] in excludes:
        continue
    else:
        s.append(pwd)
        excludes += pwd[0]
fw = open("随机密码.txt","w")
fw.write("\n".join(s))
fw.close

print("\n".join(s))