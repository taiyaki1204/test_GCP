Jupyter Notebook
py_prac_day5
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


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line
Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune 

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product
360

for mult in multiplicands
    print (mult)
  File "<ipython-input-3-cbda09e8bd84>", line 1
    for mult in multiplicands
                             ^
SyntaxError: invalid syntax



for mult in multiplicands:
    print (mult)
    
2
2
2
3
3
5

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')  
        
HELLO

test = 'osdGsd'

test.isupper()
False

for char in test:
    char

for char in test:
    print(char)
o
s
d
G
s
d

for i in range(5):
    print("Doing important work. i =", i)
Doing important work. i = 0
Doing important work. i = 1
Doing important work. i = 2
Doing important work. i = 3
Doing important work. i = 4

r = range(5)
r
range(0, 5)

help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop


list(range(5))
[0, 1, 2, 3, 4]

nums = [1, 2, 4, 8, 16]
for i in range(len(nums)):
    nums[i] = nums[i] * 2
nums
[2, 4, 8, 16, 32]

len(nums)
5

for i in nums:
    print(i)
2
4
8
16
32

def double_odds(nums):
    for i, num in enumerate(nums):
        if num % 2 == 1:
            nums[i] = num * 2
​
x = list(range(10))
double_odds(x)
x
[0, 2, 2, 6, 4, 10, 6, 14, 8, 18]

def test5(nums):
    for i, num in enumerate(nums):
        print(i)
        print(num)
test5(5)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-c07d326aa267> in <module>
      3         print(i)
      4         print(num)
----> 5 test5(5)

<ipython-input-2-c07d326aa267> in test5(nums)
      1 def test5(nums):
----> 2     for i, num in enumerate(nums):
      3         print(i)
      4         print(num)
      5 test5(5)

TypeError: 'int' object is not iterable


def test5(nums):
    for i, num in enumerate(nums):
        print(i)
        print(num)
x = list(range(5))
test5(x)
0
0
1
1
2
2
3
3
4
4

def test5(nums):
    for i, num in enumerate(nums):
        print(num)
x = list(range(5))
test5(x)
0
1
2
3
4

def double_odds(nums):
    for i, num in enumerate(nums):
        if num % 2 == 1:
            nums[i] = num * 2
            print(num)
            print(i)
​
x = list(range(10))
double_odds(x)
x
1
1
3
3
5
5
7
7
9
9
[0, 2, 2, 6, 4, 10, 6, 14, 8, 18]

help(x)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None


x.count()
​
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-22592ee537f4> in <module>
----> 1 x.count()

TypeError: count() takes exactly one argument (0 given)


count(x)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-bf52d2c870aa> in <module>
----> 1 count(x)

NameError: name 'count' is not defined


x.count
<function list.count(value, /)>

list(enumerate(['a', 'b']))
[(0, 'a'), (1, 'b')]

x = 0.125
numerator, denominator = x.as_integer_ratio()

​

numerator
1

denominator
8

help(as_integer_ratio())
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-14-53e430376d51> in <module>
----> 1 help(as_integer_ratio())

NameError: name 'as_integer_ratio' is not defined


help(as_integer_ratio)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-15-7ae25c8eb09d> in <module>
----> 1 help(as_integer_ratio)

NameError: name 'as_integer_ratio' is not defined


help(x)
Help on float object:

class float(object)
 |  float(x=0, /)
 |  
 |  Convert a string or number to a floating point number, if possible.
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Formats the float according to format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __round__(self, ndigits=None, /)
 |      Return the Integral closest to x, rounding half toward even.
 |      
 |      When an argument is passed, work like built-in round(x, ndigits).
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(self, /)
 |      Return the Integral closest to x between 0 and x.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original float
 |      and with a positive denominator.
 |      
 |      Raise OverflowError on infinities and a ValueError on NaNs.
 |      
 |      >>> (10.0).as_integer_ratio()
 |      (10, 1)
 |      >>> (0.0).as_integer_ratio()
 |      (0, 1)
 |      >>> (-.25).as_integer_ratio()
 |      (-1, 4)
 |  
 |  conjugate(self, /)
 |      Return self, the complex conjugate of any float.
 |  
 |  hex(self, /)
 |      Return a hexadecimal representation of a floating-point number.
 |      
 |      >>> (-0.1).hex()
 |      '-0x1.999999999999ap-4'
 |      >>> 3.14159.hex()
 |      '0x1.921f9f01b866ep+1'
 |  
 |  is_integer(self, /)
 |      Return True if the float is an integer.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __getformat__(typestr, /) from builtins.type
 |      You probably don't want to use this function.
 |      
 |        typestr
 |          Must be 'double' or 'float'.
 |      
 |      It exists mainly to be used in Python's test suite.
 |      
 |      This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
 |      little-endian' best describes the format of floating point numbers used by the
 |      C type named by typestr.
 |  
 |  __set_format__(typestr, fmt, /) from builtins.type
 |      You probably don't want to use this function.
 |      
 |        typestr
 |          Must be 'double' or 'float'.
 |        fmt
 |          Must be one of 'unknown', 'IEEE, big-endian' or 'IEEE, little-endian',
 |          and in addition can only be one of the latter two if it appears to
 |          match the underlying C reality.
 |      
 |      It exists mainly to be used in Python's test suite.
 |      
 |      Override the automatic determination of C-level floating point type.
 |      This affects how floats are converted to and from binary strings.
 |  
 |  fromhex(string, /) from builtins.type
 |      Create a floating-point number from a hexadecimal string.
 |      
 |      >>> float.fromhex('0x1.ffffp10')
 |      2047.984375
 |      >>> float.fromhex('-0x1p-1074')
 |      -5e-324
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  real
 |      the real part of a complex number


x__trunc__
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-17-ce516928ade4> in <module>
----> 1 x__trunc__

NameError: name 'x__trunc__' is not defined


x.__trunc__
<function float.__trunc__()>

x.as_integer_ratio()
(1, 8)

nums = [
    ('one', 1, 'I'),
    ('two', 2, 'II'),
    ('three', 3, 'III'),
    ('four', 4, 'IV'),
]

for word, integer, roman_numeral in nums:
    print(integer, word, roman_numeral, sep=' = ', end='; ')
1 = one = I; 2 = two = II; 3 = three = III; 4 = four = IV; 

print(回答する)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-22-42d7adec9065> in <module>
----> 1 print(回答する)

NameError: name '回答する' is not defined


for tup in nums:
    word = tup[0]
    integer = tup[1]
    roman_numeral = tup[2]
    print(integer, word, roman_numeral, sep=' = ', end='; ')
1 = one = I; 2 = two = II; 3 = three = III; 4 = four = IV; 

help(tup)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.


i = 0
while i < 10:
    print(i, end=' ')
    i += 1
0 1 2 3 4 5 6 7 8 9 

while i < 10:
    print(i,end=' ')
    i += 1

i=5
while i < 10:
    print(i,end=' ')
    i += 1
5 6 7 8 9 

squares = [n**2 for n in range(10)]
squares
​
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

​

squares = []
for n in range(10):
    squares.append(n**2)
squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

help(squares)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None


short_planets = [planet for planet in planets if len(planet) < 6]
short_planets
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-31-86cb4150ea67> in <module>
----> 1 short_planets = [planet for planet in planets if len(planet) < 6]
      2 short_planets

NameError: name 'planets' is not defined


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line
Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune 

short_planets = [planet for planet in planets if len(planet) < 6]
short_planets
['Venus', 'Earth', 'Mars']

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets
['VENUS!', 'EARTH!', 'MARS!']

[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]
['VENUS!', 'EARTH!', 'MARS!']

[32 for planet in planets]
[32, 32, 32, 32, 32, 32, 32, 32]

def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

def count_negatives(nums):
    return len([num for num in nums if num < 0])

[32 for planet in planets]
[32, 32, 32, 32, 32, 32, 32, 32]

def count_negatives(nums):
    # Reminder: in the day 3 exercise we learned about a quirk of Python where it calculates
    # something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])

​

