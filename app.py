class Person:
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID

def main():
    person = Person("Diego", 23, "ABCD1")
    print("Nombre:", person.name)
    print("Edad:", person.age)
    print("ID:", person.ID)

if __name__ == "__main__":
    main()
