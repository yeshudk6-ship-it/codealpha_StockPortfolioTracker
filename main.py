# -------------------------------
# CodeAlpha Internship
# Task 2 - Stock Portfolio Tracker
# -------------------------------

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 195
}

portfolio = {}

print("=" * 50)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

print("\nEnter 'done' when finished.\n")

# Take user input
while True:

    stock = input("Enter Stock Symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from the available list.\n")
        continue

    try:
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

    except ValueError:
        print("Please enter a valid number.\n")
        continue

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print("Added Successfully!\n")

# Display Portfolio
print("\n")
print("=" * 50)
print("YOUR PORTFOLIO")
print("=" * 50)

total = 0

file = open("portfolio.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("=" * 40 + "\n")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]

    investment = price * quantity

    total += investment

    print(f"{stock} | Qty: {quantity} | Price: ${price} | Total: ${investment}")

    file.write(
        f"{stock} | Qty: {quantity} | Price: ${price} | Total: ${investment}\n"
    )

print("-" * 50)
print(f"Total Investment = ${total}")

file.write("-" * 40 + "\n")
file.write(f"Total Investment = ${total}")

file.close()

print("\nPortfolio saved successfully as 'portfolio.txt'")
print("\nThank you for using Stock Portfolio Tracker!")