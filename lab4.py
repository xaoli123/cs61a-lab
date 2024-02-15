#Q2
def my_map(fn, seq):
   return [fn(x) for x in seq]

#Q3
def my_filter(pred, seq):
   return [x for x in seq if pred(x)]

#Q4
def my_reduce(combiner, seq):
   result=seq[0]
   for item in seq[1:]:
      result=combiner(result,item)
   return result

#Q5
def double_eights(n):
   a=str(n)
   for i in range(len(a)):
      if a[i]=='8' and a[i+1]=='8':
         return True
   return False

#Q6
def merge(lst1, lst2):
    ls=lst1+lst2
    lst=sorted(ls)
    return lst

#Q7
def summation(n, term):
   result=0
   for i in range(1,n+1):
      a=term(i)
      result+=a
   return result