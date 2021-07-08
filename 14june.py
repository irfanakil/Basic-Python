sumeven = 0
for n in range(20, 31):
    if (n % 2 == 0):
        sumeven += n #sumeven= sumeven+n

print('sum of even no is :', sumeven)

import math
a=12
math.factorial(a)
print(a)

n = int(input('enter a no to calc factorial\n'))
a = 1
for x in range(1, n + 1):
    a *= x  # a= a*x

print('Factorial of {} is {}:'.format(n, a))
