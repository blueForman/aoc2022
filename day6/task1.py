f = open("input.txt", "r")
input = f.read()

for i in range(4, len(input)):
    teststring = input[(i-4):i];
    uniqueCharacters = set(teststring);
    if 4 == len(uniqueCharacters):
        print(i);
        exit();