Jupyter Notebook
py_prac_day3
Current Kernel Logo
Python 3 
File
Edit
View
Insert
Cell
Kernel
Widgets
Help


3.0 == 3
True

'3' == 3
False

def is_odd(n):
    return (n % 2) == 1
​
print(is_odd(100))
print(is_odd(-1))
​
False
False

def is_odd(n):
    return (n % 2) == 1
​
print(is_odd(100))
print(is_odd(-1))
​
False
True

def inspect(x):
    if x == 0 :
        print(x, "is zero")
    elif x > 0 :
        print(x, "is positive")
    elif x < 0 :
        print(x, "is negative")
    else:
        print(x, "is not num")
        
inspect(0)
inspect(-17)
​
    
0 is zero
-17 is negative

bool(0)
bool(1)
bool()
bool(sadf)
​
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-479c14dec1c5> in <module>
      2 bool(1)
      3 bool()
----> 4 bool(sadf)

NameError: name 'sadf' is not defined


bool("sdf")
True

​

