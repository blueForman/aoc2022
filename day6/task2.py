f = open("input.txt", "r")
input = f.read()

for i in range(14, len(input)):
    teststring = input[(i-14):i];
    uniqueCharacters = set(teststring);
    if 14 == len(uniqueCharacters):
        print(i);
        exit();