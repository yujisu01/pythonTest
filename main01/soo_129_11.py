>>> coun=['Salt','Pepsi','Coke']
>>> for i in coun:
...  for j in i:
...   print(j*2)
...
SS
aa
ll
tt
PP
ee
pp
ss
ii
CC
oo
kk
ee

>>> print(coun)
['Salt', 'Pepsi', 'Coke']
>>> for i in coun:
...  print(i*2)
...
SaltSalt
PepsiPepsi
CokeCoke
>>> print(coun)
['Salt', 'Pepsi', 'Coke']
>>> for i in coun:
...  print(i*2, end='')
...
SaltSaltPepsiPepsiCokeCoke>>> for j in i:
...  print(j, end='')
...
Coke>>>
>>> print(coun)
['Salt', 'Pepsi', 'Coke']
>>> for i in coun:
...  for j in i:
...   print(j*3, end='')
...
SSSaaallltttPPPeeepppsssiiiCCCoookkkeee>>>
