import psycopg

continueProgram = True
choice = 0

# Retreives all students from the 3005_Assignment_03 database
def getAllStudents():
    try:
        # Attempt to connect to the 3005_Assignment_03 database
        connection = psycopg.connect("dbname=3005_Assignment_03 user=postgres password=ILove3005")
    except BaseException:
        # Print an error if the database could not be connected to
        print("ERROR! Could not connect to database")
    else:
        cursor = connection.cursor() # Creates a cursor which allows us to run queries on the database

        cursor.execute("SELECT * FROM students") # Gets all students from the database
        print(cursor.fetchall()) # Prints all students retreived in the previous line
        connection.close() # Closes the connection to the database


# Adds a student to the 3005_Assignment_03 database
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        # Attempt to connect to the 3005_Assignment_03 database
        connection = psycopg.connect("dbname=3005_Assignment_03 user=postgres password=ILove3005")
    except BaseException:
        # Print an error if the database could not be connected to
        print("ERROR! Could not connect to database")
    else:
        cursor = connection.cursor() # Creates a cursor which allows us to run queries on the database
        
        cursor.execute("INSERT INTO students (student_id, first_name, last_name, email, enrollment_date) VALUES (DEFAULT, '" + first_name + "', '" + last_name + "', '" + email + "', '" + enrollment_date + "');") # Inserts a student to the database using function parameters
        connection.commit() # Commits changes made by the cursor to the database
        connection.close() # Closes the connection to the database


# Updates a student from the 3005_Assignment_03 database
def updateStudentEmail(student_id, new_email):
    try:
        # Attempt to connect to the 3005_Assignment_03 database
        connection = psycopg.connect("dbname=3005_Assignment_03 user=postgres password=ILove3005")
    except BaseException:
        # Print an error if the database could not be connected to
        print("ERROR! Could not connect to database")
    else:
        cursor = connection.cursor() # Creates a cursor which allows us to run queries on the database
        
        cursor.execute("UPDATE students SET email = '" + new_email + "' WHERE student_id = " + str(student_id) + ";") # Updates a student's email in the database using function parameters
        connection.commit() # Commits changes made by the cursor to the database
        connection.close() # Closes the connection to the database


# Deletes a student from the 3005_Assignment_03 database
def deleteStudent(student_id):
    try:
        # Attempt to connect to the 3005_Assignment_03 database
        connection = psycopg.connect("dbname=3005_Assignment_03 user=postgres password=ILove3005")
    except BaseException:
        # Print an error if the database could not be connected to
        print("ERROR! Could not connect to database")
    else:
        cursor = connection.cursor() # Creates a cursor which allows us to run queries on the database
        
        cursor.execute("DELETE FROM students WHERE student_id = " + str(student_id) + ";") # Deletes a student from the database using function parameters
        connection.commit() # Commits changes made by the cursor to the database
        connection.close() # Closes the connection to the database


# Main program loop
while(continueProgram):
    print("\nSelect a function to perform... 0: QUIT PROGRAM 1: getAllStudents 2: addStudent 3: updateStudentEmail 4: deleteStudent")
    choice = input("YOUR CHOICE: ")

    if(choice == "0"):
        # End the while loop, and therefore end the program
        continueProgram = False
    elif(choice == "1"):
        getAllStudents()
    elif(choice == "2"):
        # Get user input for all parameters to addStudent() and run the function
        addStudent(input("STUDENT FIRST NAME: "), input("STUDENT LAST NAME: "), input("STUDENT EMAIL: "), input("STUDENT DATE OF ENROLLMENT: "))
    elif(choice == "3"):
        # Get user input for all parameters to updateStudentEmail() and run the function
        updateStudentEmail(input("STUDENT ID: "), input("NEW STUDENT EMAIL: "))
    elif(choice == "4"):
        # Get user input for all parameters to deleteStudent() and run the function
        deleteStudent(input("STUDENT ID: "))
    else:
        # Print and error when the user has not entered a number from 0-4
        print("INVALID INPUT! ENTER A NUMBER FROM 0-4")
