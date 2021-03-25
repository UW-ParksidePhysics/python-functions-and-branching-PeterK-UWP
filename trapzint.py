

from math import pi, cos, sin
print('Part a')

def trapzint1(f, a, b):
  T = ((b - a)/2) * (f(a) + f(b))
  return T

print('completed a')

print('Part b')  # 1 trap

f0 = [cos, 0, pi]
f1 = [sin, 0, pi]
f2 = [sin, 0, pi/2]
trap = []
functions = [f0, f1, f2]
for i in functions:
      trap.append(trapzint1(i[0], i[1], i[2]))
     
print(trap)


def integral():
  I = [
    0, 2, 1
  ]
  return I

def error_trap():
  error = []
  error_integral = integral()
  for i in range(0,3):
    error.append(error_integral[i] - trap[i])

  return error

print(error_trap())

print("should get, 0 2 1.78")

print('completed b')



print('Part c')  # 2 trap

def trapzint2(f, a, b):
  H1 = ((b/2. - a)/2.  * (f(a) + f(b/2.)))
  H2 = ((b - b/2.)/2.  * (f(b/2.) + f(b)))
  sumH = H1 + H2
  return sumH

def trap2():
  sumH = []
  for i in functions:
    sumH.append(trapzint2(i[0], i[1], i[2]))
  return sumH

print(trap2())
print('completed c')




print('Part d')  #n trap

n = 10
def trapzint3(f, a, b, n):
  for i in range(1, n+1):
    h = (b - a)/float(n)
    s = (f((a + i * h)) + f(a + i * h) + 1) / 2
    s *= h
  return s
      
 
 
def trapn():
  trap_n = []
  for i in functions:
    trap_n.append(trapzint3(i[0], i[1], i[2], i))
  return trap_n

print(trapn())
print('completed d')