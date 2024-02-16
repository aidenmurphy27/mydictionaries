#create dictionary
student = {'name':'Aiden Murphy',
           'age':'20', 
           'major':'Finance/MIS',
           'hobbies':'Guitar, Basketball, Video Games'}

#add to dictionary
student['state'] = 'Texas'

#change age
student['age'] = int(student['age']) + 1

for key in student:
    print(f"The student's {key} is: {student[key]}")