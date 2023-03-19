# Creating a List of numbers
List = [1, 2, 3, 4, 5]
print("\nList of numbers: ")
print(List)

# Insert 100 at position 3
List[2] = 100
print("After inserting 100 at position 3:")
print(List)

#  Delete the number 4
List.remove(4)
print("After deleting the number 4 :")
print(List)

# Append 200
List.append(200)
print("After appending 200 :")
print(List)

# Print the list using for loop
print("Printing the list using for loop :")
for x in List:
    print(x)

# Delete the list
print("Deleting the list")
del List

