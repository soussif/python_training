# import sys
# from typing import Counter

# import requests

# print(sys.version)
# print(sys.executable)

# phrase = "Giraffe Academy"
# print(phrase.index("G"))
# print(phrase.replace("Giraffe", "Elephant"))

# string = "Hello World"
# substring = string[1:5]
# reversestring = string[::-1]
# removewhitespacestring = string.strip()
# upperstring = string.upper()
# startwith = string.startswith('Hello')
# findstring = string.find('lo')  # - 1 if not found
# replace = string.replace('World', 'Universe')
# splitwork = string.split()  # delimiter space if you want to change.split(",")
# converstring = ' '.join(splitwork)  # join again a list into a string, better than for i in
# var1 = 3.1
# var2 = 6
# my_string = f"the variable is {var1} and {var2}"  # new syntax 3.6
# print(my_string)

# # from timeit import default_timer as timer

# # start = timer()
# # # operation
# # stop = timer()
# # print(stop-start)

# for i in reversestring:
#     print(i)
# if 'ell' in reversestring:
#     print('yes')
# else:
#     print('no')

# print("Giraffe\" Academy")
# name = 'Faek'
# result = float(5) + int(5.8)
# list = ["karen", "kevin", "Jim"]
# list2 = ["1", "2"]
# list_add = list.insert(1, "kelly")
# list_extend = list.extend(list2)
# list_index = list.index("karen")
# list_remove = list.remove("kelly")
# list_count = list.count("kevin")
# list_sort = list.sort()
# list_copy = list.copy()
# tuples = ("karen", "kevin", "Jim")
# dict = {
#     "Jan": "January",
#     "Feb": "February"
# }
# print(dict["Jan"])
# print(dict.get("Mar"))

# from collections import Counter
# a = "aaaabbbcc"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.most_common(1)[0][0])
# print(list(my_counter.elements()))

# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)
# print(pt.x)
# print(pt.y)

# from collections import defaultdict  # has a default value
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['c'])  # default int is 0

# from collections import deque
# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(3)
# print(d)

# d.popleft()
# print (d)
# d.clear()
# d.extendleft([4,5,6])
# print(d)
# d.rotate(1)
# print(d)

# lambda arguments: expression
# add10 = lambda x: x + 10

# def add10_func(x):
#     return x+ 10

# print(add10(5))
# mult = lambda x,y: x*y
# print(mult(2,7))




# read = open("zmlony0201_old.txt", "r")
# print(read.readable())
# # print(read.readlines())
# # read.close()

# append = open("zmlony0201_old.txt", "a")
# append.write("\nTest text")
# append.close()

# overwrite = open("index.html", "w")
# overwrite.write("<p>This is a Test HTML</p>")
# overwrite.close()


# student1 = Student("Faek", "IT", 5)
# student2 = Student("Mauricio", "Accounting", 2.8)
# print(student1.gpa)
# print("student 1 is on honor: " + str(student1.on_honor_roll()))
# print("student 2 is on honor: " + str(student2.on_honor_roll()))
# student3 = SpecialStudent("Hubert", "Art", 2.5)
# print(student3.name)
# print(student3.on_honor_roll())
# print(student3.special_student())


# print(greet(name))
# r = requests.get('https://coreyms.com')
# print(r.status_code)