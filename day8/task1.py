f = open("input.txt", "r")
input = f.read().split('\n')

trees = [];

for row in input:
    treeRow = [];
    for tree in row:
        treeRow.append(int(tree));
    trees.append(treeRow);
    width = len(treeRow);

height = len(trees);
visibleCount = (2*height) + 2*(width-2);
def checkTop(x, y, value, trees):
    for i in range(y):
        if value <= trees[i][x]:
            return False;
    return True;

def checkLeft(x, y, value, trees):
    for i in range(x):
        if value <= trees[y][i]:
            return False;
    return True;

def checkBottom(x, y, value, trees, height):
    for i in range((y+1), height):
        if value <= trees[i][x]:
            return False;
    return True;

def checkRight(x, y, value, trees, width):
    for i in range((x+1), width):
        if value <= trees[y][i]:
            return False;
    return True;

for y in range(1, (height-1)):
    for x in range(1, (width-1)):
        if (checkTop(x, y, trees[y][x], trees) or
        checkLeft(x, y, trees[y][x], trees) or
        checkRight(x, y, trees[y][x], trees, width) or 
        checkBottom(x, y, trees[y][x], trees, height)):
            visibleCount += 1;

print(visibleCount);
                
        