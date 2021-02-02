def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

# generator is much faster and memory efficient, we don't wait for result ready to use next one so faster
import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(10000000)))
print(sys.getsizeof(firstn_generator(10000000)))

