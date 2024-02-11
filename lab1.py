def xk(c, d):
    if c==4:
        return 6
    elif d>=4:
        return 6+7+c
    else:
        return 25

def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothing")

def falling(n,k):
   if k==0:
      print(1)
   else:
      a=n
      for i in range(1,k):
         n*=a-i
      print(n)

def divisible_by_k(n,k):
   if n<k:
      print(0)
   else:
      a=k
      for i in range(1,n//k+1):
         k=a*i
         print(k)
      print(n//a)

def sum_digits(y):
   if y<=0:
      print(false)
   else:
      a=str(y)
      total=sum(int(char) for char in a)
      print(total)

def ab(c, d):
     if c > 5:
         print(c)
     elif c > 7:
         print(d)
     print('foo')

def bake(cake, make):
     if cake == 0:
         cake = cake + 1
         print(cake)
     if cake == 1:
         print(make)
     else:
         return cake
     return make

def double_eights(n):
   a=str(n)
   for i in range(len(a)):
      if a[i]=='8' and a[i+1]=='8':
         return True
   return False