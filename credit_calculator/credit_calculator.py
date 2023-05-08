"""Credit Calculator Project"""

# Libraries
import math
import argparse


class CreditCalculator:
    def __init__(self):
        """Initialize the class"""
        self.payment: float = 0
        self.principal: float = 0
        self.interest: float = 0
        self.overpayment: float = 0
        self.periods = 0

    def annuity_mon_pay(self):
        """Calculate annuity monthly payment"""
        i = self.interest / (12 * 100)
        a = math.ceil(self.principal * (i * pow(1 + i, self.periods)) / (pow(1 + i, self.periods) - 1))
        print(f'Your annuity payment = {a}!')
        self.overpayment = a * self.periods - self.principal
        print(f'Overpayment = {self.overpayment}')

    def diff_pay(self):
        """Calculate differentiated monthly payment"""
        i = self.interest / (12 * 100)
        for m in range(1, self.periods + 1):
            d = math.ceil(self.principal / self.periods + i *
                          (self.principal - (self.principal * (m - 1)) / self.periods))
            print(f'Month {m}: paid out {d}')
            self.overpayment += d
        print(f'Overpayment = {self.overpayment - self.principal}')

    def num_mon_pay(self):
        """Calculate the number of months to repay the credit"""
        i = self.interest / (12 * 100)
        n = math.ceil(math.log(self.payment / (self.payment - i * self.principal), 1 + i))
        years = n // 12
        months = n % 12
        self.overpayment = self.payment * n - self.principal
        if years == 0:
            print(f'You need {months} months to repay this credit!')
        elif months == 0:
            print(f'You need {years} years to repay this credit!')
        else:
            print(f'You need {years} years and {months} months to repay this credit!')
        print(f'Overpayment = {self.overpayment}')

    def loan_principal(self):
        """Calculate the loan principal"""
        i = self.interest / (12 * 100)
        p = math.floor(self.payment / ((i * pow(1 + i, self.periods)) / (pow(1 + i, self.periods) - 1)))
        print(f'Your loan principal = {p}!')
        self.overpayment = self.payment * self.periods - p
        print(f'Overpayment = {self.overpayment}')

    def parser(self):
        """Parse the arguments and call the corresponding method"""
        if args.type == 'annuity':
            if args.payment is not None and args.principal is not None and args.interest is not None:
                self.payment = args.payment
                self.principal = args.principal
                self.interest = args.interest
                self.num_mon_pay()
            elif args.payment is not None and args.periods is not None and args.interest is not None:
                self.payment = args.payment
                self.periods = args.periods
                self.interest = args.interest
                self.loan_principal()
            elif args.principal is not None and args.periods is not None and args.interest is not None:
                self.principal = args.principal
                self.periods = args.periods
                self.interest = args.interest
                self.annuity_mon_pay()
            else:
                print('Incorrect parameters')
        elif args.type == 'diff':
            if args.type is None or args.interest is None or args.principal is None \
                    or args.periods is None:
                print('Incorrect parameters')
            elif args.principal and args.periods and args.interest:
                self.principal = args.principal
                self.periods = args.periods
                self.interest = args.interest
                self.diff_pay()
            else:
                print('Incorrect parameters')
        else:
            print('Incorrect parameters')


# Main
if __name__ == '__main__':
    credit_calc = CreditCalculator()
    parser = argparse.ArgumentParser()
    # Add the arguments to the parser
    parser.add_argument('--type', type=str, help='type of payment')
    parser.add_argument('--payment', type=float, help='monthly payment')
    parser.add_argument('--principal', type=float, help='credit principal')
    parser.add_argument('--periods', type=int, help='the number of payment periods')
    parser.add_argument('--interest', type=float, help='the loan interest rate')
    args = parser.parse_args()
    credit_calc.parser()
