database = (["Gor", 500, "2599"],["Hayk", 0, "1122"],["Garik", 0, "1234"])
logined = False

while True:
    password = input("Please enter your password: ")
    for x in range(0, len(database)):
        if password == database[x][2]:


            print()
            while True:
                logined = True

                print('-' * 25)
                print(f'Welcome ! {database[x][0]}')
                print('-' * 25)
                print('Check balance - B')
                print('Cash In - (+)')
                print('Cash Out - (-)')
                print('Exit - E')
                print('Transaction - T')
                print('-' * 25)
                while True:
                    command = input("please enter command => ")
                    if command == "B":
                        print(f'Your balance {database[x][1]}')

                    elif command == "+":
                        cash_in = int(input("Enter sum: "))
                        if cash_in <= 0:
                            print("invalid sum, try again.")
                        else:
                            database[x][1] += cash_in
                            print("Operation completed!")

                    elif command == "-":
                        cash_out = int(input("Enter sum: "))
                        if cash_out <= 0 or cash_out < database[x][1]:
                            print("Invalid sum, try again")
                        else:
                            database[x][1] -= cash_out
                            print("Operation completed!")

                    elif command == "E":
                        print("EXIT")
                        break

                    elif command == "T":
                        user_id = int(input('Enter user id =>> '))
                        if user_id < 0 or user_id == x or user_id >= len(database):
                            print('Invalid id !')
                        else:
                            sum = int(input('Enter sum =>> '))
                            if sum <= 0 or database[x][1] < sum:
                                print('Invalid sum !')
                            else:
                                database[x][1] -= sum
                                database[user_id][1] += sum
                                print("Operation completed!")
                break



        elif x == len(database) - 1:
            print("Invalid password, try again.")