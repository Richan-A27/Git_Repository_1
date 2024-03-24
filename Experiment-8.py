class Rectangle:
    def __init__(self, length, breadth):
        self.length = length 
        self.breadth = breadth
        
    def __str__(self):
        return f"Rectangle({self.length}, {self.breadth})"

R1 = Rectangle(100, 50)
R2 = Rectangle(200, 100)

R3 = Rectangle(R1.length + R2.length, R1.breadth + R2.breadth)

def compare(a, b):
    if a == b:
        return f"{a} is equal to {b}"
    elif a < b:
        return f"{a} is less than {b}"
    elif a > b:
        return f"{a} is greater than {b}"
    elif a >= b:
        return f"{a} is greater than or equal to {b}"
    elif a <= b:
        return f"{a} is less than or equal to {b}"
    else:
        return "Invalid comparison"

rec_dimension_1 = R1.length + R1.breadth
rec_dimension_2 = R2.length + R2.breadth

print("Result of comparison:",compare(rec_dimension_1, rec_dimension_2))



#Student info 
class Student:
    def __init__(self, regno, name, cgpa):
        self.regno = regno
        self.name = name
        self.cgpa = cgpa

    def get_regno(self):
        return self.regno

    def set_regno(self, regno):
        self.regno = regno

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cgpa(self):
        return self.cgpa

    def set_cgpa(self, cgpa):
        self.cgpa = cgpa

    def generate_report(self):
        report = f"Registration Number: {self.regno}\nName: {self.name}\nCGPA: {self.cgpa}"
        return report

# Create Student objects
student1 = Student("URK23CS0000", "Max", 8.8)
student2 = Student("URK23CS0001", "Santner", 9.5)

# Display reports
print("Student 1 Report:")
print(student1.generate_report())
print("\nStudent 2 Report:")
print(student2.generate_report())