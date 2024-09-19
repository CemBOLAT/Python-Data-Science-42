def ft_filter(f, iterable):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if f:
        return (item for item in iterable if f(item))
    return (x for x in iterable if x)
