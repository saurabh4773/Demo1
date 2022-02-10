while True:
    print("Menu \n1.Addition \n2.Subtraction \n3.Division \n4.Multilication \n5.Exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print("Addition is : ",num1+num2)
    elif choice == 2:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print("Subtraction is : ",num1-num2)
    elif choice == 3:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print("Division is : ",num1/num2)
    elif choice == 4:
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        print("Multiplication is : ",num1*num2)
    elif choice == 5:
        break
    else:
        print("Invalid choice")   