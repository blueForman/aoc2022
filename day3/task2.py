letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

priocounter = 1;

prioLetters = {};

for letter in letters:
    prioLetters[letter] = priocounter;
    priocounter = priocounter + 1;

f = open("input.txt", "r")
input = f.read()


formatedInput = input.split('\n');

total = len(formatedInput);

start = 0;

totalSum = 0;

groupedRucksacks = [];

for i in range(0, total//3):
    row1 = formatedInput[i*3];
    row2 = formatedInput[i*3+1];
    row3 = formatedInput[i*3+2];
    group = [
        row1, row2, row3
    ];
    groupedRucksacks.append(group);

for rucksackGroup in groupedRucksacks:
    rucksack1 = rucksackGroup[0];
    rucksack2 = rucksackGroup[1];
    rucksack3 = rucksackGroup[2];
    intersectedSet = set(rucksack1) & set(rucksack2) & set(rucksack3);
    for character in intersectedSet:
        totalSum = totalSum + prioLetters[character];


print(totalSum);