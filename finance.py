def money():
    return (
        "---------------------------------\n"
        f"Salary:                    ${salary}\n"
        f"Expenses:                  ${amount}\n"
        f"Money in favor:            ${total}\n"
        f"percentage of salary used: {percentage:.1f}%\n"
        "---------------------------------"
    )


while True:
    try:
        salary = int(input("Enter your monthly net salary: $"))
        if salary >= 0:
            break

    except ValueError:
        print("Please enter numbers only")

amount = 0

while True:
    try:
        worth = int(input("Enter the expense (When finished, enter: 0): $"))
        if worth == 0:
            break

    except ValueError:
        print("Please enter numbers only")

    amount += worth

total = salary - amount
percentage = (amount / salary) * 100

print(money())
