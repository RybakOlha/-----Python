class String(str):
    
    def __add__(self, other):
        return String(str(self) + str(other))
    
    def __radd__(self, other):
        return String(str(other) + str(self))
    
    def __sub__(self, other):
            return String(str(self).replace(str(other), '', 1))
    
    
r = String("fghj66666kl")
print(r + None)
print(r - 'fgh')
print(None + r)