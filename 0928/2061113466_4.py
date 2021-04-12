grade=[]
grade.append([int(input()), int(input()), int(input())])
grade.append([int(input()), int(input()), int(input())])
grade.append([int(input()), int(input()), int(input())])

stu={1:grade[0], 2:grade[1], 3:grade[2]}
student=int(input())
gra=stu.get(student)
gra.sort()

print(gra, gra[2],gra[0])
