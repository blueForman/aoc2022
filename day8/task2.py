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
def countTop(x, y, value, trees):
    count=0;
    topTrees = range(y);
    for i in reversed(topTrees):
        count += 1;
        if value <= trees[i][x]:
            break;
    return count;

def countLeft(x, y, value, trees):
    count=0;
    leftTrees = range(x);
    for i in reversed(leftTrees):
        count += 1;
        if value <= trees[y][i]:
            break;
    return count;

def countBottom(x, y, value, trees, height):
    count = 0;
    for i in range((y+1), height):
        count += 1;
        if value <= trees[i][x]:
            break;
    return count;

def countRight(x, y, value, trees, width):
    count = 0;
    for i in range((x+1), width):
        count += 1;
        if value <= trees[y][i]:
            break;
    return count;

scenicScore = 0;

for y in range(1, (height-1)):
    for x in range(1, (width-1)):
        top = countTop(x, y, trees[y][x], trees);
        left = countLeft(x, y, trees[y][x], trees);
        right = countRight(x, y, trees[y][x], trees, width); 
        bottom = countBottom(x, y, trees[y][x], trees, height);
        score = top * left * right * bottom;
        if score > scenicScore:
            scenicScore = score;

print(scenicScore);
                
        