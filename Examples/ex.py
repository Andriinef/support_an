class Data:
    def __radd__(self, other):
        return "finxter 42"


x = Data()
y = Data()

x += y

print(x)
# finxter 42
