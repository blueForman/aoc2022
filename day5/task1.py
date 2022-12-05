
import time
from collections import defaultdict

cargo = defaultdict(list)
parts = open("input.txt").read().split("\n\n")
config = parts[0].split('\n')

for l in config[:-1]:
    for i, c in enumerate(l):
        if c.isalpha():
            cargo[config[-1][i]].insert(0, c)

for l in parts[1].split("\n"):
    move = list(l.replace("move", "").replace(
        "to", "").replace("from", "").split())

    cargo[move[2]] += cargo[move[1]][-int(move[0]):][::-1]
    del cargo[move[1]][-int(move[0]):]

result = ""
for i in range(1, 10):
    result = result + cargo[str(i)][-1]
print(result)
