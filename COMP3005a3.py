import psycopg2

conn_params = {
    'dbname': 'COMP3005a3',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost'
}

def connect():
    conn = None
    try:
        conn = psycopg2.connect(**conn_params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn

def getAllStudents():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    student_records = cur.fetchall()
    for row in student_records:
        print(row)
    cur.close()
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()
    cur.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    cur.close()
    conn.close()

def deleteStudent(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cur.close()
    conn.close()


def main():
    while True:
        print("\nStudent Database Management")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Update Student Email")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
            print("Student added successfully.")

        elif choice == '2':
            print("Fetching all students...")
            getAllStudents()

        elif choice == '3':
            student_id = int(input("Enter student ID to update email: "))
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
            print("Email updated successfully.")

        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            deleteStudent(student_id)
            print("Student deleted successfully.")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()