class Box:
    def __init__(self, rohit):
        self.superman = rohit

    def greet(self):
        return f'{self.superman} Hello, how are you?'
    
    @property
    def new_name(self):
        return self.superman


# b = Box('Harish')
# c = Box('Rajat')
d = Box('rohit')
print(f'how are you bhai this is me')

print(d.greet())
print(d.new_name)

# Class object instantiation
# Syntax >> variablename = className(self values)

# print(b)
# print(b.superman)
# print(c.superman)
# print(c.greet())

# a = 67
# print(type(a))
# a = str(a)
# print(type(a))