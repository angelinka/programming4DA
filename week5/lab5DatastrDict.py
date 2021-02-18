#program stores a student name and a list of her courses and
# grades in a dict, the program should then print out her data.

student = {
    'name': 'Mary',
    'courses': [
        {'courseName': 'Programming',
        'grade': 45},
        {'courseName': 'History',
        'grade': 99}
    ]
}

print ('Student:', student['name'])

#printing out courseName and grade using for loop
for course in student['courses']:
    print ('\t', course['courseName'], '\t:', course['grade'])