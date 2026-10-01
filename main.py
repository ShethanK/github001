#Monthly Expenses
class Expenses():
    salary=50000
    def __init__(self):
        self.food=""
        self.travel=""
        self.rent=""
        self.others=""
    def display(self):
        expensive=self.food+self.travel+self.rent+self.others
        print("Your Savings",self.salary-expensive)
a=Expenses()
a.food=int(input("Monthly costs for Food:"))
a.travel=int(input("Monthly Travel Expensive:"))
a.rent=int(input("Monthly Rent:"))
a.others=int(input("Monthly Other Expensis:"))
a.display()

