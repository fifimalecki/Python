import math
print((2.25).as_integer_ratio())
print((12.34).as_integer_ratio())
print((66.66).as_integer_ratio())
print((math.pi).as_integer_ratio())

import sys
print(sys.float_info)

x=sys.float_info.max
print(x)
print(2*x)