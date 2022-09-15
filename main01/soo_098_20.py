>>> def soo(num):
...  if num==0 or num==1:
...   return 1
...  return soo(num-2)+soo(num-1)
...
>>> for i in range(0,5):
...  print(soo(i),end='')
...
11235>>>
