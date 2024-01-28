# WAPP to find out the min value and max value from a list without
# using library function use only loop
# WAPP to calculate the sum of diagonal a matrix using loop

marks=[56, 90, 76, 80, 93.98]
marks[3]=10
# print(marks)
# for item in marks:
#     print(item)

# for i in range(0,5):
#     print(marks[i])

m=[[1, 2, 3],[4, 5, 6], [7, 8, 9]]

# print(m)
s=0
for i in range(0,3):
    for j in range(0,3):
        if i==j:
            s=s+m[i][j]
            print(m[i][j], end=" ")
        else:
            print("-", end=" ")
    print("")
print("Sum of diagonal is",s)

# for k in m:
#     print(k)
    # for item in k:
    #     print(item, end=" ")
    # print("")