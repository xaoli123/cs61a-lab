#Q1
def ordered_digits(x):
   a=str(x)
   for i in range(len(a)):
      if a[i]>a[i+1]:
         return False
         break
      return True

#Q3
def nearest_two(x):
   i=0
   if x>=2:
      while abs(x-2**i)>abs(2**(i+1)-x):
         i+=1
      return 2**i
   elif x<2:
      while abs(1/2**i-x)>abs(1/2**(i+1)-x):
         i+=1
      return 1/2**i

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1