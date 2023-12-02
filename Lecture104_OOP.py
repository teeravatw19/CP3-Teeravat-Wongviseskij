class Customer:
    Fname = ""
    Lname = ""
    age = 0

    def addCart(self):
        print(f"Added product to {self.Fname} {self.Lname}({self.age})'s cart")

customer1 = Customer()
customer1.Fname = "Teeravat"
customer1.Lname = "Wongviseskij"
customer1.age = 18
customer1.addCart()

customer2 = Customer()
customer2.Fname = "A"
customer2.Lname = "B"
customer2.addCart()

customer3 = Customer()
customer3.Fname = "C"
customer3.Lname = "D"
customer3.addCart()