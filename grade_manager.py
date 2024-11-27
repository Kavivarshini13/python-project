class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # A list to store grades for the student

    def add_grade(self, grade):
        
        if grade < 0 or grade > 100:
            print("Invalid grade. It should be between 0 and 100.")
        else:
            self.grades.append(grade)

    def get_average(self):
       
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_passed(self):
       
        return self.get_average() >= 50

    def __str__(self):
        
        average = self.get_average()
        status = "Passed" if self.is_passed() else "Failed"
        return f"{self.name} - Grades: {self.grades}, Average: {average:.2f} ({status})"


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
       
        student = Student(name)
        self.students.append(student)

    def add_student_grade(self, name, grade):
       
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                print(f"Grade {grade} has been added for {name}.")
                return
        print(f"Student {name} not found.")

    def get_student_report(self, name):
       
        for student in self.students:
            if student.name == name:
                print(student)
                return
        print(f"Student {name} not found.")

    def get_all_reports(self):
       
        if not self.students:
            print("No students in the system.")
            return
        print("\nGrade Reports:")
        for student in self.students:
            print(student)

