import os

"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
from typing import Callable, Iterable, List


def validate_line(line: str) -> bool:
    if len(line.split()) != 5:
        file = open("report.txt", "a+")
        file.write(line.strip() + " validate_line\n")
        file.close()
        return False


def validate_date(line: str) -> bool:
    if len(line.split()) == 5:
        date = line.split()[4].strip()
        only_numeric_date = []
        for symbol in date:
            if not symbol.isalpha():
                only_numeric_date.append(symbol)
        only_numeric_date = ''.join(only_numeric_date).strip()

        if not (len(only_numeric_date) == 10 and only_numeric_date[4] == "-" and only_numeric_date[7] == "-"):
            file = open("report.txt", "a+")
            file.write(line.strip() + " validate_date\n")
            file.close()
            return False
    else:
        return False


def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    file = open(filepath, "r+")
    lines = list(file.readlines())

    for validator in validators:
        for line in lines:
            validator(line)
    file.close()
    return os.path.abspath("report.txt")
