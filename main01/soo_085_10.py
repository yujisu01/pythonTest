>>> a=list()
>>> for i in range(0,10):
...  a.append(i)
...
>>> for i in range(2,5):
...  a.remove(i)
...
>>> sum=0
>>> for i in range(len(a)):
...  sum+=a[i]
...
>>> print(sum)
36
>>>


