# Student Login & Marks System

print("----- Welcome to Student Portal -----")
# LOGIN DATA = Stored
saved_user: dict[str, str] = {
    "username": "student1591574",
    "password": "adi@123"
}

# USER INPUT
username = input("Enter username: ")
password = input("Enter password: ")

# LOGIN CHECK
if username == saved_user["username"]:
    if password == saved_user["password"]:
        print("\nLogin Successful ✅")

        # STUDENT INFO
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")

        # MARKS INPUT
        marks = []
        m1 = float(input("Enter marks of Computer: "))
        m2 = float(input("Enter marks of Science: "))
        m3 = float(input("Enter marks of Maths: "))
        marks.append(m1)
        marks.append(m2)
        marks.append(m3)

        # CALCULATIONS
        total = sum(marks)
        percentage = total / 3

        # GRADE SYSTEM
        if percentage >= 80:
            grade = "A+"
        elif percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"

        # RESULTS
        print("\n----- RESULT -----")
        print("Name:", name.capitalize())
        print("Roll No:", roll_no)
        print("Marks:", marks)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)

        # STRING & SLICING EXTRA
        print("\n--- Extra Info ---")
        print("Name first 3 letters:", name[:3])
        print("Name reversed:", name[::-1])
    else:
        print("Wrong Password ❌")
else:
    print("Invalid Username ❌")