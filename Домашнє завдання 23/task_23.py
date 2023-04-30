class GeometricProgression:
    
    def __init__(self, start, ratio, cnt):
        self.start = start
        self.ratio = ratio
        self.current = start
        self.cnt = cnt
        self.step = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.current
        self.current *= self.ratio
        self.step += 1
        if self.step > self.cnt:
          raise StopIteration
        return value


n = int(input())
for i in GeometricProgression(1, 2, n):
    print(i)