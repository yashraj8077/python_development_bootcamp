# class NewClass:
#     uniform = 'blue'
    
#     def  __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def printName(self):
#         return self.name
    
#     def printId(self):
#         return self.id

#     def printInfo(self):
#         return f'My name is {self.name} and my Id is {self.id}'
    

# student1 = NewClass('Yash', 27645)
# student2 = NewClass('Paritosh', 27647)
# student3 = NewClass('Rajat', 34234)

# print(student1.printName())
# print(student1.printId())
# print(student2.printInfo())
# student3.name = 'Radha'
# print(student3.printInfo())

class Animal:
    def speak(self):
        return "Some sound"

# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return "Woof!"

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        # self.name = name
        self.breed = breed


d = Dog('Chandan', 'German shepherd')
print(d.name)
print(d.breed)
