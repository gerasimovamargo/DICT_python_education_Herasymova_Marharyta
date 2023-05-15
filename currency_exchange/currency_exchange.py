"""CurrencyExchange is a program that allows you to exchange currencies."""

# Libraries
import requests
import json
import re


class CurrencyExchange:
    def __init__(self):
        """Initialize CurrencyExchange class."""
        self.user_currency_code = None
        self.user_currency_amount = None
        self.user_currency_exchange = None
        self.data = None

    def request(self):
        """Request to the site and get the result.
        If the currency code is not correct, then an error will be displayed."""
        try:
            request = requests.get(f"https://www.floatrates.com/daily/{self.user_currency_code}.json")
            self.data = json.loads(request.text)
            if self.user_currency_exchange in self.data:
                rate = self.data[self.user_currency_exchange]["rate"]
                result = round(self.user_currency_amount * rate, 2)
                print(f"You received {result} {self.user_currency_exchange.upper()}.")
            else:
                print("Error: Currency code is not supported.")
        except json.JSONDecodeError:
            print("Error: Currency code is not correct.")

    def main(self):
        """Main function witch start the program and ask user to input currency code and amount."""
        while True:
            print("Welcome to CurrencyExchange!\nIf you want to exit, just input command: '!exit'.")
            self.user_currency_code = input("Enter the currency code you want to exchange from: ").lower()
            if self.user_currency_code == "!exit":
                exit("Bye!")
            if self.user_currency_code == "" or not re.match(r"^[a-zA-Z]+$", self.user_currency_code):
                print("Error: Currency code is not correct.")
                continue
            self.user_currency_exchange = input("Enter the currency code you want to exchange to: ").lower()
            if self.user_currency_exchange == "!exit":
                exit("Bye!")
            if self.user_currency_exchange == "" or not re.match(r"^[a-zA-Z]+$", self.user_currency_exchange):
                print("Error: Currency code is not correct.")
                continue
            self.user_currency_amount = float(input("Enter the amount of money you want to exchange: "))
            if self.user_currency_amount == "!exit":
                exit("Bye!")
            self.request()


# Main
if __name__ == "__main__":
    currency_exchange = CurrencyExchange()
    currency_exchange.main()
