from datetime import datetime

print("Current date is ", datetime.now().date())
print("Current time is ", datetime.now().time())
print("Current day is ", datetime.now().day)
print("Current month is ", datetime.now().month)
print("Current Year is ", datetime.now().year)
print("Current weekday is ", datetime.now().date().weekday()) #Monday is 0
print("Current date + time is ", datetime.now().strftime("%B"))

print("++++++++++++++++++")
print(datetime.now().strftime("%a"), "+++++ Locales abbreviated weekday name.")
print(datetime.now().strftime("%A"), "+++++ Locales full weekday name.	")
print(datetime.now().strftime("%b"), "+++++ Locales abbreviated month name.	")
print(datetime.now().strftime("%B"), "+++++ Locales full month name.	")
print(datetime.now().strftime("%c"), "+++++ Locales appropriate date and time representation.	")
print(datetime.now().strftime("%d"), "+++++ Day of the month as a decimal number [01,31].	")
print(datetime.now().strftime("%H"), "+++++ Hour (24-hour clock) as a decimal number [00,23].")	
print(datetime.now().strftime("%I"), "+++++ Hour (12-hour clock) as a decimal number [01,12].	")
print(datetime.now().strftime("%j"), "+++++ Day of the year as a decimal number [001,366].	")
print(datetime.now().strftime("%m"), "+++++ Month as a decimal number [01,12].	")
print(datetime.now().strftime("%M"), "+++++ Minute as a decimal number [00,59].	")
print(datetime.now().strftime("%p"), "+++++ Locales equivalent of either AM or PM.	(1)")
print(datetime.now().strftime("%S"), "+++++ Second as a decimal number [00,61].	(2)")
print(datetime.now().strftime("%U"), "+++++ Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.	(3)")
print(datetime.now().strftime("%w"), "+++++ Weekday as a decimal number [0(Sunday),6].	")
print(datetime.now().strftime("%W"), "+++++ Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.	(3)")
print(datetime.now().strftime("%x"), "+++++ Locales appropriate date representation.	")
print(datetime.now().strftime("%X"), "+++++ Locales appropriate time representation.	")
print(datetime.now().strftime("%y"), "+++++ Year without century as a decimal number [00,99].	")
print(datetime.now().strftime("%Y"), "+++++ Year with century as a decimal number.	")
print(datetime.now().strftime("%Z"), "+++++ Time zone name (no characters if no time zone exists).	")
print(datetime.now().strftime("%%"), "+++++ A literal '%' character.")
print("++++++++++++++++++")