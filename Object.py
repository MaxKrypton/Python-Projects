class students:
    all = []
    def __init__(self, name, age, grade, rank):
        
        # Validation
        
        assert age >= 0, f" The age {age} is less than zero "
        
        # assignn to self object
        
        self.name = name
        self.age = age
        self.grade = grade
        self.rank = rank
        
        # adding all attributes into one list
        students.all.append(self)
    
    # The __repr__ whiich allows you to represent your list in a good way
    
    def __repr__(self):
        return f"students({self.name}, {self.age}, {self.grade}, {self.rank})"
    
student1 = students("Quentin", 20, "Freshman", 2)
student2 = students("Tamara", 20, "Junior", 1)
student3 = students("Alain", 21, "Swathmore", 1)
student4 = students("Merlyne", 21, "Junior", 2)

print(students.all)

for i in students.all:
    print(i)