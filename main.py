from datetime import datetime

dt_string = "12AA-11-20"
new_string = []
for symbol in dt_string:
    if not symbol.isalpha():
        new_string.append(symbol)

new_string = ''.join(new_string).strip()

print(new_string)