
# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

print("Available Stocks:", stock_prices)
print("-" * 40)

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available")
        continue
    
    quantity = int(input("Enter quantity: "))
    
    investment = stock_prices[stock] * quantity
    portfolio[stock] = investment
    total_investment += investment

print("\n📊 Portfolio Summary")
for stock, value in portfolio.items():
    print(f"{stock} : ₹{value}")

print("Total Investment: ₹", total_investment)

# Optional: save to file
save = input("Do you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        for stock, value in portfolio.items():
            file.write(f"{stock} : ₹{value}\n")
        file.write(f"Total Investment: ₹{total_investment}")
    print("✅ Data saved to portfolio.txt")
