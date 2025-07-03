try:
    sample_file = open("sample.txt", "r")
    reading = sample_file.read()
    print("Reading file content: ")
    print(reading)
    sample_file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
