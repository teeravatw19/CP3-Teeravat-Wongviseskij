def showBill():
    print("---- My Food ----")
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])

def total():
    sum = 0
    for i in range(len(priceList)):
        sum += priceList[i]
    print(f"Total price : {sum} Baht")

menuList = []
priceList = []
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
total()