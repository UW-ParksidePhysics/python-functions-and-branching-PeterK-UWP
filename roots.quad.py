

from numpy.lib.scimath import sqrt
def roots(a,b,c):
 x1 =(-b + (sqrt(4 * a * c)))/(2 * a)
 x2 =(-b - (sqrt(4 * a * c)))/(2 * a)
 return x1, x2


def test_roots_float():
  test_roots = roots(1, -6 ,4)
  print (type(test_roots[0]), type(test_roots[1])) 
  #organization float vs string
  print(test_roots)
  return

def test_roots_float1():
  test_roots = roots(-1, -6 ,4)
  print (type(test_roots[0]), type(test_roots[1])) 
  #organization float vs string
  print(test_roots)
  return

test_roots_float()
test_roots_float1()