# Task 1: Read a File and Handle Errors
This program reads the `sample.txt` file and handles error gracefully if it doesn't exist

How it works:
- The program starts with `try` block.
- Then it reads the file `sample.txt` and prints out its content.
- Finally, the `except` works, if there's a `FileNotFoundError` error then it prints out the message.

### Example:
```
Reading file content: 
Line1: This is the first line
Line2: This is the second line
```

# Task 2: Write and Append Data to a File
The program takes input from user and writes and appends to `output.txt` file.

How it works:
- First it takes the input from user.
- Then it writes the input from user to the file `output.txt` and prints it's written successfully.
- Then it again takes input from user and appends to the same file and prints success message.
- Finally, it reads the file and prints out the file's content.

### Example:
```
Enter text to write to file: Hello world
Data successfully written to output.txt

Enter additional text to append: Learning python programming
Data successfully appended.

Final content of output.txt: 
Hello world
Learning python programming
```

**Note: I tried with 2 different approach and one of them is commented out.**