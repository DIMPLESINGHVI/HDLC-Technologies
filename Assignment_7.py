'''Create the following dictionary and perform the following operations D={
1: 100, 2: 200, 3: 300}
i) Display the data at the key 2.
ii) Append the data
400 using the key 4.
iii) Delete the value at key 3. '''

# creating the dictionary
D = {1: 100, 2: 200, 3: 300}

# displaying data at key 2
print("Displaying data at key 2: ", D[2])

# appending the data
print("appending the data: ")
D[4] = 400
print(D)

# deleting the value at key 3
print("Deleting the value at key 3")
D.pop(3)
print(D)
