s = input("camelCase: ")
new = ""
for i in s:
    if i.isupper():
        new += "".join(["","_"])
        new += i.lower()
    else:
        new += i
print("snake_case:", new)