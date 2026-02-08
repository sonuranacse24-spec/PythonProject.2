n = int(input("Enter number of items: "))
items = []

for i in range(n):
    num = int(input(f"Enter item number {i+1}: "))
    items.append(num)

# (a) Total number of items
print("\n(a) Total number of items:", len(items))

# (b) Last item in the list
print("(b) Last item in the list:", items[-1])

# (c) Items in sorted order
print("(c) Sorted list:", sorted(items))

# (d) Check if item 515 exists
if 515 in items:
    print("(d) Yes")
else:
    print("(d) No")

items.append(121)
items.append(321)
items.sort()

print("(e) Updated sorted list:", items)
