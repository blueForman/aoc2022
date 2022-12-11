f = open("input.txt", "r");
input = f.read().split('\n');

additions = [];
for line in input:
    if line == 'noop':
        additions.append(0);
    else:
        lineElements = line.split(' ');
        command = lineElements[0];
        addition = int(lineElements[1]);
        additions.append(0);
        additions.append(addition);

print(additions[220]);

total = 0;
x = 1;
cycles = [20, 60, 100, 140, 180, 220];
for cycle in cycles:
    subtotal = 1;
    for i in range(0, cycle-1):
        subtotal += additions[i];
    #print(subtotal);
    #print(additions[i]);
    subtotal *= cycle;
    #print(cycle, subtotal);
    total += subtotal; 

print(total);