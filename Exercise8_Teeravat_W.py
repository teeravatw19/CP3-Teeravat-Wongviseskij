u = input("Username : ")
p = input("Password : ")
if u == "admin" and p == "1234":
    print("-----------Borntodev School-----------")
    print("1. Complete Python3 Programming : 2,990")
    print("2. Complete Java Programming : 1,990")
    print("3. Fundamental Web Dev with HTML5 & CSS3 : 690")
    order = int(input("Choose some course : "))
    if order == 1:
        amount = int(input("How many do you want? : "))
        print(f"{2_990 * amount} Baht")
    elif order == 2:
        amount = int(input("How many do you want? : "))
        print(f"{1_990 * amount} Baht")
    elif order == 3:
        amount = int(input("How many do you want? : "))
        print(f"{690 * amount} Baht")
    else:
        print("We don't have it, sorry :(")
else:
    print("Invalid username or password, please try again.")