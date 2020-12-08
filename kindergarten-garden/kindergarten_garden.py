class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagrams = diagram.split("\n")
        self.students = students

    def plants(self, student):
        all_plants = []
        plant_names = []
        name_index = self.students.index(student)
        for diagram in self.diagrams:
          all_plants.append(diagram[name_index*2: name_index*2 + 2])
        for row in all_plants:
          for plant in row:
            plant_names.append(self.plant_name(plant))
        return plant_names


    def plant_name(self, letters):
        for letter in letters:
          if letter == "G":
            return "Grass"
          elif letter == "C":
            return "Clover"
          elif letter == "R":
            return "Radishes"
          else:
            return "Violets"


classroom = Garden("VCRRGVRG\nRVGCCGCV",  students=["Samantha", "Patricia", "Xander", "Roger"])

print(classroom.plants("Xander"))
