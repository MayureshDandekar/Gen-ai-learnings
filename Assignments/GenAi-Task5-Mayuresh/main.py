import math_utils

print(math_utils.add(4,3))
print(math_utils.substract(10,3))
print(math_utils.square(3))

from math_utils import square
print(square(3))

import string_utils

print(string_utils.capitalize_words("the moutains are beautiful"))
print(string_utils.reverse_string("boy is good"))
print(string_utils.word_count("Hey How are You!!"))

from shop_package import discount as disc

print(disc.apply_discount(10000,10))
print(disc.flat_discount(10000))

from shop_package.billing import calculate_total, apply_tax
print(calculate_total([1000,5000,4000]))
print(apply_tax(10000))

# from shop_package import * 

# print(apply_discount(10000,10))
# print(flat_discount(10000))

# print(calculate_total([1000,5000,4000]))
# print(apply_tax(10000))
