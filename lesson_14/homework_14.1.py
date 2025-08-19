class Student:
    def __init__(self, name, surname, age, average_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_mark = average_mark

    def get_average_mark(self, marks_list):
        self.average_mark = int(sum(marks_list)/len(marks_list))
        return self.average_mark


student = Student(name="Boris", surname="Doroshenko", age="25", average_mark=None)

print(student.name+' '+student.surname)
print(student.age)

Boris_marks = [10, 7, 11, 9, 6, 12, 10, 11, 8, 8]
student.get_average_mark(Boris_marks)

print(f'The average mark for {student.name} {student.surname} is {student.average_mark}')
