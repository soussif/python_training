
# default argument at the end
def foo(a, b, c, d=4):
    print(a, b, c)


my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2, 'c': 3}
# to unpack list as argument
foo(*my_list)
foo(**my_dict)


# variable length function
def foo2(a, b, *args, **kwargs):
    # arg you can pass any argument like "3", kwargs you can pass any keywords argument like "three=3"
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo2(1, 2, 3, 4, 5, six=6, seven=7)

def foo3():
    global number
    x = number
    number = 3
    print('number inside function: ', x)


number = 0
foo3()
print(number)

# python call by object or object reference