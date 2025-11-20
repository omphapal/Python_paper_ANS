n = int(input("How many elements? "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

search_num = int(input("Enter number to search: "))

if search_num in lst:
    print("Found!")
else:
    print("Not Found!")

print("Occurrences:", lst.count(search_num))
