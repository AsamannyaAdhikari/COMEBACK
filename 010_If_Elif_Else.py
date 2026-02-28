while True:
    try:
        a = int(input("Enter your age is: "))
        print("Your age is: ",a)

        if(a>18):
            print("You can drive.")
        else:
            print("You can't drive.")
    except ValueError:
        print("Invalid input! Please enter a number.")

    choise = input("Can you test again:(Yes/No): ").lower()
    if choise != "yes":
        print("Good Bye!")
        break    