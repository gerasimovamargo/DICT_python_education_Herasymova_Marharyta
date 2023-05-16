"""Regular expression program"""

# Library
import re


class RegularExpression:
    def __init__(self):
        """Initialize variables"""
        self.first_string = ""
        self.second_string = ""

    def main_process(self):
        """Main process of program"""
        while True:
            user_input = input("Enter the string: ")
            if "|" not in user_input:
                print("You must input string with '|'")
                continue

            self.first_string, self.second_string = user_input.split(sep="|")
            if not self.first_string:
                print(False)
                continue

            if self.first_string == "^" and self.second_string == "$":
                print(bool(re.match(self.first_string, self.second_string)))
            else:
                print(bool(re.search(self.first_string, self.second_string)))


# Main
if __name__ == "__main__":
    regular_expression = RegularExpression()
    regular_expression.main_process()
