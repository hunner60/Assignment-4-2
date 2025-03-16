
# Input the employee's name, total transaction value, number of transactions, and shifts worked
employee_name = input("Enter the employee's name: ")
num_shifts = int(input("Enter the number of shifts worked: "))
num_transactions = int(input("Enter the number of transactions: "))
total_value = float(input("Enter the total dollar value of transactions: "))


# Calculate the productivity score
productivity_score = (total_value / num_transactions) / num_shifts

# Initialize bonus
bonus = 0

# Determine the bonus based on the productivity score using if-else statements
if productivity_score <= 30:
    bonus = 50.00
elif productivity_score <= 69:
    bonus = 75.00
elif productivity_score <= 199:
    bonus = 100.00
else:
    bonus = 200.00

# Output the employee's name, productivity score, and bonus
print(f"Employee: {employee_name}")
print(f"Productivity Score: {productivity_score:.2f}")
print(f"Bonus: ${bonus:.2f}")

