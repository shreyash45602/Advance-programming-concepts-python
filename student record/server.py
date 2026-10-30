import webbrowser

FILE_NAME = "students.txt"
HTML_FILE = "students.html"


# Function to add student record
def add_student():

    print("\n----- Student Registration -----")

    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")
    email = input("Enter Email: ")
    mobile = input("Enter Mobile No: ")

    # Open file in append mode
    with open(FILE_NAME, "a") as file:
        file.write(name + "|" + roll_no + "|" + email + "|" + mobile + "\n")

    print("\nRecord saved successfully!")


# Function to read student records
def read_students():

    students = []

    try:
        # Open file in read mode
        with open(FILE_NAME, "r") as file:

            for line in file:

                data = line.strip().split("|")

                if len(data) == 4:
                    students.append(data)

    except FileNotFoundError:

        print("\nNo records found.")

    return students


# Function to create HTML table
def create_html(students):

    html = """
<!DOCTYPE html>

<html>

<head>

<title>Student Records</title>

<style>

body {
    font-family: Arial;
    background-color: #f2f2f2;
    padding: 30px;
}

h1 {
    text-align: center;
    color: #333333;
}

table {
    width: 80%;
    margin: auto;
    border-collapse: collapse;
    background-color: white;
}

th {
    background-color: #007bff;
    color: white;
}

th, td {
    border: 1px solid #cccccc;
    padding: 12px;
    text-align: center;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

</style>

</head>

<body>

<h1>Student Records</h1>

<table>

<tr>
    <th>Name</th>
    <th>Roll No</th>
    <th>Email</th>
    <th>Mobile No</th>
</tr>
"""

    # Add each student as a table row
    for student in students:

        html += f"""
<tr>
    <td>{student[0]}</td>
    <td>{student[1]}</td>
    <td>{student[2]}</td>
    <td>{student[3]}</td>
</tr>
"""

    html += """
</table>

</body>

</html>
"""

    # Create HTML file
    with open(HTML_FILE, "w") as file:
        file.write(html)

    print("\nHTML table created successfully!")


# Main program
while True:

    print("\n==============================")
    print("     STUDENT MANAGEMENT")
    print("==============================")

    print("1. Add Student")
    print("2. View All Records")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        students = read_students()

        if students:

            create_html(students)

            # Open HTML file in browser
            webbrowser.open(HTML_FILE)

        else:

            print("\nNo student records available.")

    elif choice == "3":

        print("\nProgram closed.")
        break

    else:

        print("\nInvalid choice! Please enter 1, 2 or 3.")