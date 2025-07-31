def main():
    time  = input("What time is it (##:##): ")
    time = convert(time)
    if isinstance(time, float):
        if 7<=time<=8:
            print("breakfast time")
        elif 12<=time<=13:
            print("lunch time")
        elif 18<=time<=19:
            print("dinner time")
        else:
            return
    else:
        print("Please Enter a valid time")

def convert(time):
    time_hours, time_min = time.split(":")
    time_hours = float(time_hours)
    time_min = float(time_min)/60
    if 0 <= time_hours <= 24 and 0 <= time_min <= .9833:
        time = time_hours + time_min
        return time
    else:
        return

if __name__ == "__main__":
    main()