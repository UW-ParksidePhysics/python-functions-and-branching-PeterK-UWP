from math import pi, cos, sin

def trapzint1(f, a, b):
  T = ((b - a)/2) * (f(a) + f(b))
  return T
print('trapezoid test one')
print('----------------')
print(trapzint1(cos, 0 ,pi))
print(trapzint1(sin, 0, pi))
print(trapzint1(sin, 0, pi/2))
print('----------------')




def trapzint2(f, a, b):
  H1 = ((b/2 - a)/2  * (f(a) + f(b/2)))
  H2 = ((b - b/2)/2  * (f(b/2) + f(b)))
  sumH = H1 + H2
  return sumH

print('trapezoid test 2')
print('----------------')
print(trapzint2(cos, 0 ,pi))
print(trapzint2(sin, 0, pi))
print(trapzint2(sin, 0, pi/2))
print('----------------')


def trapzintn(f, a, b, n=10):
  h = (b - a)/float(n)
  A = h/2
  var = 0
  for i in range(0, n):
    xi = a + i * h
    var += f(xi) + f(xi + h)
    mult = A * var
    return mult
print(' trapezoid test n')
print('----------------')
print(f"{trapzintn(cos, 0, pi, 1000):.2f}")
print(f"{trapzintn(sin, 0, pi, 1000):.2f}")
print(f"{trapzintn(sin, 0, pi/2, 1000):.2f}")
print('----------------')

#test_trapzintn()



