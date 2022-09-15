Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sum=0
>>> a=[1,2,3,4,5]
>>> b=[2,3,4,5,6]
>>> c=[x*y for x in a for y in b]
>>> for i in c[:7]:
...  sum+=i
...
>>> print(sum)
30