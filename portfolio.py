import yfinance as yf
import json
import os

# File to store portfolio data
PORTFOLIO_FILE = "portfolio_data.json"

def load_portfolio():
    """Load the portfolio from the JSON file."""
    if os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, 'r') as file:
            return json.load(file)
    return 

def save_portfolio(portfolio):
    """Save the portfolio to a JSON file."""
    with open(PORTFOLIO_FILE, 'w') as file:
        json.dump(portfolio, file, indent=4)


def display_Indian_company_list(filename="indian_companies.txt"):
    """Display all companies and their symbols from the file."""
    print("List of Available Companies and Symbols:")
    print("")
    with open(filename, 'r') as file:
        for line in file:
            name, symbol = line.strip().split(',')
            print(f"{name} ({symbol})")

def display_usa_company_list(filename="usa_companies.txt"):
    """Display all companies and their symbols from the file."""
    print("List of Available Companies and Symbols:")
    print("")
    with open(filename, 'r') as file:
        for line in file:
            name, symbol = line.strip().split(',')
            print(f"{name} ({symbol})")

def add_stock(symbol, quantity):
    """Add a stock to the portfolio."""
    portfolio = load_portfolio()

    # Fetching stock price.
    price = fetch_stock_price(symbol)              

    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
    else:
        portfolio[symbol] = {
            'quantity': quantity
        }
    save_portfolio(portfolio)
    print(f"{symbol} added to your portfolio.")


def remove_stock(symbol):
    """Remove a stock from the portfolio."""
    portfolio = load_portfolio()
    if symbol in portfolio:
        del portfolio[symbol]
        save_portfolio(portfolio)
        print(f"{symbol} removed from your portfolio.")
    else:
        print(f"{symbol} is not in your portfolio.")


def fetch_stock_price(symbol):
    """Fetch the current stock price using yfinance."""
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d')
    return data['Close'][0] if not data.empty else None


def view_portfolio():
    """View the current portfolio with real-time stock prices."""
    portfolio = load_portfolio()
    if not portfolio:
        print("Your portfolio is empty.")
        return
    

    print("Your Portfolio:")
    for symbol, details in portfolio.items():
        current_price = fetch_stock_price(symbol)
        if current_price:
            total_value = current_price * details['quantity']
            print(f"{symbol}: {details['quantity']} shares @ {current_price:.2f} USD, Total Value: {total_value:.2f} USD")
        else:
            print(f"{symbol}: Price data unavailable.")


def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Stock Symbol by Companies")
        print("5. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            price = fetch_stock_price(symbol)
            print(f"Current price of {symbol}: ${price} per share")
            check = input("Do you want to add stock at this price- y/n: ").lower()
            if(check=="y"):
                quantity = int(input("Enter quantity: "))
                add_stock(symbol, quantity)            
            
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)

        elif choice == '3':
            view_portfolio()

        elif choice == '4':
            print("1. For Indian companies.")
            print("2. For US companies.")
            country = input("Enter the country name of the comapnies you want to see the symbol:")
            
            if(country == '1'):
                display_Indian_company_list()
            elif(country == '2'):
                display_usa_company_list()
            else:
                print("Please enter a valid input!!!")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    


