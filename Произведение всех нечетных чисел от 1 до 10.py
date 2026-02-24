
#вариант 1
multipl = 1
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
               continue
    multipl *= a
print(f'{multipl}')
#вариант 2
multipl = 1
a = 0
for i in range(0,10):
    a += 1
    if a % 2 == 0:
        continue
    multipl *= a
print(f'{multipl}')