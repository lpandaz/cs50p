# xx:xx or x:xx

# 7-8 breakfast, 12:00 to 13:00 lunch, 18:00-19:00 dinner


def main():
    

    user_input = input("What time is it? ")
    real_time = convert(user_input)


    if real_time >= 7 and real_time <= 8:
        print("breakfast time")
    elif real_time >= 12 and real_time <= 13:
        print("lunch time")
    elif real_time >= 18 and real_time <= 19:
        print("dinner time")
    

def convert(time):
    hour, min = time.split(":")
    hour = float(hour)
    min = float(min)
    new_time = hour + (min / 60)
    return new_time

if __name__ == "__main__":
    main()