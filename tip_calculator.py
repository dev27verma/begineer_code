print("Welcome To Tip Calculator")
bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
person = int(input("How many people to split the bill: "))

print(f"Each person should pay: Rs. {round(((bill + tip_percentage/100 * bill)/person),2)}")