#Q2
def insert_items(s, before, after):
    a=after
    b=before
    positions=[index for index,value in enumerate(s) if value == b]
    ls=positions
    for i in range(len(ls)):
        n=ls[i]
        s.insert(n+1+i,a)
    print(s)

#Q4
def count_occurrences(t, n, x):
    lst=list(t)
    ls=lst[:n+1]
    del lst[:n+1]
    a=ls.count(x)
    return a

#Q6
def partial_reverse(s, start):
    n=start
    before=s[:n]
    after=s[n:][::-1]
    s[:n]=before
    s[n:]=after
    print(s)