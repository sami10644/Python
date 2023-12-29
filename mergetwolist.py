a = [1, 2, 2, 3, 5, 40, 789, 7777]
b = [1, 2, 5, 7, 890]
c = []

i = 0  # Pointer for list a
j = 0  # Pointer for list b

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    elif a[i] > b[j]:
        c.append(b[j])
        j += 1
    else:
        # If elements are equal, add both to the result.
        c.append(a[i])
        i += 1
        c.append(b[j])
        j += 1

# If there are remaining elements in a or b, append them to the result.
while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

print(c)

