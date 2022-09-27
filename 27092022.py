
# mini banking system
# deposit money
# withdraw money
# view bank statement

# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function


class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("You Withdrew:", amount)
		else:
			print("Insufficient balance")

	def display(self):
		print(" Net Available Balance=",self.balance)

s = Bank_Account()
while True:
	choice = int(input("enter "))
	if choice == 1:
		s.deposit()
	elif choice == 2:
		s.withdraw()
	elif choice == 3:
		s.display()






















# class company:
#     def __hello(self):
#         print ("hello")
#     def __init__(self):
#         print ("welcome to ws cube tech")
#
#
# obj = company()
# obj





# class companyA:
#     def employee1(self):
#         print ("the name of the employee 1 is John")
#     def employee2(self):
#         print ("the name of the employee 2 is Peter")
#
# class companyB:
#     def employee3(self):
#         print("the name of employee 3 is Lisa")
#     def employee4(self):
#         print ("the name of the employee 4 is David")
#
# class companyC(companyA,companyB):
#     def employee5(self):
#         print ("the name of the employee 5 is Rebecca")
#
# objA = companyA()
# objB = companyB()
# objC = companyC()
#
# objC.employee1()




# class company:
#     def __init__(self):#constructor
#         print("these are the employee details")
#         print("welcome to wscube tech")
#     def employee(self):
#         print ("the name of the employee is John")
#         print ("employee id = 123")
#     def employee1(self):
#         print("the name of the employee is Peter")
#         print ("employee id = 321")
#
# obj = company()
# obj.employee1()