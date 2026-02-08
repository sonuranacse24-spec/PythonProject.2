students = {}

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Search Student")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        students[sid] = name
        print("Student Added")

    elif choice == "2":
        print("Student List:")
        for sid, name in students.items():
            print(sid, "-", name)

    elif choice == "3":
        sid = input("Enter ID to update: ")
        if sid in students:
            students[sid] = input("Enter new name: ")
            print("Updated")
        else:
            print("Student not found")

    elif choice == "4":
        sid = input("Enter ID to delete: ")
        if sid in students:
            del students[sid]
            print("Deleted")
        else:
            print("Student not found")

    elif choice == "5":
        key = input("Enter ID or Name: ")
        for sid, name in students.items():
            if sid == key or name == key:
                print("Found:", sid, name)

    elif choice == "6":
        break

    else:
        print("Invalid choice")
