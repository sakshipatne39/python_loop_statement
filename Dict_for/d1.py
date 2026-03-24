student = {
    "name" : "sakshi",
     "age" : 26 ,
     "course" : "python"
}
keyName = 'age'

print(student[keyName])

for stud in student :
    print(f"stud = {stud}, type of stude = {type(stud)} keyvalue = {student.get(stud)}")