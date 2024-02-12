#Q4
def composer(f, g):
   return lambda x:f(g(x))
def g(x):
   return x + 1
def f(x):
   return x**2
def composite_identity(f, g):
   return lambda x:k(x)
def k(x):
   if f(g(x))==g(f(x)):
      return True
   else:
      return False
def h(x):
   return x*3
a1=composer(f, g)
a2=composer(h, a1)
a2=a2(5)
print(a2)
b1=composite_identity(f, g)
b1=b1(5)
print(b1)

#Q7
import math
def multiple(a,b):
   return a*b//math.gcd(a,b)