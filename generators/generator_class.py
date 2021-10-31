def gen(n):
    for i in range(n):
        yield i**2
        # yield return value and pauses this function so we keep track of internal information, but return stop the function
g = gen(10)
for i in g:
    print(i)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))