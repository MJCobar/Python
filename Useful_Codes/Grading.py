StudentList = ["Bob","Sarah","Corey","Lindsey","Pablo","Terrance","Max","Yvette"]
GradesAssign1 = [90.0,85.4,74.0,45.0,100.0,86.2,74.0,92.5]
GradesAssign2 = [100.0,92.3,82.5,65.5,78.2,68.5,76.1,92.5]
GradesAssign3 = [94.4,88.7,68.8,71.1,80.6,73.4,84.9,76.5]

for x in range(len(StudentList)):
    StudentName = StudentList[x]
    StudentAvg = (GradesAssign1[x] + GradesAssign2[x] + GradesAssign3[x])/3.0
    StudentMin = min(GradesAssign1[x],GradesAssign2[x],GradesAssign3[x])
    StudentMax = max(GradesAssign1[x],GradesAssign2[x],GradesAssign3[x])
    print("Student Name: {}, Average Grade: {}, Lowest Grade: {}, Highest Grade: {}".format(StudentName,StudentAvg,StudentMin,StudentMax))