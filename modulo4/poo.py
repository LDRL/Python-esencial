# Programacion orientada a objetos
# Encapsulamiento
# Abstraccion
# Inheritance
# Polimorfismo

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print('Hello, my name is {} and I am {} yearss old'.format(self.name, self.age))

if __name__ == '__main__':
    person = Person('L', 27)

    print('Age:{}'.format(person.age))
    person.say_hello()