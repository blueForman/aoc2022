letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

priocounter = 1;

prioLetters = {};

for letter in letters:
    prioLetters[letter] = priocounter;
    priocounter = priocounter + 1;

f = open("input.txt", "r")
input = f.read()

total = 0;

formatedInput = input.split('\n');

for row in formatedInput:
    totalLength = len(row);
    half = totalLength//2;
    compartment1 = row[0:half];
    compartment2 = row[half:totalLength];
    commonCharacters = ''.join(set(compartment1).intersection(compartment2))   

    for commonLetter in commonCharacters:
        total = total + prioLetters[commonLetter];


print(total);