Jupyter Notebook
py_prac_day4
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


primes = [2,3,5,7]
​

ry
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

my_favourite_things = [32, 'raindrops on roses', help]

0
planets[0]
'Mercury'

planets[1]
'Venus'

planets[-1]
'Neptune'

2
planets[-2]
'Uranus'

planets[0:3]
['Mercury', 'Venus', 'Earth']

planets[:3]
['Mercury', 'Venus', 'Earth']

planets[0:]
planets[0:]
['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets[3:]
['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets[0]
'Mercury'

1
planets[1]
'Venus'

planets[-1:1]
[]

planets[1:-1]
['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']

3
planets[-3]
'Saturn'

3:
planets[-3:]
['Saturn', 'Uranus', 'Neptune']

planets[3] = 'Malacandra'
planets
['Mercury',
 'Venus',
 'Earth',
 'Malacandra',
 'Jupiter',
 'Saturn',
 'Uranus',
 'Neptune']

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# (Okay, that was rather silly. Let's give them back their old names)
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets
len(planets)
8

planets[]
  File "<ipython-input-23-655fd1bbf0fc>", line 1
    planets[]
            ^
SyntaxError: invalid syntax



planets
planets
['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets
sorted(planets)
['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']

planets.sorted()
planets.sorted()
​
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-26-3017bc78bd01> in <module>
----> 1 planets.sorted()

AttributeError: 'list' object has no attribute 'sorted'


planets.sort()

planets
​
['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']

primes = [2, 3, 5, 7]
sum(primes)
17

max(primes)
7

print(primes.max())
print(primes.max())
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-31-5185b355f47d> in <module>
----> 1 print(primes.max())

AttributeError: 'list' object has no attribute 'max'


print(primes.max
  File "<ipython-input-32-33946e05d712>", line 1
    print(primes.max
                    ^
SyntaxError: unexpected EOF while parsing



)
print(primes.max)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-33-86bef81fca88> in <module>
----> 1 print(primes.max)

AttributeError: 'list' object has no attribute 'max'



c = 12 + 3j

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)
0
3.0

x.bit_length()
4

planets.append('Pluto')

planets
​
['Earth',
 'Jupiter',
 'Mars',
 'Mercury',
 'Neptune',
 'Saturn',
 'Uranus',
 'Venus',
 'Pluto']

planets.pop()
'Pluto'

planets
​
['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']

planets.index('Earth')
0

ets
"Earth" in planets
True

planets
help(planets)
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


1,2,3
t ={1,2,3}

t
t
{1, 2, 3}

x = 0.125
x.as_integer_ratio()
x = 0.125
x.as_integer_ratio()
(1, 8)

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)
0.125

a = 1
b = 0
a, b = b, a
print(a, b)
0 1

​

