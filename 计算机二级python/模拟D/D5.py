a = [[1,2,3], [4,5,6], [7,8,9]]
b = [3,6,9]
s = 0
for c in a:
    for j in range(3):
        s += c[j] * b[j]
print(s)