Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[[1,1,0,1,0],[1,0,1,0]]
>>> tot,totsu=0,0
>>> for i in a:
...  for j in i:
...   tot+=j
...  totsu=totsu+len(i)
...
>>> print(totsu,tot)
9 5