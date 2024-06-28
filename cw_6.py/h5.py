class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id


person1 = Person(name="Alice", age=30)
student1 = Student(name="Bob", age=20, student_id="12345")

print(f"{person1.name} is {person1.age} years old.")
print(f"{student1.name} is a student with ID {student1.student_id}.")
