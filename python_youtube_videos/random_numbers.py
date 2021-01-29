import random

a = random.random()
print(a)

b_float = random.uniform(1, 10)
print(b_float)
b_int = random.randint(1, 10)
print(b_int)
b_excludeupper = random.randrange(1, 10)
print(b_excludeupper)

b_normaldistribution = random.normalvariate(0, 1)
print(b_normaldistribution)

mylist = list("ABCDEFGH")

c_choice = random.choice(mylist)
print(c_choice)
c_sample = random.sample(mylist, 3)
print(c_sample)

c_shuffle = random.shuffle(mylist)
print(c_shuffle)

import secrets

a = secrets.randbelow(10)
print("10 not included " + a)

a = secrets.randbits(4)
# 1111 from 1 to 15
print(a)
list = list("ABCDEF")
a = secrets.choice(list)

import numpy as np
a = np.random.rand(3, 3)
# 3 * 3random float
a = np.random.randint(0, 10, (3,4))
# a 3 * 4
print(a)
