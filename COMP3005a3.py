import psycopg2

# Connection parameters
connectionParameters = {
    'dbname': 'COMP3005a3',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost'
}

# Connect to the database
def connect():
    conn = None
    # Try to connect to the database
    try:
        conn = psycopg2.connect(**connectionParameters)
    # If an error occurs, print the error
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn

# Create the students table
def getAllStudents():
    # Connect to the database
    conn = connect()
    # Create a cursor object
    cur = conn.cursor()
    # Execute a select statement
    cur.execute("SELECT * FROM students")
    # Fetch all the rows from the result
    student_records = cur.fetchall()
    # Print the rows
    for row in student_records:
        print(row)
    cur.close()
    conn.close()

# Add a student to the students table
def addStudent(first_name, last_name, email, enrollment_date):
    # Connect to the database
    conn = connect()
    cur = conn.cursor()
    # Execute an insert statement
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    # Commit the transaction
    conn.commit()
    cur.close()
    conn.close()

# Update a student's email
def updateStudentEmail(student_id, new_email):
    # Connect to the database
    conn = connect()
    cur = conn.cursor()
    # Execute an update statement
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    # Commit the transaction
    conn.commit()
    cur.close()
    conn.close()

# Delete a student from the students table
def deleteStudent(student_id):
    # Connect to the database
    conn = connect()
    cur = conn.cursor()
    # Execute a delete statement
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    # Commit the transaction
    conn.commit()
    cur.close()
    conn.close()


# Main function
def main():
    # Main menu
    while True:
        print("\nStudent Database Management")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Update Student Email")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ")

        # Add new student
        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
            print("Student added successfully.")

        # Fetch all students
        elif choice == '2':
            print("Fetching all students...")
            getAllStudents()

        # Update student email
        elif choice == '3':
            student_id = int(input("Enter student ID to update email: "))
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
            print("Email updated successfully.")

        # Delete student
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            deleteStudent(student_id)
            print("Student deleted successfully.")

        # Exit the program
        elif choice == '5':
            print("Exiting program.")
            break
        
        # Invalid choice
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()