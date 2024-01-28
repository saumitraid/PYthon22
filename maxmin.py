marks=[]
nos=int(input("Enter no of students:-"))
for i in range(0,nos):
    m=int(input("Enter %d student's marks:-"%(i+1)))
    marks.append(m)
mn=marks[0]
mx=marks[0]
for i in range(1, nos):
    if mn>marks[i]:
        mn=marks[i]
    if mx<marks[i]:
        mx=marks[i]

print("The min =",mn)
print("The max =",mx)

print(marks[2:])