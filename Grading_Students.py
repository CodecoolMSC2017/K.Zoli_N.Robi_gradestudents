import sys

def solve(grades):
        temp =[]
        for i in range(n):
           if grades[i] > 37:
               if grades[i]%5 == 1:
                   grades[i] = grades[i] -1
                   temp.append(grades[i])
               elif grades[i]%5 == 2:
                   temp.append(grades[i])
               elif grades[i]%5 == 3:
                   grades[i] = grades[i] +2
                   temp.append(grades[i])
               elif grades[i]%5 == 4:
                   grades[i] = grades[i] +1
                   temp.append(grades[i])
           else:
               temp.append(grades[i])
        grades = temp
        return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
