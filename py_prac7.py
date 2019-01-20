Jupyter Notebook
py_prac_day7
(autosaved)
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


import math

print("It's math! It has type {}".format(type(math)))
import math
​
print("It's math! It has type {}".format(type(math)))
It's math! It has type <class 'module'>

print(dir(math))
print(dir(math))
​
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-d121256e9997> in <module>
----> 1 print(dir(math))

NameError: name 'math' is not defined


import math
​
print("It's math! It has type {}".format(type(math)))
​
It's math! It has type <class 'module'>

print(dir(math))
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

print("pi to 4 significant digits = {:.4}".format(math.pi))
pi to 4 significant digits = 3.142

math.log(32, 2)
5.0

help(math.log)
Help on built-in function log in module math:

log(...)
    log(x, [base=math.e])
    Return the logarithm of x to the given base.
    
    If the base not specified, returns the natural logarithm (base e) of x.


help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(x, y, /)
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)



import math as mt
mt.pi
3.141592653589793

import math
mt = math

from math import *
print(pi, log(32, 2))
3.141592653589793 5.0

from math import *
from numpy import *
print(pi, log(32, 2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-5045b296ad83> in <module>
      1 from math import *
      2 from numpy import *
----> 3 print(pi, log(32, 2))

TypeError: return arrays must be of ArrayType


from math import log, pi
from numpy import asarray

import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )
numpy.random is a <class 'module'>
it contains names such as... ['set_state', 'shuffle', 'standard_cauchy', 'standard_exponential', 'standard_gamma', 'standard_normal', 'standard_t', 'test', 'triangular', 'uniform', 'vonmises', 'wald', 'warnings', 'weibull', 'zipf']

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
rolls
array([4, 1, 5, 5, 4, 2, 4, 3, 4, 4])

type(rolls)
numpy.ndarray

print(dir(rolls))
['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__', '__array_interface__', '__array_prepare__', '__array_priority__', '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__complex__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__', 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'ctypes', 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten', 'getfield', 'imag', 'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']

#
#type() (what is this thing?)
# dir() (what can I do with it?)

# What am I trying to do with this dice roll data? Maybe I want the average roll, in which case the "mean"
# method looks promising...
rolls.mean()
3.6

# Or maybe I just want to get back on familiar ground, in which case I might want to check out "tolist"
rolls.tolist()
[4, 1, 5, 5, 4, 2, 4, 3, 4, 4]

#
#3: help() (tell me more)

# That "ravel" attribute sounds interesting. I'm a big classical music fan.
help(rolls.ravel)
Help on built-in function ravel:

ravel(...) method of numpy.ndarray instance
    a.ravel([order])
    
    Return a flattened array.
    
    Refer to `numpy.ravel` for full documentation.
    
    See Also
    --------
    numpy.ravel : equivalent function
    
    ndarray.flat : a flat iterator on the array.


# Okay, just tell me everything there is to know about numpy.ndarray
# (Click the "output" button to see the novel-length output)
help(rolls)
Help on ndarray object:

class ndarray(builtins.object)
 |  ndarray(shape, dtype=float, buffer=None, offset=0,
 |          strides=None, order=None)
 |  
 |  An array object represents a multidimensional, homogeneous array
 |  of fixed-size items.  An associated data-type object describes the
 |  format of each element in the array (its byte-order, how many bytes it
 |  occupies in memory, whether it is an integer, a floating point number,
 |  or something else, etc.)
 |  
 |  Arrays should be constructed using `array`, `zeros` or `empty` (refer
 |  to the See Also section below).  The parameters given here refer to
 |  a low-level method (`ndarray(...)`) for instantiating an array.
 |  
 |  For more information, refer to the `numpy` module and examine the
 |  methods and attributes of an array.
 |  
 |  Parameters
 |  ----------
 |  (for the __new__ method; see Notes below)
 |  
 |  shape : tuple of ints
 |      Shape of created array.
 |  dtype : data-type, optional
 |      Any object that can be interpreted as a numpy data type.
 |  buffer : object exposing buffer interface, optional
 |      Used to fill the array with data.
 |  offset : int, optional
 |      Offset of array data in buffer.
 |  strides : tuple of ints, optional
 |      Strides of data in memory.
 |  order : {'C', 'F'}, optional
 |      Row-major (C-style) or column-major (Fortran-style) order.
 |  
 |  Attributes
 |  ----------
 |  T : ndarray
 |      Transpose of the array.
 |  data : buffer
 |      The array's elements, in memory.
 |  dtype : dtype object
 |      Describes the format of the elements in the array.
 |  flags : dict
 |      Dictionary containing information related to memory use, e.g.,
 |      'C_CONTIGUOUS', 'OWNDATA', 'WRITEABLE', etc.
 |  flat : numpy.flatiter object
 |      Flattened version of the array as an iterator.  The iterator
 |      allows assignments, e.g., ``x.flat = 3`` (See `ndarray.flat` for
 |      assignment examples; TODO).
 |  imag : ndarray
 |      Imaginary part of the array.
 |  real : ndarray
 |      Real part of the array.
 |  size : int
 |      Number of elements in the array.
 |  itemsize : int
 |      The memory use of each array element in bytes.
 |  nbytes : int
 |      The total number of bytes required to store the array data,
 |      i.e., ``itemsize * size``.
 |  ndim : int
 |      The array's number of dimensions.
 |  shape : tuple of ints
 |      Shape of the array.
 |  strides : tuple of ints
 |      The step-size required to move from one element to the next in
 |      memory. For example, a contiguous ``(3, 4)`` array of type
 |      ``int16`` in C-order has strides ``(8, 2)``.  This implies that
 |      to move from element to element in memory requires jumps of 2 bytes.
 |      To move from row-to-row, one needs to jump 8 bytes at a time
 |      (``2 * 4``).
 |  ctypes : ctypes object
 |      Class containing properties of the array needed for interaction
 |      with ctypes.
 |  base : ndarray
 |      If the array is a view into another array, that array is its `base`
 |      (unless that array is also a view).  The `base` array is where the
 |      array data is actually stored.
 |  
 |  See Also
 |  --------
 |  array : Construct an array.
 |  zeros : Create an array, each element of which is zero.
 |  empty : Create an array, but leave its allocated memory unchanged (i.e.,
 |          it contains "garbage").
 |  dtype : Create a data-type.
 |  
 |  Notes
 |  -----
 |  There are two modes of creating an array using ``__new__``:
 |  
 |  1. If `buffer` is None, then only `shape`, `dtype`, and `order`
 |     are used.
 |  2. If `buffer` is an object exposing the buffer interface, then
 |     all keywords are interpreted.
 |  
 |  No ``__init__`` method is needed because the array is fully initialized
 |  after the ``__new__`` method.
 |  
 |  Examples
 |  --------
 |  These examples illustrate the low-level `ndarray` constructor.  Refer
 |  to the `See Also` section above for easier ways of constructing an
 |  ndarray.
 |  
 |  First mode, `buffer` is None:
 |  
 |  >>> np.ndarray(shape=(2,2), dtype=float, order='F')
 |  array([[ -1.13698227e+002,   4.25087011e-303],
 |         [  2.88528414e-306,   3.27025015e-309]])         #random
 |  
 |  Second mode:
 |  
 |  >>> np.ndarray((2,), buffer=np.array([1,2,3]),
 |  ...            offset=np.int_().itemsize,
 |  ...            dtype=int) # offset = 1*itemsize, i.e. skip first element
 |  array([2, 3])
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __array__(...)
 |      a.__array__(|dtype) -> reference if type unchanged, copy otherwise.
 |      
 |      Returns either a new reference to self if dtype is not given or a new array
 |      of provided data type if dtype is different from the current dtype of the
 |      array.
 |  
 |  __array_prepare__(...)
 |      a.__array_prepare__(obj) -> Object of same type as ndarray object obj.
 |  
 |  __array_ufunc__(...)
 |  
 |  __array_wrap__(...)
 |      a.__array_wrap__(obj) -> Object of same type as ndarray object a.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __complex__(...)
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __copy__(...)
 |      a.__copy__()
 |      
 |      Used if :func:`copy.copy` is called on an array. Returns a copy of the array.
 |      
 |      Equivalent to ``a.copy(order='K')``.
 |  
 |  __deepcopy__(...)
 |      a.__deepcopy__(memo, /) -> Deep copy of array.
 |      
 |      Used if :func:`copy.deepcopy` is called on an array.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
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
 |  __format__(...)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Return self+=value.
 |  
 |  __iand__(self, value, /)
 |      Return self&=value.
 |  
 |  __ifloordiv__(self, value, /)
 |      Return self//=value.
 |  
 |  __ilshift__(self, value, /)
 |      Return self<<=value.
 |  
 |  __imatmul__(self, value, /)
 |      Return self@=value.
 |  
 |  __imod__(self, value, /)
 |      Return self%=value.
 |  
 |  __imul__(self, value, /)
 |      Return self*=value.
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __ior__(self, value, /)
 |      Return self|=value.
 |  
 |  __ipow__(self, value, /)
 |      Return self**=value.
 |  
 |  __irshift__(self, value, /)
 |      Return self>>=value.
 |  
 |  __isub__(self, value, /)
 |      Return self-=value.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __itruediv__(self, value, /)
 |      Return self/=value.
 |  
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __matmul__(self, value, /)
 |      Return self@value.
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
 |  __or__(self, value, /)
 |      Return self|value.
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
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __reduce__(...)
 |      a.__reduce__()
 |      
 |      For pickling.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmatmul__(self, value, /)
 |      Return value@self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __setstate__(...)
 |      a.__setstate__(state, /)
 |      
 |      For unpickling.
 |      
 |      The `state` argument must be a sequence that contains the following
 |      elements:
 |      
 |      Parameters
 |      ----------
 |      version : int
 |          optional pickle version. If omitted defaults to 0.
 |      shape : tuple
 |      dtype : data-type
 |      isFortran : bool
 |      rawdata : string or list
 |          a binary string with the data (or a list if 'a' is an object array)
 |  
 |  __sizeof__(...)
 |      Size of object in memory, in bytes.
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
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  all(...)
 |      a.all(axis=None, out=None, keepdims=False)
 |      
 |      Returns True if all elements evaluate to True.
 |      
 |      Refer to `numpy.all` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.all : equivalent function
 |  
 |  any(...)
 |      a.any(axis=None, out=None, keepdims=False)
 |      
 |      Returns True if any of the elements of `a` evaluate to True.
 |      
 |      Refer to `numpy.any` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.any : equivalent function
 |  
 |  argmax(...)
 |      a.argmax(axis=None, out=None)
 |      
 |      Return indices of the maximum values along the given axis.
 |      
 |      Refer to `numpy.argmax` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.argmax : equivalent function
 |  
 |  argmin(...)
 |      a.argmin(axis=None, out=None)
 |      
 |      Return indices of the minimum values along the given axis of `a`.
 |      
 |      Refer to `numpy.argmin` for detailed documentation.
 |      
 |      See Also
 |      --------
 |      numpy.argmin : equivalent function
 |  
 |  argpartition(...)
 |      a.argpartition(kth, axis=-1, kind='introselect', order=None)
 |      
 |      Returns the indices that would partition this array.
 |      
 |      Refer to `numpy.argpartition` for full documentation.
 |      
 |      .. versionadded:: 1.8.0
 |      
 |      See Also
 |      --------
 |      numpy.argpartition : equivalent function
 |  
 |  argsort(...)
 |      a.argsort(axis=-1, kind='quicksort', order=None)
 |      
 |      Returns the indices that would sort this array.
 |      
 |      Refer to `numpy.argsort` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.argsort : equivalent function
 |  
 |  astype(...)
 |      a.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)
 |      
 |      Copy of the array, cast to a specified type.
 |      
 |      Parameters
 |      ----------
 |      dtype : str or dtype
 |          Typecode or data-type to which the array is cast.
 |      order : {'C', 'F', 'A', 'K'}, optional
 |          Controls the memory layout order of the result.
 |          'C' means C order, 'F' means Fortran order, 'A'
 |          means 'F' order if all the arrays are Fortran contiguous,
 |          'C' order otherwise, and 'K' means as close to the
 |          order the array elements appear in memory as possible.
 |          Default is 'K'.
 |      casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
 |          Controls what kind of data casting may occur. Defaults to 'unsafe'
 |          for backwards compatibility.
 |      
 |            * 'no' means the data types should not be cast at all.
 |            * 'equiv' means only byte-order changes are allowed.
 |            * 'safe' means only casts which can preserve values are allowed.
 |            * 'same_kind' means only safe casts or casts within a kind,
 |              like float64 to float32, are allowed.
 |            * 'unsafe' means any data conversions may be done.
 |      subok : bool, optional
 |          If True, then sub-classes will be passed-through (default), otherwise
 |          the returned array will be forced to be a base-class array.
 |      copy : bool, optional
 |          By default, astype always returns a newly allocated array. If this
 |          is set to false, and the `dtype`, `order`, and `subok`
 |          requirements are satisfied, the input array is returned instead
 |          of a copy.
 |      
 |      Returns
 |      -------
 |      arr_t : ndarray
 |          Unless `copy` is False and the other conditions for returning the input
 |          array are satisfied (see description for `copy` input parameter), `arr_t`
 |          is a new array of the same shape as the input array, with dtype, order
 |          given by `dtype`, `order`.
 |      
 |      Notes
 |      -----
 |      Starting in NumPy 1.9, astype method now returns an error if the string
 |      dtype to cast to is not long enough in 'safe' casting mode to hold the max
 |      value of integer/float array that is being casted. Previously the casting
 |      was allowed even if the result was truncated.
 |      
 |      Raises
 |      ------
 |      ComplexWarning
 |          When casting from complex to float or int. To avoid this,
 |          one should use ``a.real.astype(t)``.
 |      
 |      Examples
 |      --------
 |      >>> x = np.array([1, 2, 2.5])
 |      >>> x
 |      array([ 1. ,  2. ,  2.5])
 |      
 |      >>> x.astype(int)
 |      array([1, 2, 2])
 |  
 |  byteswap(...)
 |      a.byteswap(inplace=False)
 |      
 |      Swap the bytes of the array elements
 |      
 |      Toggle between low-endian and big-endian data representation by
 |      returning a byteswapped array, optionally swapped in-place.
 |      
 |      Parameters
 |      ----------
 |      inplace : bool, optional
 |          If ``True``, swap bytes in-place, default is ``False``.
 |      
 |      Returns
 |      -------
 |      out : ndarray
 |          The byteswapped array. If `inplace` is ``True``, this is
 |          a view to self.
 |      
 |      Examples
 |      --------
 |      >>> A = np.array([1, 256, 8755], dtype=np.int16)
 |      >>> map(hex, A)
 |      ['0x1', '0x100', '0x2233']
 |      >>> A.byteswap(inplace=True)
 |      array([  256,     1, 13090], dtype=int16)
 |      >>> map(hex, A)
 |      ['0x100', '0x1', '0x3322']
 |      
 |      Arrays of strings are not swapped
 |      
 |      >>> A = np.array(['ceg', 'fac'])
 |      >>> A.byteswap()
 |      array(['ceg', 'fac'],
 |            dtype='|S3')
 |  
 |  choose(...)
 |      a.choose(choices, out=None, mode='raise')
 |      
 |      Use an index array to construct a new array from a set of choices.
 |      
 |      Refer to `numpy.choose` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.choose : equivalent function
 |  
 |  clip(...)
 |      a.clip(min=None, max=None, out=None)
 |      
 |      Return an array whose values are limited to ``[min, max]``.
 |      One of max or min must be given.
 |      
 |      Refer to `numpy.clip` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.clip : equivalent function
 |  
 |  compress(...)
 |      a.compress(condition, axis=None, out=None)
 |      
 |      Return selected slices of this array along given axis.
 |      
 |      Refer to `numpy.compress` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.compress : equivalent function
 |  
 |  conj(...)
 |      a.conj()
 |      
 |      Complex-conjugate all elements.
 |      
 |      Refer to `numpy.conjugate` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.conjugate : equivalent function
 |  
 |  conjugate(...)
 |      a.conjugate()
 |      
 |      Return the complex conjugate, element-wise.
 |      
 |      Refer to `numpy.conjugate` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.conjugate : equivalent function
 |  
 |  copy(...)
 |      a.copy(order='C')
 |      
 |      Return a copy of the array.
 |      
 |      Parameters
 |      ----------
 |      order : {'C', 'F', 'A', 'K'}, optional
 |          Controls the memory layout of the copy. 'C' means C-order,
 |          'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,
 |          'C' otherwise. 'K' means match the layout of `a` as closely
 |          as possible. (Note that this function and :func:`numpy.copy` are very
 |          similar, but have different default values for their order=
 |          arguments.)
 |      
 |      See also
 |      --------
 |      numpy.copy
 |      numpy.copyto
 |      
 |      Examples
 |      --------
 |      >>> x = np.array([[1,2,3],[4,5,6]], order='F')
 |      
 |      >>> y = x.copy()
 |      
 |      >>> x.fill(0)
 |      
 |      >>> x
 |      array([[0, 0, 0],
 |             [0, 0, 0]])
 |      
 |      >>> y
 |      array([[1, 2, 3],
 |             [4, 5, 6]])
 |      
 |      >>> y.flags['C_CONTIGUOUS']
 |      True
 |  
 |  cumprod(...)
 |      a.cumprod(axis=None, dtype=None, out=None)
 |      
 |      Return the cumulative product of the elements along the given axis.
 |      
 |      Refer to `numpy.cumprod` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.cumprod : equivalent function
 |  
 |  cumsum(...)
 |      a.cumsum(axis=None, dtype=None, out=None)
 |      
 |      Return the cumulative sum of the elements along the given axis.
 |      
 |      Refer to `numpy.cumsum` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.cumsum : equivalent function
 |  
 |  diagonal(...)
 |      a.diagonal(offset=0, axis1=0, axis2=1)
 |      
 |      Return specified diagonals. In NumPy 1.9 the returned array is a
 |      read-only view instead of a copy as in previous NumPy versions.  In
 |      a future version the read-only restriction will be removed.
 |      
 |      Refer to :func:`numpy.diagonal` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.diagonal : equivalent function
 |  
 |  dot(...)
 |      a.dot(b, out=None)
 |      
 |      Dot product of two arrays.
 |      
 |      Refer to `numpy.dot` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.dot : equivalent function
 |      
 |      Examples
 |      --------
 |      >>> a = np.eye(2)
 |      >>> b = np.ones((2, 2)) * 2
 |      >>> a.dot(b)
 |      array([[ 2.,  2.],
 |             [ 2.,  2.]])
 |      
 |      This array method can be conveniently chained:
 |      
 |      >>> a.dot(b).dot(b)
 |      array([[ 8.,  8.],
 |             [ 8.,  8.]])
 |  
 |  dump(...)
 |      a.dump(file)
 |      
 |      Dump a pickle of the array to the specified file.
 |      The array can be read back with pickle.load or numpy.load.
 |      
 |      Parameters
 |      ----------
 |      file : str
 |          A string naming the dump file.
 |  
 |  dumps(...)
 |      a.dumps()
 |      
 |      Returns the pickle of the array as a string.
 |      pickle.loads or numpy.loads will convert the string back to an array.
 |      
 |      Parameters
 |      ----------
 |      None
 |  
 |  fill(...)
 |      a.fill(value)
 |      
 |      Fill the array with a scalar value.
 |      
 |      Parameters
 |      ----------
 |      value : scalar
 |          All elements of `a` will be assigned this value.
 |      
 |      Examples
 |      --------
 |      >>> a = np.array([1, 2])
 |      >>> a.fill(0)
 |      >>> a
 |      array([0, 0])
 |      >>> a = np.empty(2)
 |      >>> a.fill(1)
 |      >>> a
 |      array([ 1.,  1.])
 |  
 |  flatten(...)
 |      a.flatten(order='C')
 |      
 |      Return a copy of the array collapsed into one dimension.
 |      
 |      Parameters
 |      ----------
 |      order : {'C', 'F', 'A', 'K'}, optional
 |          'C' means to flatten in row-major (C-style) order.
 |          'F' means to flatten in column-major (Fortran-
 |          style) order. 'A' means to flatten in column-major
 |          order if `a` is Fortran *contiguous* in memory,
 |          row-major order otherwise. 'K' means to flatten
 |          `a` in the order the elements occur in memory.
 |          The default is 'C'.
 |      
 |      Returns
 |      -------
 |      y : ndarray
 |          A copy of the input array, flattened to one dimension.
 |      
 |      See Also
 |      --------
 |      ravel : Return a flattened array.
 |      flat : A 1-D flat iterator over the array.
 |      
 |      Examples
 |      --------
 |      >>> a = np.array([[1,2], [3,4]])
 |      >>> a.flatten()
 |      array([1, 2, 3, 4])
 |      >>> a.flatten('F')
 |      array([1, 3, 2, 4])
 |  
 |  getfield(...)
 |      a.getfield(dtype, offset=0)
 |      
 |      Returns a field of the given array as a certain type.
 |      
 |      A field is a view of the array data with a given data-type. The values in
 |      the view are determined by the given type and the offset into the current
 |      array in bytes. The offset needs to be such that the view dtype fits in the
 |      array dtype; for example an array of dtype complex128 has 16-byte elements.
 |      If taking a view with a 32-bit integer (4 bytes), the offset needs to be
 |      between 0 and 12 bytes.
 |      
 |      Parameters
 |      ----------
 |      dtype : str or dtype
 |          The data type of the view. The dtype size of the view can not be larger
 |          than that of the array itself.
 |      offset : int
 |          Number of bytes to skip before beginning the element view.
 |      
 |      Examples
 |      --------
 |      >>> x = np.diag([1.+1.j]*2)
 |      >>> x[1, 1] = 2 + 4.j
 |      >>> x
 |      array([[ 1.+1.j,  0.+0.j],
 |             [ 0.+0.j,  2.+4.j]])
 |      >>> x.getfield(np.float64)
 |      array([[ 1.,  0.],
 |             [ 0.,  2.]])
 |      
 |      By choosing an offset of 8 bytes we can select the complex part of the
 |      array for our view:
 |      
 |      >>> x.getfield(np.float64, offset=8)
 |      array([[ 1.,  0.],
 |         [ 0.,  4.]])
 |  
 |  item(...)
 |      a.item(*args)
 |      
 |      Copy an element of an array to a standard Python scalar and return it.
 |      
 |      Parameters
 |      ----------
 |      \*args : Arguments (variable number and type)
 |      
 |          * none: in this case, the method only works for arrays
 |            with one element (`a.size == 1`), which element is
 |            copied into a standard Python scalar object and returned.
 |      
 |          * int_type: this argument is interpreted as a flat index into
 |            the array, specifying which element to copy and return.
 |      
 |          * tuple of int_types: functions as does a single int_type argument,
 |            except that the argument is interpreted as an nd-index into the
 |            array.
 |      
 |      Returns
 |      -------
 |      z : Standard Python scalar object
 |          A copy of the specified element of the array as a suitable
 |          Python scalar
 |      
 |      Notes
 |      -----
 |      When the data type of `a` is longdouble or clongdouble, item() returns
 |      a scalar array object because there is no available Python scalar that
 |      would not lose information. Void arrays return a buffer object for item(),
 |      unless fields are defined, in which case a tuple is returned.
 |      
 |      `item` is very similar to a[args], except, instead of an array scalar,
 |      a standard Python scalar is returned. This can be useful for speeding up
 |      access to elements of the array and doing arithmetic on elements of the
 |      array using Python's optimized math.
 |      
 |      Examples
 |      --------
 |      >>> x = np.random.randint(9, size=(3, 3))
 |      >>> x
 |      array([[3, 1, 7],
 |             [2, 8, 3],
 |             [8, 5, 3]])
 |      >>> x.item(3)
 |      2
 |      >>> x.item(7)
 |      5
 |      >>> x.item((0, 1))
 |      1
 |      >>> x.item((2, 2))
 |      3
 |  
 |  itemset(...)
 |      a.itemset(*args)
 |      
 |      Insert scalar into an array (scalar is cast to array's dtype, if possible)
 |      
 |      There must be at least 1 argument, and define the last argument
 |      as *item*.  Then, ``a.itemset(*args)`` is equivalent to but faster
 |      than ``a[args] = item``.  The item should be a scalar value and `args`
 |      must select a single item in the array `a`.
 |      
 |      Parameters
 |      ----------
 |      \*args : Arguments
 |          If one argument: a scalar, only used in case `a` is of size 1.
 |          If two arguments: the last argument is the value to be set
 |          and must be a scalar, the first argument specifies a single array
 |          element location. It is either an int or a tuple.
 |      
 |      Notes
 |      -----
 |      Compared to indexing syntax, `itemset` provides some speed increase
 |      for placing a scalar into a particular location in an `ndarray`,
 |      if you must do this.  However, generally this is discouraged:
 |      among other problems, it complicates the appearance of the code.
 |      Also, when using `itemset` (and `item`) inside a loop, be sure
 |      to assign the methods to a local variable to avoid the attribute
 |      look-up at each loop iteration.
 |      
 |      Examples
 |      --------
 |      >>> x = np.random.randint(9, size=(3, 3))
 |      >>> x
 |      array([[3, 1, 7],
 |             [2, 8, 3],
 |             [8, 5, 3]])
 |      >>> x.itemset(4, 0)
 |      >>> x.itemset((2, 2), 9)
 |      >>> x
 |      array([[3, 1, 7],
 |             [2, 0, 3],
 |             [8, 5, 9]])
 |  
 |  max(...)
 |      a.max(axis=None, out=None, keepdims=False)
 |      
 |      Return the maximum along a given axis.
 |      
 |      Refer to `numpy.amax` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.amax : equivalent function
 |  
 |  mean(...)
 |      a.mean(axis=None, dtype=None, out=None, keepdims=False)
 |      
 |      Returns the average of the array elements along given axis.
 |      
 |      Refer to `numpy.mean` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.mean : equivalent function
 |  
 |  min(...)
 |      a.min(axis=None, out=None, keepdims=False)
 |      
 |      Return the minimum along a given axis.
 |      
 |      Refer to `numpy.amin` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.amin : equivalent function
 |  
 |  newbyteorder(...)
 |      arr.newbyteorder(new_order='S')
 |      
 |      Return the array with the same data viewed with a different byte order.
 |      
 |      Equivalent to::
 |      
 |          arr.view(arr.dtype.newbytorder(new_order))
 |      
 |      Changes are also made in all fields and sub-arrays of the array data
 |      type.
 |      
 |      
 |      
 |      Parameters
 |      ----------
 |      new_order : string, optional
 |          Byte order to force; a value from the byte order specifications
 |          below. `new_order` codes can be any of:
 |      
 |          * 'S' - swap dtype from current to opposite endian
 |          * {'<', 'L'} - little endian
 |          * {'>', 'B'} - big endian
 |          * {'=', 'N'} - native order
 |          * {'|', 'I'} - ignore (no change to byte order)
 |      
 |          The default value ('S') results in swapping the current
 |          byte order. The code does a case-insensitive check on the first
 |          letter of `new_order` for the alternatives above.  For example,
 |          any of 'B' or 'b' or 'biggish' are valid to specify big-endian.
 |      
 |      
 |      Returns
 |      -------
 |      new_arr : array
 |          New array object with the dtype reflecting given change to the
 |          byte order.
 |  
 |  nonzero(...)
 |      a.nonzero()
 |      
 |      Return the indices of the elements that are non-zero.
 |      
 |      Refer to `numpy.nonzero` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.nonzero : equivalent function
 |  
 |  partition(...)
 |      a.partition(kth, axis=-1, kind='introselect', order=None)
 |      
 |      Rearranges the elements in the array in such a way that the value of the
 |      element in kth position is in the position it would be in a sorted array.
 |      All elements smaller than the kth element are moved before this element and
 |      all equal or greater are moved behind it. The ordering of the elements in
 |      the two partitions is undefined.
 |      
 |      .. versionadded:: 1.8.0
 |      
 |      Parameters
 |      ----------
 |      kth : int or sequence of ints
 |          Element index to partition by. The kth element value will be in its
 |          final sorted position and all smaller elements will be moved before it
 |          and all equal or greater elements behind it.
 |          The order of all elements in the partitions is undefined.
 |          If provided with a sequence of kth it will partition all elements
 |          indexed by kth of them into their sorted position at once.
 |      axis : int, optional
 |          Axis along which to sort. Default is -1, which means sort along the
 |          last axis.
 |      kind : {'introselect'}, optional
 |          Selection algorithm. Default is 'introselect'.
 |      order : str or list of str, optional
 |          When `a` is an array with fields defined, this argument specifies
 |          which fields to compare first, second, etc. A single field can
 |          be specified as a string, and not all fields need to be specified,
 |          but unspecified fields will still be used, in the order in which
 |          they come up in the dtype, to break ties.
 |      
 |      See Also
 |      --------
 |      numpy.partition : Return a parititioned copy of an array.
 |      argpartition : Indirect partition.
 |      sort : Full sort.
 |      
 |      Notes
 |      -----
 |      See ``np.partition`` for notes on the different algorithms.
 |      
 |      Examples
 |      --------
 |      >>> a = np.array([3, 4, 2, 1])
 |      >>> a.partition(3)
 |      >>> a
 |      array([2, 1, 3, 4])
 |      
 |      >>> a.partition((1, 3))
 |      array([1, 2, 3, 4])
 |  
 |  prod(...)
 |      a.prod(axis=None, dtype=None, out=None, keepdims=False)
 |      
 |      Return the product of the array elements over the given axis
 |      
 |      Refer to `numpy.prod` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.prod : equivalent function
 |  
 |  ptp(...)
 |      a.ptp(axis=None, out=None, keepdims=False)
 |      
 |      Peak to peak (maximum - minimum) value along a given axis.
 |      
 |      Refer to `numpy.ptp` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.ptp : equivalent function
 |  
 |  put(...)
 |      a.put(indices, values, mode='raise')
 |      
 |      Set ``a.flat[n] = values[n]`` for all `n` in indices.
 |      
 |      Refer to `numpy.put` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.put : equivalent function
 |  
 |  ravel(...)
 |      a.ravel([order])
 |      
 |      Return a flattened array.
 |      
 |      Refer to `numpy.ravel` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.ravel : equivalent function
 |      
 |      ndarray.flat : a flat iterator on the array.
 |  
 |  repeat(...)
 |      a.repeat(repeats, axis=None)
 |      
 |      Repeat elements of an array.
 |      
 |      Refer to `numpy.repeat` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.repeat : equivalent function
 |  
 |  reshape(...)
 |      a.reshape(shape, order='C')
 |      
 |      Returns an array containing the same data with a new shape.
 |      
 |      Refer to `numpy.reshape` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.reshape : equivalent function
 |      
 |      Notes
 |      -----
 |      Unlike the free function `numpy.reshape`, this method on `ndarray` allows
 |      the elements of the shape parameter to be passed in as separate arguments.
 |      For example, ``a.reshape(10, 11)`` is equivalent to
 |      ``a.reshape((10, 11))``.
 |  
 |  resize(...)
 |      a.resize(new_shape, refcheck=True)
 |      
 |      Change shape and size of array in-place.
 |      
 |      Parameters
 |      ----------
 |      new_shape : tuple of ints, or `n` ints
 |          Shape of resized array.
 |      refcheck : bool, optional
 |          If False, reference count will not be checked. Default is True.
 |      
 |      Returns
 |      -------
 |      None
 |      
 |      Raises
 |      ------
 |      ValueError
 |          If `a` does not own its own data or references or views to it exist,
 |          and the data memory must be changed.
 |          PyPy only: will always raise if the data memory must be changed, since
 |          there is no reliable way to determine if references or views to it
 |          exist.
 |      
 |      SystemError
 |          If the `order` keyword argument is specified. This behaviour is a
 |          bug in NumPy.
 |      
 |      See Also
 |      --------
 |      resize : Return a new array with the specified shape.
 |      
 |      Notes
 |      -----
 |      This reallocates space for the data area if necessary.
 |      
 |      Only contiguous arrays (data elements consecutive in memory) can be
 |      resized.
 |      
 |      The purpose of the reference count check is to make sure you
 |      do not use this array as a buffer for another Python object and then
 |      reallocate the memory. However, reference counts can increase in
 |      other ways so if you are sure that you have not shared the memory
 |      for this array with another Python object, then you may safely set
 |      `refcheck` to False.
 |      
 |      Examples
 |      --------
 |      Shrinking an array: array is flattened (in the order that the data are
 |      stored in memory), resized, and reshaped:
 |      
 |      >>> a = np.array([[0, 1], [2, 3]], order='C')
 |      >>> a.resize((2, 1))
 |      >>> a
 |      array([[0],
 |             [1]])
 |      
 |      >>> a = np.array([[0, 1], [2, 3]], order='F')
 |      >>> a.resize((2, 1))
 |      >>> a
 |      array([[0],
 |             [2]])
 |      
 |      Enlarging an array: as above, but missing entries are filled with zeros:
 |      
 |      >>> b = np.array([[0, 1], [2, 3]])
 |      >>> b.resize(2, 3) # new_shape parameter doesn't have to be a tuple
 |      >>> b
 |      array([[0, 1, 2],
 |             [3, 0, 0]])
 |      
 |      Referencing an array prevents resizing...
 |      
 |      >>> c = a
 |      >>> a.resize((1, 1))
 |      Traceback (most recent call last):
 |      ...
 |      ValueError: cannot resize an array that has been referenced ...
 |      
 |      Unless `refcheck` is False:
 |      
 |      >>> a.resize((1, 1), refcheck=False)
 |      >>> a
 |      array([[0]])
 |      >>> c
 |      array([[0]])
 |  
 |  round(...)
 |      a.round(decimals=0, out=None)
 |      
 |      Return `a` with each element rounded to the given number of decimals.
 |      
 |      Refer to `numpy.around` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.around : equivalent function
 |  
 |  searchsorted(...)
 |      a.searchsorted(v, side='left', sorter=None)
 |      
 |      Find indices where elements of v should be inserted in a to maintain order.
 |      
 |      For full documentation, see `numpy.searchsorted`
 |      
 |      See Also
 |      --------
 |      numpy.searchsorted : equivalent function
 |  
 |  setfield(...)
 |      a.setfield(val, dtype, offset=0)
 |      
 |      Put a value into a specified place in a field defined by a data-type.
 |      
 |      Place `val` into `a`'s field defined by `dtype` and beginning `offset`
 |      bytes into the field.
 |      
 |      Parameters
 |      ----------
 |      val : object
 |          Value to be placed in field.
 |      dtype : dtype object
 |          Data-type of the field in which to place `val`.
 |      offset : int, optional
 |          The number of bytes into the field at which to place `val`.
 |      
 |      Returns
 |      -------
 |      None
 |      
 |      See Also
 |      --------
 |      getfield
 |      
 |      Examples
 |      --------
 |      >>> x = np.eye(3)
 |      >>> x.getfield(np.float64)
 |      array([[ 1.,  0.,  0.],
 |             [ 0.,  1.,  0.],
 |             [ 0.,  0.,  1.]])
 |      >>> x.setfield(3, np.int32)
 |      >>> x.getfield(np.int32)
 |      array([[3, 3, 3],
 |             [3, 3, 3],
 |             [3, 3, 3]])
 |      >>> x
 |      array([[  1.00000000e+000,   1.48219694e-323,   1.48219694e-323],
 |             [  1.48219694e-323,   1.00000000e+000,   1.48219694e-323],
 |             [  1.48219694e-323,   1.48219694e-323,   1.00000000e+000]])
 |      >>> x.setfield(np.eye(3), np.int32)
 |      >>> x
 |      array([[ 1.,  0.,  0.],
 |             [ 0.,  1.,  0.],
 |             [ 0.,  0.,  1.]])
 |  
 |  setflags(...)
 |      a.setflags(write=None, align=None, uic=None)
 |      
 |      Set array flags WRITEABLE, ALIGNED, (WRITEBACKIFCOPY and UPDATEIFCOPY),
 |      respectively.
 |      
 |      These Boolean-valued flags affect how numpy interprets the memory
 |      area used by `a` (see Notes below). The ALIGNED flag can only
 |      be set to True if the data is actually aligned according to the type.
 |      The WRITEBACKIFCOPY and (deprecated) UPDATEIFCOPY flags can never be set
 |      to True. The flag WRITEABLE can only be set to True if the array owns its
 |      own memory, or the ultimate owner of the memory exposes a writeable buffer
 |      interface, or is a string. (The exception for string is made so that
 |      unpickling can be done without copying memory.)
 |      
 |      Parameters
 |      ----------
 |      write : bool, optional
 |          Describes whether or not `a` can be written to.
 |      align : bool, optional
 |          Describes whether or not `a` is aligned properly for its type.
 |      uic : bool, optional
 |          Describes whether or not `a` is a copy of another "base" array.
 |      
 |      Notes
 |      -----
 |      Array flags provide information about how the memory area used
 |      for the array is to be interpreted. There are 7 Boolean flags
 |      in use, only four of which can be changed by the user:
 |      WRITEBACKIFCOPY, UPDATEIFCOPY, WRITEABLE, and ALIGNED.
 |      
 |      WRITEABLE (W) the data area can be written to;
 |      
 |      ALIGNED (A) the data and strides are aligned appropriately for the hardware
 |      (as determined by the compiler);
 |      
 |      UPDATEIFCOPY (U) (deprecated), replaced by WRITEBACKIFCOPY;
 |      
 |      WRITEBACKIFCOPY (X) this array is a copy of some other array (referenced
 |      by .base). When the C-API function PyArray_ResolveWritebackIfCopy is
 |      called, the base array will be updated with the contents of this array.
 |      
 |      All flags can be accessed using the single (upper case) letter as well
 |      as the full name.
 |      
 |      Examples
 |      --------
 |      >>> y
 |      array([[3, 1, 7],
 |             [2, 0, 0],
 |             [8, 5, 9]])
 |      >>> y.flags
 |        C_CONTIGUOUS : True
 |        F_CONTIGUOUS : False
 |        OWNDATA : True
 |        WRITEABLE : True
 |        ALIGNED : True
 |        WRITEBACKIFCOPY : False
 |        UPDATEIFCOPY : False
 |      >>> y.setflags(write=0, align=0)
 |      >>> y.flags
 |        C_CONTIGUOUS : True
 |        F_CONTIGUOUS : False
 |        OWNDATA : True
 |        WRITEABLE : False
 |        ALIGNED : False
 |        WRITEBACKIFCOPY : False
 |        UPDATEIFCOPY : False
 |      >>> y.setflags(uic=1)
 |      Traceback (most recent call last):
 |        File "<stdin>", line 1, in <module>
 |      ValueError: cannot set WRITEBACKIFCOPY flag to True
 |  
 |  sort(...)
 |      a.sort(axis=-1, kind='quicksort', order=None)
 |      
 |      Sort an array, in-place.
 |      
 |      Parameters
 |      ----------
 |      axis : int, optional
 |          Axis along which to sort. Default is -1, which means sort along the
 |          last axis.
 |      kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, optional
 |          Sorting algorithm. Default is 'quicksort'.
 |      order : str or list of str, optional
 |          When `a` is an array with fields defined, this argument specifies
 |          which fields to compare first, second, etc.  A single field can
 |          be specified as a string, and not all fields need be specified,
 |          but unspecified fields will still be used, in the order in which
 |          they come up in the dtype, to break ties.
 |      
 |      See Also
 |      --------
 |      numpy.sort : Return a sorted copy of an array.
 |      argsort : Indirect sort.
 |      lexsort : Indirect stable sort on multiple keys.
 |      searchsorted : Find elements in sorted array.
 |      partition: Partial sort.
 |      
 |      Notes
 |      -----
 |      See ``sort`` for notes on the different sorting algorithms.
 |      
 |      Examples
 |      --------
 |      >>> a = np.array([[1,4], [3,1]])
 |      >>> a.sort(axis=1)
 |      >>> a
 |      array([[1, 4],
 |             [1, 3]])
 |      >>> a.sort(axis=0)
 |      >>> a
 |      array([[1, 3],
 |             [1, 4]])
 |      
 |      Use the `order` keyword to specify a field to use when sorting a
 |      structured array:
 |      
 |      >>> a = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])
 |      >>> a.sort(order='y')
 |      >>> a
 |      array([('c', 1), ('a', 2)],
 |            dtype=[('x', '|S1'), ('y', '<i4')])
 |  
 |  squeeze(...)
 |      a.squeeze(axis=None)
 |      
 |      Remove single-dimensional entries from the shape of `a`.
 |      
 |      Refer to `numpy.squeeze` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.squeeze : equivalent function
 |  
 |  std(...)
 |      a.std(axis=None, dtype=None, out=None, ddof=0, keepdims=False)
 |      
 |      Returns the standard deviation of the array elements along given axis.
 |      
 |      Refer to `numpy.std` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.std : equivalent function
 |  
 |  sum(...)
 |      a.sum(axis=None, dtype=None, out=None, keepdims=False)
 |      
 |      Return the sum of the array elements over the given axis.
 |      
 |      Refer to `numpy.sum` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.sum : equivalent function
 |  
 |  swapaxes(...)
 |      a.swapaxes(axis1, axis2)
 |      
 |      Return a view of the array with `axis1` and `axis2` interchanged.
 |      
 |      Refer to `numpy.swapaxes` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.swapaxes : equivalent function
 |  
 |  take(...)
 |      a.take(indices, axis=None, out=None, mode='raise')
 |      
 |      Return an array formed from the elements of `a` at the given indices.
 |      
 |      Refer to `numpy.take` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.take : equivalent function
 |  
 |  tobytes(...)
 |      a.tobytes(order='C')
 |      
 |      Construct Python bytes containing the raw data bytes in the array.
 |      
 |      Constructs Python bytes showing a copy of the raw contents of
 |      data memory. The bytes object can be produced in either 'C' or 'Fortran',
 |      or 'Any' order (the default is 'C'-order). 'Any' order means C-order
 |      unless the F_CONTIGUOUS flag in the array is set, in which case it
 |      means 'Fortran' order.
 |      
 |      .. versionadded:: 1.9.0
 |      
 |      Parameters
 |      ----------
 |      order : {'C', 'F', None}, optional
 |          Order of the data for multidimensional arrays:
 |          C, Fortran, or the same as for the original array.
 |      
 |      Returns
 |      -------
 |      s : bytes
 |          Python bytes exhibiting a copy of `a`'s raw data.
 |      
 |      Examples
 |      --------
 |      >>> x = np.array([[0, 1], [2, 3]])
 |      >>> x.tobytes()
 |      b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
 |      >>> x.tobytes('C') == x.tobytes()
 |      True
 |      >>> x.tobytes('F')
 |      b'\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00'
 |  
 |  tofile(...)
 |      a.tofile(fid, sep="", format="%s")
 |      
 |      Write array to a file as text or binary (default).
 |      
 |      Data is always written in 'C' order, independent of the order of `a`.
 |      The data produced by this method can be recovered using the function
 |      fromfile().
 |      
 |      Parameters
 |      ----------
 |      fid : file or str
 |          An open file object, or a string containing a filename.
 |      sep : str
 |          Separator between array items for text output.
 |          If "" (empty), a binary file is written, equivalent to
 |          ``file.write(a.tobytes())``.
 |      format : str
 |          Format string for text file output.
 |          Each entry in the array is formatted to text by first converting
 |          it to the closest Python type, and then using "format" % item.
 |      
 |      Notes
 |      -----
 |      This is a convenience function for quick storage of array data.
 |      Information on endianness and precision is lost, so this method is not a
 |      good choice for files intended to archive data or transport data between
 |      machines with different endianness. Some of these problems can be overcome
 |      by outputting the data as text files, at the expense of speed and file
 |      size.
 |      
 |      When fid is a file object, array contents are directly written to the
 |      file, bypassing the file object's ``write`` method. As a result, tofile
 |      cannot be used with files objects supporting compression (e.g., GzipFile)
 |      or file-like objects that do not support ``fileno()`` (e.g., BytesIO).
 |  
 |  tolist(...)
 |      a.tolist()
 |      
 |      Return the array as a (possibly nested) list.
 |      
 |      Return a copy of the array data as a (nested) Python list.
 |      Data items are converted to the nearest compatible Python type.
 |      
 |      Parameters
 |      ----------
 |      none
 |      
 |      Returns
 |      -------
 |      y : list
 |          The possibly nested list of array elements.
 |      
 |      Notes
 |      -----
 |      The array may be recreated, ``a = np.array(a.tolist())``.
 |      
 |      Examples
 |      --------
 |      >>> a = np.array([1, 2])
 |      >>> a.tolist()
 |      [1, 2]
 |      >>> a = np.array([[1, 2], [3, 4]])
 |      >>> list(a)
 |      [array([1, 2]), array([3, 4])]
 |      >>> a.tolist()
 |      [[1, 2], [3, 4]]
 |  
 |  tostring(...)
 |      a.tostring(order='C')
 |      
 |      Construct Python bytes containing the raw data bytes in the array.
 |      
 |      Constructs Python bytes showing a copy of the raw contents of
 |      data memory. The bytes object can be produced in either 'C' or 'Fortran',
 |      or 'Any' order (the default is 'C'-order). 'Any' order means C-order
 |      unless the F_CONTIGUOUS flag in the array is set, in which case it
 |      means 'Fortran' order.
 |      
 |      This function is a compatibility alias for tobytes. Despite its name it returns bytes not strings.
 |      
 |      Parameters
 |      ----------
 |      order : {'C', 'F', None}, optional
 |          Order of the data for multidimensional arrays:
 |          C, Fortran, or the same as for the original array.
 |      
 |      Returns
 |      -------
 |      s : bytes
 |          Python bytes exhibiting a copy of `a`'s raw data.
 |      
 |      Examples
 |      --------
 |      >>> x = np.array([[0, 1], [2, 3]])
 |      >>> x.tobytes()
 |      b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
 |      >>> x.tobytes('C') == x.tobytes()
 |      True
 |      >>> x.tobytes('F')
 |      b'\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00'
 |  
 |  trace(...)
 |      a.trace(offset=0, axis1=0, axis2=1, dtype=None, out=None)
 |      
 |      Return the sum along diagonals of the array.
 |      
 |      Refer to `numpy.trace` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.trace : equivalent function
 |  
 |  transpose(...)
 |      a.transpose(*axes)
 |      
 |      Returns a view of the array with axes transposed.
 |      
 |      For a 1-D array, this has no effect. (To change between column and
 |      row vectors, first cast the 1-D array into a matrix object.)
 |      For a 2-D array, this is the usual matrix transpose.
 |      For an n-D array, if axes are given, their order indicates how the
 |      axes are permuted (see Examples). If axes are not provided and
 |      ``a.shape = (i[0], i[1], ... i[n-2], i[n-1])``, then
 |      ``a.transpose().shape = (i[n-1], i[n-2], ... i[1], i[0])``.
 |      
 |      Parameters
 |      ----------
 |      axes : None, tuple of ints, or `n` ints
 |      
 |       * None or no argument: reverses the order of the axes.
 |      
 |       * tuple of ints: `i` in the `j`-th place in the tuple means `a`'s
 |         `i`-th axis becomes `a.transpose()`'s `j`-th axis.
 |      
 |       * `n` ints: same as an n-tuple of the same ints (this form is
 |         intended simply as a "convenience" alternative to the tuple form)
 |      
 |      Returns
 |      -------
 |      out : ndarray
 |          View of `a`, with axes suitably permuted.
 |      
 |      See Also
 |      --------
 |      ndarray.T : Array property returning the array transposed.
 |      
 |      Examples
 |      --------
 |      >>> a = np.array([[1, 2], [3, 4]])
 |      >>> a
 |      array([[1, 2],
 |             [3, 4]])
 |      >>> a.transpose()
 |      array([[1, 3],
 |             [2, 4]])
 |      >>> a.transpose((1, 0))
 |      array([[1, 3],
 |             [2, 4]])
 |      >>> a.transpose(1, 0)
 |      array([[1, 3],
 |             [2, 4]])
 |  
 |  var(...)
 |      a.var(axis=None, dtype=None, out=None, ddof=0, keepdims=False)
 |      
 |      Returns the variance of the array elements, along given axis.
 |      
 |      Refer to `numpy.var` for full documentation.
 |      
 |      See Also
 |      --------
 |      numpy.var : equivalent function
 |  
 |  view(...)
 |      a.view(dtype=None, type=None)
 |      
 |      New view of array with the same data.
 |      
 |      Parameters
 |      ----------
 |      dtype : data-type or ndarray sub-class, optional
 |          Data-type descriptor of the returned view, e.g., float32 or int16. The
 |          default, None, results in the view having the same data-type as `a`.
 |          This argument can also be specified as an ndarray sub-class, which
 |          then specifies the type of the returned object (this is equivalent to
 |          setting the ``type`` parameter).
 |      type : Python type, optional
 |          Type of the returned view, e.g., ndarray or matrix.  Again, the
 |          default None results in type preservation.
 |      
 |      Notes
 |      -----
 |      ``a.view()`` is used two different ways:
 |      
 |      ``a.view(some_dtype)`` or ``a.view(dtype=some_dtype)`` constructs a view
 |      of the array's memory with a different data-type.  This can cause a
 |      reinterpretation of the bytes of memory.
 |      
 |      ``a.view(ndarray_subclass)`` or ``a.view(type=ndarray_subclass)`` just
 |      returns an instance of `ndarray_subclass` that looks at the same array
 |      (same shape, dtype, etc.)  This does not cause a reinterpretation of the
 |      memory.
 |      
 |      For ``a.view(some_dtype)``, if ``some_dtype`` has a different number of
 |      bytes per entry than the previous dtype (for example, converting a
 |      regular array to a structured array), then the behavior of the view
 |      cannot be predicted just from the superficial appearance of ``a`` (shown
 |      by ``print(a)``). It also depends on exactly how ``a`` is stored in
 |      memory. Therefore if ``a`` is C-ordered versus fortran-ordered, versus
 |      defined as a slice or transpose, etc., the view may give different
 |      results.
 |      
 |      
 |      Examples
 |      --------
 |      >>> x = np.array([(1, 2)], dtype=[('a', np.int8), ('b', np.int8)])
 |      
 |      Viewing array data using a different type and dtype:
 |      
 |      >>> y = x.view(dtype=np.int16, type=np.matrix)
 |      >>> y
 |      matrix([[513]], dtype=int16)
 |      >>> print(type(y))
 |      <class 'numpy.matrixlib.defmatrix.matrix'>
 |      
 |      Creating a view on a structured array so it can be used in calculations
 |      
 |      >>> x = np.array([(1, 2),(3,4)], dtype=[('a', np.int8), ('b', np.int8)])
 |      >>> xv = x.view(dtype=np.int8).reshape(-1,2)
 |      >>> xv
 |      array([[1, 2],
 |             [3, 4]], dtype=int8)
 |      >>> xv.mean(0)
 |      array([ 2.,  3.])
 |      
 |      Making changes to the view changes the underlying array
 |      
 |      >>> xv[0,1] = 20
 |      >>> print(x)
 |      [(1, 20) (3, 4)]
 |      
 |      Using a view to convert an array to a recarray:
 |      
 |      >>> z = x.view(np.recarray)
 |      >>> z.a
 |      array([1], dtype=int8)
 |      
 |      Views share data:
 |      
 |      >>> x[0] = (9, 10)
 |      >>> z[0]
 |      (9, 10)
 |      
 |      Views that change the dtype size (bytes per entry) should normally be
 |      avoided on arrays defined by slices, transposes, fortran-ordering, etc.:
 |      
 |      >>> x = np.array([[1,2,3],[4,5,6]], dtype=np.int16)
 |      >>> y = x[:, 0:2]
 |      >>> y
 |      array([[1, 2],
 |             [4, 5]], dtype=int16)
 |      >>> y.view(dtype=[('width', np.int16), ('length', np.int16)])
 |      Traceback (most recent call last):
 |        File "<stdin>", line 1, in <module>
 |      ValueError: new type not compatible with array.
 |      >>> z = y.copy()
 |      >>> z.view(dtype=[('width', np.int16), ('length', np.int16)])
 |      array([[(1, 2)],
 |             [(4, 5)]], dtype=[('width', '<i2'), ('length', '<i2')])
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
 |  T
 |      Same as self.transpose(), except that self is returned if
 |      self.ndim < 2.
 |      
 |      Examples
 |      --------
 |      >>> x = np.array([[1.,2.],[3.,4.]])
 |      >>> x
 |      array([[ 1.,  2.],
 |             [ 3.,  4.]])
 |      >>> x.T
 |      array([[ 1.,  3.],
 |             [ 2.,  4.]])
 |      >>> x = np.array([1.,2.,3.,4.])
 |      >>> x
 |      array([ 1.,  2.,  3.,  4.])
 |      >>> x.T
 |      array([ 1.,  2.,  3.,  4.])
 |  
 |  __array_finalize__
 |      None.
 |  
 |  __array_interface__
 |      Array protocol: Python side.
 |  
 |  __array_priority__
 |      Array priority.
 |  
 |  __array_struct__
 |      Array protocol: C-struct side.
 |  
 |  base
 |      Base object if memory is from some other object.
 |      
 |      Examples
 |      --------
 |      The base of an array that owns its memory is None:
 |      
 |      >>> x = np.array([1,2,3,4])
 |      >>> x.base is None
 |      True
 |      
 |      Slicing creates a view, whose memory is shared with x:
 |      
 |      >>> y = x[2:]
 |      >>> y.base is x
 |      True
 |  
 |  ctypes
 |      An object to simplify the interaction of the array with the ctypes
 |      module.
 |      
 |      This attribute creates an object that makes it easier to use arrays
 |      when calling shared libraries with the ctypes module. The returned
 |      object has, among others, data, shape, and strides attributes (see
 |      Notes below) which themselves return ctypes objects that can be used
 |      as arguments to a shared library.
 |      
 |      Parameters
 |      ----------
 |      None
 |      
 |      Returns
 |      -------
 |      c : Python object
 |          Possessing attributes data, shape, strides, etc.
 |      
 |      See Also
 |      --------
 |      numpy.ctypeslib
 |      
 |      Notes
 |      -----
 |      Below are the public attributes of this object which were documented
 |      in "Guide to NumPy" (we have omitted undocumented public attributes,
 |      as well as documented private attributes):
 |      
 |      * data: A pointer to the memory area of the array as a Python integer.
 |        This memory area may contain data that is not aligned, or not in correct
 |        byte-order. The memory area may not even be writeable. The array
 |        flags and data-type of this array should be respected when passing this
 |        attribute to arbitrary C-code to avoid trouble that can include Python
 |        crashing. User Beware! The value of this attribute is exactly the same
 |        as self._array_interface_['data'][0].
 |      
 |      * shape (c_intp*self.ndim): A ctypes array of length self.ndim where
 |        the basetype is the C-integer corresponding to dtype('p') on this
 |        platform. This base-type could be c_int, c_long, or c_longlong
 |        depending on the platform. The c_intp type is defined accordingly in
 |        numpy.ctypeslib. The ctypes array contains the shape of the underlying
 |        array.
 |      
 |      * strides (c_intp*self.ndim): A ctypes array of length self.ndim where
 |        the basetype is the same as for the shape attribute. This ctypes array
 |        contains the strides information from the underlying array. This strides
 |        information is important for showing how many bytes must be jumped to
 |        get to the next element in the array.
 |      
 |      * data_as(obj): Return the data pointer cast to a particular c-types object.
 |        For example, calling self._as_parameter_ is equivalent to
 |        self.data_as(ctypes.c_void_p). Perhaps you want to use the data as a
 |        pointer to a ctypes array of floating-point data:
 |        self.data_as(ctypes.POINTER(ctypes.c_double)).
 |      
 |      * shape_as(obj): Return the shape tuple as an array of some other c-types
 |        type. For example: self.shape_as(ctypes.c_short).
 |      
 |      * strides_as(obj): Return the strides tuple as an array of some other
 |        c-types type. For example: self.strides_as(ctypes.c_longlong).
 |      
 |      Be careful using the ctypes attribute - especially on temporary
 |      arrays or arrays constructed on the fly. For example, calling
 |      ``(a+b).ctypes.data_as(ctypes.c_void_p)`` returns a pointer to memory
 |      that is invalid because the array created as (a+b) is deallocated
 |      before the next Python statement. You can avoid this problem using
 |      either ``c=a+b`` or ``ct=(a+b).ctypes``. In the latter case, ct will
 |      hold a reference to the array until ct is deleted or re-assigned.
 |      
 |      If the ctypes module is not available, then the ctypes attribute
 |      of array objects still returns something useful, but ctypes objects
 |      are not returned and errors may be raised instead. In particular,
 |      the object will still have the as parameter attribute which will
 |      return an integer equal to the data attribute.
 |      
 |      Examples
 |      --------
 |      >>> import ctypes
 |      >>> x
 |      array([[0, 1],
 |             [2, 3]])
 |      >>> x.ctypes.data
 |      30439712
 |      >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_long))
 |      <ctypes.LP_c_long object at 0x01F01300>
 |      >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_long)).contents
 |      c_long(0)
 |      >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_longlong)).contents
 |      c_longlong(4294967296L)
 |      >>> x.ctypes.shape
 |      <numpy.core._internal.c_long_Array_2 object at 0x01FFD580>
 |      >>> x.ctypes.shape_as(ctypes.c_long)
 |      <numpy.core._internal.c_long_Array_2 object at 0x01FCE620>
 |      >>> x.ctypes.strides
 |      <numpy.core._internal.c_long_Array_2 object at 0x01FCE620>
 |      >>> x.ctypes.strides_as(ctypes.c_longlong)
 |      <numpy.core._internal.c_longlong_Array_2 object at 0x01F01300>
 |  
 |  data
 |      Python buffer object pointing to the start of the array's data.
 |  
 |  dtype
 |      Data-type of the array's elements.
 |      
 |      Parameters
 |      ----------
 |      None
 |      
 |      Returns
 |      -------
 |      d : numpy dtype object
 |      
 |      See Also
 |      --------
 |      numpy.dtype
 |      
 |      Examples
 |      --------
 |      >>> x
 |      array([[0, 1],
 |             [2, 3]])
 |      >>> x.dtype
 |      dtype('int32')
 |      >>> type(x.dtype)
 |      <type 'numpy.dtype'>
 |  
 |  flags
 |      Information about the memory layout of the array.
 |      
 |      Attributes
 |      ----------
 |      C_CONTIGUOUS (C)
 |          The data is in a single, C-style contiguous segment.
 |      F_CONTIGUOUS (F)
 |          The data is in a single, Fortran-style contiguous segment.
 |      OWNDATA (O)
 |          The array owns the memory it uses or borrows it from another object.
 |      WRITEABLE (W)
 |          The data area can be written to.  Setting this to False locks
 |          the data, making it read-only.  A view (slice, etc.) inherits WRITEABLE
 |          from its base array at creation time, but a view of a writeable
 |          array may be subsequently locked while the base array remains writeable.
 |          (The opposite is not true, in that a view of a locked array may not
 |          be made writeable.  However, currently, locking a base object does not
 |          lock any views that already reference it, so under that circumstance it
 |          is possible to alter the contents of a locked array via a previously
 |          created writeable view onto it.)  Attempting to change a non-writeable
 |          array raises a RuntimeError exception.
 |      ALIGNED (A)
 |          The data and all elements are aligned appropriately for the hardware.
 |      WRITEBACKIFCOPY (X)
 |          This array is a copy of some other array. The C-API function
 |          PyArray_ResolveWritebackIfCopy must be called before deallocating
 |          to the base array will be updated with the contents of this array.
 |      UPDATEIFCOPY (U)
 |          (Deprecated, use WRITEBACKIFCOPY) This array is a copy of some other array.
 |          When this array is
 |          deallocated, the base array will be updated with the contents of
 |          this array.
 |      FNC
 |          F_CONTIGUOUS and not C_CONTIGUOUS.
 |      FORC
 |          F_CONTIGUOUS or C_CONTIGUOUS (one-segment test).
 |      BEHAVED (B)
 |          ALIGNED and WRITEABLE.
 |      CARRAY (CA)
 |          BEHAVED and C_CONTIGUOUS.
 |      FARRAY (FA)
 |          BEHAVED and F_CONTIGUOUS and not C_CONTIGUOUS.
 |      
 |      Notes
 |      -----
 |      The `flags` object can be accessed dictionary-like (as in ``a.flags['WRITEABLE']``),
 |      or by using lowercased attribute names (as in ``a.flags.writeable``). Short flag
 |      names are only supported in dictionary access.
 |      
 |      Only the WRITEBACKIFCOPY, UPDATEIFCOPY, WRITEABLE, and ALIGNED flags can be
 |      changed by the user, via direct assignment to the attribute or dictionary
 |      entry, or by calling `ndarray.setflags`.
 |      
 |      The array flags cannot be set arbitrarily:
 |      
 |      - UPDATEIFCOPY can only be set ``False``.
 |      - WRITEBACKIFCOPY can only be set ``False``.
 |      - ALIGNED can only be set ``True`` if the data is truly aligned.
 |      - WRITEABLE can only be set ``True`` if the array owns its own memory
 |        or the ultimate owner of the memory exposes a writeable buffer
 |        interface or is a string.
 |      
 |      Arrays can be both C-style and Fortran-style contiguous simultaneously.
 |      This is clear for 1-dimensional arrays, but can also be true for higher
 |      dimensional arrays.
 |      
 |      Even for contiguous arrays a stride for a given dimension
 |      ``arr.strides[dim]`` may be *arbitrary* if ``arr.shape[dim] == 1``
 |      or the array has no elements.
 |      It does *not* generally hold that ``self.strides[-1] == self.itemsize``
 |      for C-style contiguous arrays or ``self.strides[0] == self.itemsize`` for
 |      Fortran-style contiguous arrays is true.
 |  
 |  flat
 |      A 1-D iterator over the array.
 |      
 |      This is a `numpy.flatiter` instance, which acts similarly to, but is not
 |      a subclass of, Python's built-in iterator object.
 |      
 |      See Also
 |      --------
 |      flatten : Return a copy of the array collapsed into one dimension.
 |      
 |      flatiter
 |      
 |      Examples
 |      --------
 |      >>> x = np.arange(1, 7).reshape(2, 3)
 |      >>> x
 |      array([[1, 2, 3],
 |             [4, 5, 6]])
 |      >>> x.flat[3]
 |      4
 |      >>> x.T
 |      array([[1, 4],
 |             [2, 5],
 |             [3, 6]])
 |      >>> x.T.flat[3]
 |      5
 |      >>> type(x.flat)
 |      <type 'numpy.flatiter'>
 |      
 |      An assignment example:
 |      
 |      >>> x.flat = 3; x
 |      array([[3, 3, 3],
 |             [3, 3, 3]])
 |      >>> x.flat[[1,4]] = 1; x
 |      array([[3, 1, 3],
 |             [3, 1, 3]])
 |  
 |  imag
 |      The imaginary part of the array.
 |      
 |      Examples
 |      --------
 |      >>> x = np.sqrt([1+0j, 0+1j])
 |      >>> x.imag
 |      array([ 0.        ,  0.70710678])
 |      >>> x.imag.dtype
 |      dtype('float64')
 |  
 |  itemsize
 |      Length of one array element in bytes.
 |      
 |      Examples
 |      --------
 |      >>> x = np.array([1,2,3], dtype=np.float64)
 |      >>> x.itemsize
 |      8
 |      >>> x = np.array([1,2,3], dtype=np.complex128)
 |      >>> x.itemsize
 |      16
 |  
 |  nbytes
 |      Total bytes consumed by the elements of the array.
 |      
 |      Notes
 |      -----
 |      Does not include memory consumed by non-element attributes of the
 |      array object.
 |      
 |      Examples
 |      --------
 |      >>> x = np.zeros((3,5,2), dtype=np.complex128)
 |      >>> x.nbytes
 |      480
 |      >>> np.prod(x.shape) * x.itemsize
 |      480
 |  
 |  ndim
 |      Number of array dimensions.
 |      
 |      Examples
 |      --------
 |      >>> x = np.array([1, 2, 3])
 |      >>> x.ndim
 |      1
 |      >>> y = np.zeros((2, 3, 4))
 |      >>> y.ndim
 |      3
 |  
 |  real
 |      The real part of the array.
 |      
 |      Examples
 |      --------
 |      >>> x = np.sqrt([1+0j, 0+1j])
 |      >>> x.real
 |      array([ 1.        ,  0.70710678])
 |      >>> x.real.dtype
 |      dtype('float64')
 |      
 |      See Also
 |      --------
 |      numpy.real : equivalent function
 |  
 |  shape
 |      Tuple of array dimensions.
 |      
 |      The shape property is usually used to get the current shape of an array,
 |      but may also be used to reshape the array in-place by assigning a tuple of
 |      array dimensions to it.  As with `numpy.reshape`, one of the new shape
 |      dimensions can be -1, in which case its value is inferred from the size of
 |      the array and the remaining dimensions. Reshaping an array in-place will
 |      fail if a copy is required.
 |      
 |      Examples
 |      --------
 |      >>> x = np.array([1, 2, 3, 4])
 |      >>> x.shape
 |      (4,)
 |      >>> y = np.zeros((2, 3, 4))
 |      >>> y.shape
 |      (2, 3, 4)
 |      >>> y.shape = (3, 8)
 |      >>> y
 |      array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
 |             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
 |             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
 |      >>> y.shape = (3, 6)
 |      Traceback (most recent call last):
 |        File "<stdin>", line 1, in <module>
 |      ValueError: total size of new array must be unchanged
 |      >>> np.zeros((4,2))[::2].shape = (-1,)
 |      Traceback (most recent call last):
 |        File "<stdin>", line 1, in <module>
 |      AttributeError: incompatible shape for a non-contiguous array
 |      
 |      See Also
 |      --------
 |      numpy.reshape : similar function
 |      ndarray.reshape : similar method
 |  
 |  size
 |      Number of elements in the array.
 |      
 |      Equal to ``np.prod(a.shape)``, i.e., the product of the array's
 |      dimensions.
 |      
 |      Notes
 |      -----
 |      `a.size` returns a standard arbitrary precision Python integer. This 
 |      may not be the case with other methods of obtaining the same value
 |      (like the suggested ``np.prod(a.shape)``, which returns an instance
 |      of ``np.int_``), and may be relevant if the value is used further in
 |      calculations that may overflow a fixed size integer type.
 |      
 |      Examples
 |      --------
 |      >>> x = np.zeros((3, 5, 2), dtype=np.complex128)
 |      >>> x.size
 |      30
 |      >>> np.prod(x.shape)
 |      30
 |  
 |  strides
 |      Tuple of bytes to step in each dimension when traversing an array.
 |      
 |      The byte offset of element ``(i[0], i[1], ..., i[n])`` in an array `a`
 |      is::
 |      
 |          offset = sum(np.array(i) * a.strides)
 |      
 |      A more detailed explanation of strides can be found in the
 |      "ndarray.rst" file in the NumPy reference guide.
 |      
 |      Notes
 |      -----
 |      Imagine an array of 32-bit integers (each 4 bytes)::
 |      
 |        x = np.array([[0, 1, 2, 3, 4],
 |                      [5, 6, 7, 8, 9]], dtype=np.int32)
 |      
 |      This array is stored in memory as 40 bytes, one after the other
 |      (known as a contiguous block of memory).  The strides of an array tell
 |      us how many bytes we have to skip in memory to move to the next position
 |      along a certain axis.  For example, we have to skip 4 bytes (1 value) to
 |      move to the next column, but 20 bytes (5 values) to get to the same
 |      position in the next row.  As such, the strides for the array `x` will be
 |      ``(20, 4)``.
 |      
 |      See Also
 |      --------
 |      numpy.lib.stride_tricks.as_strided
 |      
 |      Examples
 |      --------
 |      >>> y = np.reshape(np.arange(2*3*4), (2,3,4))
 |      >>> y
 |      array([[[ 0,  1,  2,  3],
 |              [ 4,  5,  6,  7],
 |              [ 8,  9, 10, 11]],
 |             [[12, 13, 14, 15],
 |              [16, 17, 18, 19],
 |              [20, 21, 22, 23]]])
 |      >>> y.strides
 |      (48, 16, 4)
 |      >>> y[1,1,1]
 |      17
 |      >>> offset=sum(y.strides * np.array((1,1,1)))
 |      >>> offset/y.itemsize
 |      17
 |      
 |      >>> x = np.reshape(np.arange(5*6*7*8), (5,6,7,8)).transpose(2,3,1,0)
 |      >>> x.strides
 |      (32, 4, 224, 1344)
 |      >>> i = np.array([3,5,2,2])
 |      >>> offset = sum(i * x.strides)
 |      >>> x[3,5,2,2]
 |      813
 |      >>> offset / x.itemsize
 |      813
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None


[3, 4, 1, 2, 2, 1] + 10
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-23-a2508fc27c2b> in <module>
----> 1 [3, 4, 1, 2, 2, 1] + 10

TypeError: can only concatenate list (not "int") to list


rolls + 10
array([14, 11, 15, 15, 14, 12, 14, 13, 14, 14])

rolls
​
array([4, 1, 5, 5, 4, 2, 4, 3, 4, 4])

# At which indices are the dice less than or equal to 3?
rolls <= 3
array([False,  True, False, False, False,  True, False,  True, False,
       False])

xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))
xlist = [[1, 2, 3], [2, 4, 6]]
x =
[[1 2 3]
 [2 4 6]]

# Get the last element of the second row of our numpy array
x[1,-1]
6

# Get the last element of the second sublist of our nested list?
xlist[1,-1]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-29-e2f4c7f35788> in <module>
      1 # Get the last element of the second sublist of our nested list?
----> 2 xlist[1,-1]

TypeError: list indices must be integers or slices, not tuple


import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add them together to get...
a + b
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-30-70e37493c0c9> in <module>
----> 1 import tensorflow as tf
      2 # Create two constants, each with value 1
      3 a = tf.constant(1)
      4 b = tf.constant(1)
      5 # Add them together to get...

ModuleNotFoundError: No module named 'tensorflow'


print(dir(list))
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# Get the rows with population over 1m in South America
df[(df['population'] > 10*6) & (df['continent'] == 'South America')]
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-32-8b3087cd21db> in <module>
      1 # Get the rows with population over 1m in South America
----> 2 df[(df['population'] > 10*6) & (df['continent'] == 'South America')]

NameError: name 'df' is not defined


​
