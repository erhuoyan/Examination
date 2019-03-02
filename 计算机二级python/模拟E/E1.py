n = input("")
nums = n.split(",")
s = 0
for i in nums:
    s += eval(i)
print(s)