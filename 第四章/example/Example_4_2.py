# Example_4_2.py
import random
target = random.randint(1,1000)
count = 0
while True:
    try:
        guess = eval(input('请输入一个猜测的整数（1-1000）:'))
    except:
        print('输入有误，请重试，不计入猜测此数哦！')
        continue
    count = count + 1
    if guess > target:
        print("猜大了")
    elif guess < target:
        print("猜小了")
    else:
        print("猜对了")
        break
print("此论的猜测次数是:{}".format(count))