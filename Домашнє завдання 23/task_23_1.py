def geometric_progression(start, ratio, cnt):
    value = start
    for i in range(cnt):
        yield value
        value *= ratio


n = int(input())
it = geometric_progression(1, 2, n)
for i in it:
      print(i)
   