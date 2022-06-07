

If you're working with a large file, then you should instead read and process it line-by-line:

with open(filename) as file:
    for line in file:
        print(line.rstrip())
In Python 3.8 and up you can use a while loop with the walrus operator like so:

with open(filename) as file:
    while (line := file.readline().rstrip()):
        print(line)
Depending on what you plan to do with your file and how it was encoded, you may also want to manually set the access mode and character encoding:

with open(filename, 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        print(line)

https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
