from collections import Counter
from typing import Counter

a = "aaaabbbcc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))


from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x)
print(pt.y)


from collections import defaultdict  # has a default value
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])  # default int is 0


from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.popleft()
print (d)
d.clear()
d.extendleft([4,5,6])
print(d)
d.rotate(1)
print(d)