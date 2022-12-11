f = open("input.txt", "r");
input = f.read().split('\n');
subtotal = 1;
cycles = 0;
pixels = list("." * 40 * 6);

def updatePixels(subtotal, cycles, pixels):
    pos = (cycles - 1) % 40
    if pos in {subtotal-1, subtotal, subtotal+1}:
        pixels[cycles - 1] = "#";
    return pixels;

for line in input:
    if line == "noop":
        cycles += 1
        pixels = updatePixels(subtotal, cycles, pixels)
    else:
        line = line.split();
        cycles += 1
        pixels = updatePixels(subtotal, cycles, pixels)
        cycles += 1
        pixels = updatePixels(subtotal, cycles, pixels)
        subtotal += int(line[1])

for i in range(0, 201, 40):
    print("".join(pixels[i: i + 40]))

