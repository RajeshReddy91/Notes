import lambda_func as lf    # module aliasing
print(lf.l)

"""if we want to use objects directly, ie l instead if lf.l, then we have to use from - import

from lambda_func import l   
print(l)

we can also alias members like below
from lambda_func import add as a, product as p
a(10,20)
p(10,20)

if same function is present in 2 diff modules, then function from the most recent module imported will be executed.

import time
time.sleep(45)  # pause for 45 secs

*** if we want to use updated version of module then we can use
import imp
imp.reload(module1) 

"""
