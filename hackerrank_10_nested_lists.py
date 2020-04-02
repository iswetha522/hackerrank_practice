# Given the names and grades for each student in a 
# Physics class of N students, store them in a nested list
# and print the name(s) of any student(s) having the 
# second lowest grade.

# Note: If there are multiple students with the same grade, 
# order their names alphabetically and print each name 
# on a new line.

# Input Format

# The first line contains an integer,N,the number of students.
# The 2N subsequent lines describe each student over 2 lines; 
# the first line contains a student's name, and 
# the second line contains their grade.

# Constraints
# * 2 <= N <= 5
# * There will always be one or more students 
# having the second lowest grade.

# Output Format

# Print the name(s) of any student(s) having the 
# second lowest grade in Physics; if there are multiple 
# students, order their names alphabetically and 
# print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and 
# grades are assembled to build the following list:

# python 
# students = [['Harry', 37.21], 
#            ['Berry', 37.21], 
#            ['Tina', 37.2], 
#            ['Akriti', 41], 
#            ['Harsh', 39]]

# The lowest grade of 37.2 belongs to Tina. 
# The second lowest grade of 37.21 belongs to both 
# Harry and Berry, so we order their names 
# alphabetically and print each name on a new line.
students = []
score_arr = []
sorted_names_arr = []
for _ in range(int(input("Enter number of students: "))):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    students.append([name,score])
for i in range(len(students)):
    for j in range(1,2):
        score_arr.append(students[i][j])
min_score = min(score_arr)
for i in range(len(students)):
    for j in range(1,2):
        if min_score == min(score_arr):
            score_arr.remove(min_score)
new_min_score = min(score_arr)
for i in range(len(students)):
    for j in range(1,2):
        if students[i][j] == new_min_score:
            sorted_names_arr.append(students[i][0])
sorted_names_arr.sort()
print("\n".join(sorted_names_arr))   


# My way of writing the program:
# students = [['Harry', 37.21], 
#            ['Berry', 37.21], 
#            ['Tina', 37.2], 
#            ['Akriti', 41], 
#            ['Harsh', 39]]
# score_arr = []
# sorted_names_arr = []
# for i in range(len(students)):
#     for j in range(1,2):
#         score_arr.append(students[i][j])
# min_score = min(score_arr)
# if min_score == min(score_arr):
#     score_arr.remove(min_score)
# print(score_arr)
# new_min_score = min(score_arr)
# print(new_min_score)
# for i in range(len(students)):
#     for j in range(1,2):
#         if students[i][j] == new_min_score:
#             sorted_names_arr.append(students[i][0])

# sorted_names_arr.sort()
# print("\n".join(sorted_names_arr))