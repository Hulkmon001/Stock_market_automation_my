import yfinance as yf
import talib

# Define the stock symbol and time period
symbol = input("Enter the stock symbol: ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Fetch historical stock data using Yahoo Finance API
stock_data = yf.download(symbol, start=start_date, end=end_date)

# Prompt the user to select an indicator
print("Available Indicators:")
print("1. Simple Moving Average (SMA)")
print("2. Exponential Moving Average (EMA)")
print("3. Relative Strength Index (RSI)")
indicator_choice = int(input("Enter the number of the indicator you want to use: "))

# Calculate indicator values based on user's choice
if indicator_choice == 1:
    period = int(input("Enter the period for Simple Moving Average (SMA): "))
    indicator_values = talib.SMA(stock_data["Close"], timeperiod=period)
elif indicator_choice == 2:
    period = int(input("Enter the period for Exponential Moving Average (EMA): "))
    indicator_values = talib.EMA(stock_data["Close"], timeperiod=period)
elif indicator_choice == 3:
    period = int(input("Enter the period for Relative Strength Index (RSI): "))
    indicator_values = talib.RSI(stock_data["Close"], timeperiod=period)
else:
    print("Invalid choice. Exiting program.")
    exit()

# Combine indicator values with stock data
stock_data["Indicator"] = indicator_values

# Implement your trading strategy based on the indicator values and execute trades
# ...

# Example: Print the stock data with the selected indicator
print(stock_data)
