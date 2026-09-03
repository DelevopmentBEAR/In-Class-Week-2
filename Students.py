class Student: # defines a class called Student
    def __init__(self, name, school_id, gpa): # initializes the Student object with a name and school ID and GPA
        self.name = name # stores the name in the instance variable 'name'
        self.school_id = school_id # stores the school ID in the instance variable 'school_id'
        self.gpa = gpa # stores the GPA in the instance variable 'gpa'

    def __str__(self): # defines a method that returns a string representation of the Student object
        return f'Student Name: {self.name}, School ID: {self.school_id}, GPA: {self.gpa}' # returns a string that includes the name, school ID, and GPA of the Student object

# Example usage of the Student class
alex = Student('Alex', 'abcdef', 3.4)
print(alex.name) # <- prints 'Alex'
print(alex.school_id) # <- prints 'abcdef'
print(alex) # <- prints 'Student Name: Alex, School ID: abcdef, GPA: 3.4'

sam = Student('Sam', 'ghijkl', 3.7)
print(sam) # <- prints 'Student Name: Sam, School ID: ghijkl, GPA: 3.7'

mark = Student('Mark', 'mnopqr', 2.5)
print(mark) # <- prints 'Student Name: Mark, School ID: mnopqr, GPA: 2.5'