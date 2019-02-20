N = input("请输入一个整数: ")

s = 0
for i in range(eval(N),eval(N)+100):
    if i % 2 != 0:
        s = s + i
print(s)# 可以是多行代码