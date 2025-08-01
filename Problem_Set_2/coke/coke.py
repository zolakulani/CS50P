due = 50
while True:
    print("Amount Due:",due)

    c = int(input("Insert Coin: "))

    if c == 25 or c == 10 or c == 5:
        due -= c
        if due < 0:
            due = due*(-1)
            print("Change Owed:", due)
            break
        if due == 0:
            print("Change Owed:", due)
            break


