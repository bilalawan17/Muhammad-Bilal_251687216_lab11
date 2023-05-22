#Muhammad Bilal
#Lab 11
#251687216

#Q1

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def area(self):
        a, b = self.sides
        return (a * b)/2


class Circle(Shape):
    def __init__(self, radius):
        super().__init__([])
        self.radius = radius

        def area(self):
            return pi*self.radius**2

def main():

    triangle_sides = [6, 9]
    circle_radius = 7.5

    triangle = Triangle(triangle_sides)
    circle = Circle(circle_radius)

    triangle_area = triangle.area()
    circle_area = circle.area()

    print("Triangle area:", triangle_area)
    print("Circle area:", circle_area)

main()


#Q2

class employee:

    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = None

    def get_salary_status(self):
        return self.salary


class BuildingManager(employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id)
        self.salary = 10000


class ProcurementManager(employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id)
        self.salary = 12000


class LogisticsManager(employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id)
        self.salary = 15000


def main():
    employees = [
        BuildingManager("Imran Ali", "BM012"),
        ProcurementManager("Omer Saif", "PM231"),
        LogisticsManager("Sami Aslam", "LM901")
    ]

    for employee in employees:
        print("Employee Name:", employee.emp_name)
        print("Employee ID:", employee.emp_id)
        print("Salary:", employee.get_salary_status())
        print()

main()
