# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_to_int = int(age)
years_remaining = 90 - age_to_int

# Calculate days, weeks, and months to 90 years old
daysTo90 = 365 * years_remaining
weeksTo90 = 52 * years_remaining
monthsTo90 = 12 * years_remaining

# f string prints out all data types in brackets as strings
print(f"You have {daysTo90} days, {weeksTo90} weeks, and {monthsTo90} months left.")







