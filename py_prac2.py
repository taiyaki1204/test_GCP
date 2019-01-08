TypeError: f() missing 1 required positional argument: 'n'

In [20]: f(s)                                                                                                   
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-20-9528d8b41b23> in <module>
----> 1 f(s)

NameError: name 's' is not defined

In [21]: f(5)                                                                                                   
Out[21]: 10

In [22]: f(879)                                                                                                 
Out[22]: 1758

In [23]: mod_5 = lambda x: x % 5                                       

In [24]: print('101 % 5 =' , mod_5(101) 
    ...: )                                                             
101 % 5 = 1

In [25]: help(mod_5)                                                   


In [26]: abs_diff = lambda a, b: abs(a-b)                              

In [27]: print("Absolute difference of 5 and 7 is", abs_diff(5, 7))    
Absolute difference of 5 and 7 is 2

In [28]: names = ['jacques', 'Ty', 'Mia', 'pui-wa']                    

In [29]: names                                                         
Out[29]: ['jacques', 'Ty', 'Mia', 'pui-wa']

In [30]: print("Longest name is:", max(names, key=lambda name: len(name
    ...: )))                                                           
Longest name is: jacques

In [31]:                                      
