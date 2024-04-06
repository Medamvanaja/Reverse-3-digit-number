n = int(input())
a = n // 100
b = (n % 100) // 10
c = (n % 10)
rev = c * 100 + b * 10 + a
print(rev)
