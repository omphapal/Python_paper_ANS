#list of numbers
numbers=[5,3,7,3,9,3,2,5]

# Take input from user
search_num=int(input("Enter number to search: "))

#check if element exists
if search_num in numbers:
    print(search_num,"is present in the list.")

else:
    print(search_num,"is not present in the list")

    # Count occurrences

    count=numbers.count(search_num)

    print("Occurrences of ",search_num,"=",count)
