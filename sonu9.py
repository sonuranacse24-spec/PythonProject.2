n = int(input("Enter number of items: "))

items = []

for i in range(n):
    item = int(input(f"Enter item number {i+1}: "))
    items.append(item)

# (a) Print total number of items
print("\n(a) Total number of items:", len(items))

# (b) Print last item number
print("(b) Last item number:", items[-1])

# (c) Print sorted list
sorted_items = sorted(items)
print("(c) Sorted item list:", sorted_items)

# (d) Check item 515
if 515 in items:
    print("(d) Yes")
else:
    print("(d) No")

# (e) Add 121 and 321 then sort and print
items.append(121)
items.append(321)
items.sort()

print("(e) Updated sorted list:", items)
