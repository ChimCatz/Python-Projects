# DAY 2 - TIP CALCULATOR
# Run: python .\Udemy_Projects\day_2_tipcalculator.py
# Related: Udemy_Projects\ (no helper files yet)

print("Hello, ChiggaHaxlord here! :)")
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? "))
percent_tip = float(
    input("What percentage tip would you like to give? 10, 12, or 15? ")
) / 100
people = int(input("How many people to split the bill? "))

# Each person should pay:
payment = (total_bill + (total_bill * percent_tip)) / people

print(
    f"If the bill was ${total_bill:.2f}, split between {people} people, "
    f"with {percent_tip * 100:.0f}% tip."
)
print(f"Each person should pay: ${payment:.2f}")
