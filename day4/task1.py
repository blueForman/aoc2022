
f = open("input.txt", "r")
input = f.read()

total = 0;

formatedInput = input.split('\n');

totalOverlapCount = 0;

for row in formatedInput:
    elfs = row.split(',');
    elf1 = elfs[0].split('-');
    elf2 = elfs[1].split('-');
    elf1Elements = [];
    elf2Elements = [];

    for i in range(int(elf1[0]), (int(elf1[1])+1)):
        elf1Elements.append(i);
    for i in range(int(elf2[0]), (int(elf2[1])+1)):
        elf2Elements.append(i);
    if len(elf1Elements) < len(elf2Elements) : 
        smaller = elf1Elements;
        longer = elf2Elements;
    else : 
        smaller = elf2Elements;
        longer = elf1Elements;

    intersection = list(set(smaller) & set(longer));

    if len(intersection) == len(smaller):
        totalOverlapCount = totalOverlapCount + 1;

print(totalOverlapCount);