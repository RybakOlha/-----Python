def geometric_progression(start, ratio, cnt):
    """
    >>> for i in geometric_progression(1, 2, 3):
    ...     print(i)
    1
    2
    4
    >>> for i in geometric_progression(0, 2, 3):
    ...     print(i)
    ...
    1
    0
    0
    >>> for i in geometric_progression(1, 1, 3):
    ...     print(i)
    ...
    1
    1
    1
    >>> for i in geometric_progression(2, 2, 2):
    ...     print(i)
    ...
    2
    4
    """    
    value = start
    for i in range(cnt):
        yield value
        value *= ratio


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    