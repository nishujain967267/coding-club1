abc=input("enter the list")
counts = {}
for item in abc:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

for item in abc:
    if counts[item] == 1:
        print(item)