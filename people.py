from interface import out, get_cmd

people = {}

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        out("Hello there!")

def create_person(name):
    people[name] = Person(name)
    return people[name]

per = create_person("King Daddy")