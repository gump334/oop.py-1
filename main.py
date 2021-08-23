class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #def __str__(self):
    #    return f"my name is {self.name}"

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

bob = Person("bob", 35)

print(bob.age)
print(bob)