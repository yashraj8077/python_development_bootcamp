class Box:
    def __init__(self, value):
        self.value = value

    def __str__(self):     # print()
        # return f"Box({self.value})"
        return 'champa'

    def __len__(self):     # len()
        return len(self.value)

b = Box("hello")
print(b)        # Box(hello)
print(len(b))   # 5
print(str(b))
