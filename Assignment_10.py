print("Enter the Name of Source File: ")
sFile = input()
print("Enter the Name of Target File: ")
tFile = input()


a = str(input("Enter the name of the source file with .txt extension:"))
print("Displaying the contents of source file")
f = open(a, 'r')
line = f.readline()
while line != "":
    print(line)
    line = f.readline()
f.close()
print("\n")

b = str(input("Enter the name of the target file with .txt extension:"))
print("Displaying the contents of target file")
fl = open(b, 'r')
line = fl.readline()
while line != "":
    print(line)
    line = fl.readline()
fl.close()

# copying the file content
fileHandle = open(sFile, "r")
texts = fileHandle.readlines()
fileHandle.close()

fileHandle = open(tFile, "w")
for s in texts:
    fileHandle.write(s)
fileHandle.close()

print("\nFile Copied Successfully!")
print("\n")

b = str(input("Enter the name of the target file with .txt extension:"))
print("Displaying content in the target file")
fl = open(b, 'r')
line = fl.readline()
while line != "":
    print(line)
    line = fl.readline()
fl.close()