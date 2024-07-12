class Person:
    people = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.append(self)
    
    def __str__(self):
        return f'{self.name} - {self.age}'
    
    @classmethod
    def list_people(cls):
        print(f'{"*** Name ***".ljust(25)} | {"*** Age ***"}')
        for person in cls.people:
            print(f'{person.name.ljust(25)} | {person.age}')

person_1 = Person('Mew Suppasit', 30)
person_2 = Person('Alice', 25)
person_3 = Person('Singto Prachaya', 35)
person_4 = Person('Bright', 27)
person_5 = Person('Mallory', 45)
person_6 = Person('Ronaldo Adriano', 35)

Person.list_people()
