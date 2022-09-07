Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


# 파이썬 for문 입력시 들여쓰기 오류
# IndentationError: expected an indented block after 'for' statement on line 1
# 해당 오류 발생시, for문 아래 한칸 스페이스바 (들여쓰기) 해줘야 함
# print문 출력하려면, 엔터 쳐야됨

>>> a=100
>>> result=0
>>> for i in range(1,3):
... result =a>>i
  File "<stdin>", line 2
    result =a>>i
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in range(1,3):
...  result = a>> i
...  result = result+1
... print(result)
  File "<stdin>", line 4
    print(result)
    ^^^^^
SyntaxError: invalid syntax
>>>  print(result)
  File "<stdin>", line 1
    print(result)
IndentationError: unexpected indent
>>> print(result)
0
>>> for i in range(1,3):
...  result=a>>i
...  result=result+1
...  print(result)
... print(result)
  File "<stdin>", line 5
    print(result)
    ^^^^^
SyntaxError: invalid syntax
>>> a=100
>>> result=0
>>> for i in range(1,3):
...  result=a>>i
...  result=result+1
...
>>> print(result)
26
>>> 