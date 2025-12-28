class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if len(self.marks) == 0:
            return False
        avg = sum(self.marks) / len(self.marks)
        return avg > 50


student1 = Student("Agata Zygiert", [65, 76, 89])
student2 = Student("Adam Zyguś", [37, 28, 47])

print(student1.is_passed())
print(student2.is_passed())
