grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
ave_grades = []
i = 0
while i < len(grades):
    if i < len(grades):
        ave_grades.append(sum(grades[i]) / len(grades[i]))
    i += 1
students = list(sorted(students))
print(dict(zip(students, ave_grades)))
