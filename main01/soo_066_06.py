Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Soo:
...  def fn(self,a,b):
...   self.a=9
...   self.b=b
...   print(a+self.b)
...
>>> a=Soo()
>>> a.fn(4,7)
11