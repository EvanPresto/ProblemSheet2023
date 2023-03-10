def student_menu():
    print('What would you like to do?')
    print('[a] Add new student')
    print('[b]View Students')
    print('[q] Quit')
    choice = input('Type one letter (a/v/q):')
    return choice
   
def add_student(students):
    currentStudent = {}
    currentStudent["name"]=input('Enter Name')
    currentStudent["modules"]=input('Enter module')
    students.append(currentStudent)
    print(students)



    
    
def viewstudent():
    print('Student Info')

choice = student_menu()
students =[]
while (choice !='q'):
    if choice == 'a':
        add_student(students)
    elif choice == 'b':
        viewstudent()
    elif choice != 'q':
        print('Type one letter (a/v/q):')
        choice = student_menu



