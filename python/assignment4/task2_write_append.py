"""
input1 = input("Enter text to write to file: ")
file1 = open("output.txt", "w")
writing = file1.write(input1)
file1.close()
print("Data successfully written to output.txt")

print()

input2 = input("Enter additional text to append: ")
file2 = open("output.txt", "a")
appending = file2.write("\n" + input2)
file2.close()
print("Data successfully appended.")

print()

file3 = open("output.txt", "r")
reading = file3.read()
file3.close()
print("Final content of output.txt: ")
print(reading)
"""

# with open version
input1 = input("Enter text to write to file: ")
with open("output.txt", "w") as file1:
    file1.write(input1)
    print("Data successfully written to output.txt")
print()

input2 = input("Enter additional text to append: ")
with open("output.txt", "a") as file2:
    file2.write("\n" + input2)
    print("Data successfully appended.")
print()

with open("output.txt", "r") as file3:
    reading = file3.read()
    print("Final content of output.txt: ")
    print(reading)
