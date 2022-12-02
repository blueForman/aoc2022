f = open("input.txt", "r")
input = f.read()


formatedInput = input.split('\n');

elfs = [];

temp = 0;
for proteins in formatedInput:
    if proteins == "":
        elfs.append(temp)
        temp = 0
    else:
         temp = temp + int(proteins)
    
print(max(elfs))