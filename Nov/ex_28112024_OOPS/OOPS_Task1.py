# Research about the OOPs concepts
#
# Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods
#
# Use PC - to set the value of the attributes
#
# create a Print student information method/function

# Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods

class pyATB:
    Name = None
    City = None
    Role = None
    Company = None
    Exp = None

    def __init__(self, name, city, role, company, exp):
        self.Name = name
        self.City = city
        self.Role = role
        self.Company = company
        self.Exp = exp

    def Student_info(self):
        print(f"Student name {self.Name} , City {self.City}, Role{self.Role}, Company{self.Company}, Experience{self.Exp}")


thiyaga = pyATB("Thiyagarajan", "Chennai", "QA", "Sathaga", "2 Years")
thiyaga.Student_info()