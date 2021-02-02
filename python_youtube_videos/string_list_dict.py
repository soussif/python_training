import sys


print(sys.version)
print(sys.executable)

phrase = "Giraffe Academy"
print(phrase.index("G"))
print(phrase.replace("Giraffe", "Elephant"))

string = "Hello World"
substring = string[1:5]
reversestring = string[::-1]
removewhitespacestring = string.strip()
upperstring = string.upper()
startwith = string.startswith('Hello')
# - 1 if not found
findstring = string.find('lo')
replace = string.replace('World', 'Universe')
# delimiter space if you want to change.split(",")
splitwork = string.split()
# join again a list into a string, better than for i in
converstring = ' '.join(splitwork)
var1 = 3.1
var2 = 6
my_string = f"the variable is {var1} and {var2}"  # new syntax 3.6
print(my_string)


for i in reversestring:
    print(i)
if 'ell' in reversestring:
    print('yes')
else:
    print('no')

print("Giraffe\" Academy")
name = 'Faek'
result = float(5) + int(5.8)
list = ["karen", "kevin", "Jim"]
list2 = ["1", "2"]
list_add = list.insert(1, "kelly")
list_extend = list.extend(list2)
list_index = list.index("karen")
list_remove = list.remove("kelly")
list_count = list.count("kevin")
list_sort = list.sort()
list_copy = list.copy()
tuples = ("karen", "kevin", "Jim")
dict = {
    "Jan": "January",
    "Feb": "February"
}
print(dict["Jan"])
print(dict.get("Mar"))

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))
