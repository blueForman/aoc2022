dictionary = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }


f = open("input.txt", "r")
input = f.read()


formatedInput = input.split('\n');

score = 0;

for row in formatedInput:
   score = score + dictionary[row];

 

print(score);