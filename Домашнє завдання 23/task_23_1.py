def geometric_progression(start, ratio):
    value = start
    while True:
        yield value
        value *= ratio


n = int(input())
cnt = 0
for i in geometric_progression(1, 2):
    if cnt < n:
      print(i)
    else:
      break
    cnt += 1