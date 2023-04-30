def geometric_progression(start, ratio, cnt):   
    value = start
    for i in range(cnt):
        yield value
        value *= ratio


if __name__ == "__main__":
    import doctest
    doctest.testfile('1.txt')
   
