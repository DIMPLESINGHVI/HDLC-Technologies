st = str(input("Enter the string: "))
print("The input string is ", st)
rev = st[::-1]
if st == rev:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
