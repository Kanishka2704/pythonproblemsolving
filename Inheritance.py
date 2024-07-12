#Inheritance(super)
class Employee:
     def __init__(self,name,salary):
        self.name = name
        self.salary = salary
     def display_employee_info(self):
         print(f"Employee name: {self.name}\nEmployee salary: {self.salary}")

class Manager(Employee):
      def __init__(self,name,salary,department):
          super().__init__(name,salary)
          self.department = department
      def display_employee_info(self):
          super().display_employee_info()
          print(f"Employee department: {self.department}")


obj1 = Manager("Kanishka",20000,"Development")
obj1.display_employee_info()

#Inheritance(multi-level inheritance)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person_info(self):
        print(f"Person's name: {self.name}\nPerson's age: {self.age}")

class Employee(Person):
     def __init__(self,name,age,employee_id):
         super().__init__(name,age)
         self.employee_id = employee_id
     def display_employee_info(self):
         super().display_person_info()
         print(f"Employee id: {self.employee_id}")

class Manager(Employee):
    def __init__(self,name,age,employee_id,department):
         super().__init__(name,age,employee_id)
         self.department = department
    def display_department_info(self):
        super().display_employee_info()
        print(f"Department: {self.department}")

obj1 = Manager("Kanishka",23,1001,"Development")
obj1.display_department_info()

#Inheritance(hierachial inheritance)
class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type
    def display_type_info(self):
        print(f"Vehicle type:{self.vehicle_type}")
class Car(Vehicle):
    def __init__(self,vehicle_type,carbrand,carmodel,carcolor):
        super().__init__(vehicle_type)
        self.carbrand = carbrand
        self.carmodel = carmodel
        self.carcolor = carcolor

    def display_car_info(self):
        super().display_type_info()
        print(f"Carbrand: {self.carbrand}\nCarmodel:{self.carmodel}\nCarcolor:{self.carcolor}")

class Bike(Vehicle):
    def __init__(self,vehicle_type,bikebrand,bikemodel,bikecolor):
        super().__init__(vehicle_type)
        self.bikebrand = bikebrand
        self.bikemodel = bikemodel
        self.bikecolor = bikecolor
    def display_bike_info(self):
        super().display_type_info()
        print(f"Bikebrand: {self.bikebrand}\nBikemodel:{self.bikemodel}\nBikecolor:{self.bikecolor}")

vehicle1 =Car("Car","KIA","Seltos","white")
vehicle1.display_car_info()
vehicle2 =Bike("Bike","Yamaha","FascinoS","Black")
vehicle2.display_bike_info()

#inheritance-super method
class Animal:
    def speak(self):
        print("Animal Speaks")
class Dog(Animal):
     def speak(self):
         super().speak()
         print("Dog Barks")

animal = Dog()
animal.speak()

#inheritance-single inheritance-super
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person_info(self):
        print(f"Person's name: {self.name}\nPerson's age: {self.age}")
class Student(Person):
      def __init__(self,name,age,student_id):
          super().__init__(name,age)
          self.student_id = student_id
      def display_student_info(self):
         super().display_person_info()
         print(f"Student id: {self.student_id}")

student1 = Student("Kanishka",23,1021)
student1.display_student_info()

#inheritance -multiple inheritance
class A:
    def show(self):
      print("This is the baseclass1")

class B:
    def show(self):
      print("This is the baseclass2")
class C(A,B):
      def show(self):
          A.show(self)
          B.show(self)
obj = C()
obj.show()
     
        
