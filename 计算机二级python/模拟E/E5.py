def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]
for i in ls.copy():
    if is_prime == True:
        ls.remove(i)
print(len(ls))