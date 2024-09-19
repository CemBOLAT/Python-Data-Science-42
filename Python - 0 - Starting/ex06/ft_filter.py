
# List comprehensions: [x for x in iterable if f(x)]
def ft_filter(f, iterable):
    if f:
        print("x for x in iterable if f(x)", (x for x in iterable if f(x)))
    return (x for x in iterable if x)