


# Accept the date input in Month Date Year format and output it as
# Assume that every month has no more than 31 days.
# YYYY-MM-DD

# Assume that it must be Month, Day year regardless of numerals/alpha

# September 8, 1662
# 9/8/1662 only accept these two formats, everything else reprompt

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date_input = input("Date: ").strip()
    if ',' in date_input:
        date_list = date_input.split(" ")
        date_list[1] = date_list[1].replace(',', '')
        if date_list[0] in months and int(date_list[1]) >= 1 and int(date_list[1]) <= 31:
            for x in range(len(months)):
                if months[x] == date_list[0]:
                    new_month = x + 1
                    new_month = int(new_month)
                    new_day = date_list[1]
                    if new_month >= 1 and new_month <= 9:
                        new_month = f'0{new_month}'
                    if int(new_day) >= 1 and int(new_day) <= 9:
                        new_day = f'0{new_day}'

                    print(f'{date_list[2]}-{new_month}-{new_day}')
            break
        else:
            continue

    elif '/' in date_input:
        date_list = date_input.split("/")
        if date_list[0].isalpha():
            continue
        month = int(date_list[0])
        day = int(date_list[1])
        if month >= 1 and month <= 12:
            if month <= 9:
                month = f'0{month}'
            if day >= 1 and day <= 9:
                day = f'0{day}'
            elif day > 31:
                continue

            date = f'{date_list[2]}-{month}-{day}'
            print(date)
            break
        else:
            continue

