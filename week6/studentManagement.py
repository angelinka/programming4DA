
#Author: Angelina B

# Write a function that prints out a menu of commands we can perform, ie add,
#view and quit. The function should return what the user chose.

def menu():
    print ('What would you like to do?\n (a) Add new student \n (v) View students\n (q) Quit')
    choice = input('Type one letter (a/v/q): ')
    #testing that function works:
    print ('you chose', choice)
    return choice

#Create a program that keeps displaying the
# menu until the user picks q. if the user chooses a then call a function called
# doAdd() if the user chooses v then call a function called doView().    
def adding():
    student = {}
    student["name"] = input("enter student's name: ")
    student["modules"] = readModules()
    students.append(student)
    print(students)

def readModules():
    modules = []
    moduleName =  input('enter the first Module name (blank to quit): ')

    while moduleName != "":
        module = {}
        module['name'] = moduleName
        module['grade'] = int(input('enter grade: '))
        modules.append(module)
        moduleName =  input('enter next module name (blank to quit): ')

    return modules

def viewing():
    print ('in viewing')

#main program
students = []
choice = menu()

while (choice != 'q'):
    if choice == 'a':
        adding()
    elif choice == 'v':
        viewing()
    else:
        print ('Please seelect either a, v or q')
    choice = menu()
