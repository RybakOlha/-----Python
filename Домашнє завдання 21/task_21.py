class String(str):
    
    def __init__(self, value):
        super().__init__()
        
    def __add__(self, other):
        return String(str(self) + str(other))
    
    def __radd__(self, other):
        return String(str(other) + str(self))
    
    def __sub__(self, other):
        if isinstance(other, str):
            return String(str(self).replace(other, '', 1))
        else:
            return String(str(self).replace(str(other), '', 1))

str1 = String("fghj66666kl")
print(str1 + None)
print(7 + str1)
print(str1 - 6)