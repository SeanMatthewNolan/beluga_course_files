# Modules on the Python search path may be imported as follows
import math

var1 = math.pi/8

# Import statements can limit what is imported
from math import exp, log

var2 = exp(log(100))

# Everything may be imported from package (sloppy in production code)
from math import *

var3 = cos(2)**2 + sin(2)**2

# Imports may be aliased
from cmath import sqrt as isqrt
var4 = isqrt(-1)

# Objects can be imported from the same directory
from _4_classes import Animal

# Submodules can be imported as well, note __init__.py
from example_module import example_value, module_function, ModuleClass
