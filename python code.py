Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> print ("Hello World")
Hello World
>>> a="Hello"
>>> b=" World"
>>> print (a + b)
Hello World
>>> a ="Goodbye"
>>> print (a + b)
Goodbye World
>>> a = "abc123"
>>> print (a)
abc123
>>> type (a)
<class 'str'>
>>> b=2
>>> print (a+b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print (a+b)
TypeError: can only concatenate str (not "int") to str
>>> type (a)
<class 'str'>
>>> a = 1
>>> b=2
>>> print (a+b)
3
>>> a=2.5
>>> type(a)
<class 'float'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a=true
NameError: name 'true' is not defined
>>> a=True
>>> a=False
>>> 
>>> not a
True
>>> a=True
>>> not a
False
>>> type
<class 'type'>
>>> type (a)
<class 'bool'>
>>> a=2.0
>>> type (a)
<class 'float'>
>>> a=int(a)
>>> type(a)
<class 'int'>
>>> print (a)
2
>>> a= 2.5
>>> a=int (a)
>>> print (a)
2
>>> 
>>> 
>>> a="1"
>>> b=2
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(a+b)
TypeError: can only concatenate str (not "int") to str
>>> 
>>> 
>>> numberOfScores = input("Please enter the number of scores you want to average: ")
Please enter the number of scores you want to average: 