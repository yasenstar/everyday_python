print("Welcome to the tip calculator!")

bill = float(input("What is the total bill amount?\nBill($):"))
tip = int(input("How much tip percent would you like to give?\nTip%:"))
split = int(input("How many people to split the bill?\nNumber of People:"))

total_1 = (bill * (tip / 100) + bill) / split
print(f"Each person should pay (raw result): ${total_1}")

total_2 = ("{:.2f}".format((bill * (tip / 100) + bill) / split))
print(f"Each person should pay (formatted result): ${total_2}")

print("Each person should pay (formatted result): $", total_2)