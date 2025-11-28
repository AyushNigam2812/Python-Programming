#exam
m1= float(input("Enter marks of subject 1: "))
m2= float(input("Enter marks of subject 2: "))
m3= float(input("Enter marks of subject 3: "))
m4= float(input("Enter marks of subject 4: "))
m5= float(input("Enter marks of subject 5: "))

total = m1+m2+m3+m4+m5
average= total/5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)