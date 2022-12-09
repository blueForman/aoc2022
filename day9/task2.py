f = open("input.txt", "r");
input = f.read().split('\n');

class Point:
	x = 0;
	y = 0;

	def __init__(self, x, y):
		self.x = x;
		self.y = y;

numKnots = 10;
K = [];
for knot in range(numKnots):
    K.append(Point(0,0));

H = Point(0,0);
T = Point(0,0);
tailVisited = set();
tailVisited.add((0,0));

for line in input:
    move = line.split(' ');
    direction = move[0];
    steps = int(move[1]);

    for step in range(steps):
        if direction == 'U':
            K[0].y += 1;
        elif  direction == 'D':
            K[0].y -= 1;
        elif  direction == 'L':
            K[0].x -= 1;
        elif  direction == 'R':
            K[0].x += 1;

        for i in range(1, numKnots):
            
            if  abs(K[i-1].y - K[i].y) > 1 or abs(K[i-1].x - K[i].x) > 1:
                if K[i-1].y == K[i].y and K[i-1].x - K[i].x > 1: 
                    K[i].x += 1;
                elif K[i-1].y == K[i].y and K[i-1].x - K[i].x < -1:
                    K[i].x -= 1;
                elif K[i-1].x == K[i].x and K[i-1].y - K[i].y > 1: 
                    K[i].y += 1;
                elif K[i-1].x == K[i].x and K[i-1].y - K[i].y < -1: 
                    K[i].y -= 1;

                elif K[i-1].x > K[i].x and K[i-1].y > K[i].y: 
                    K[i].x += 1;
                    K[i].y += 1;
                elif K[i-1].x > K[i].x and K[i-1].y < K[i].y:
                    K[i].x += 1;
                    K[i].y -= 1;
                elif K[i-1].x < K[i].x and K[i-1].y > K[i].y:
                    K[i].x -= 1;
                    K[i].y += 1;
                elif K[i-1].x < K[i].x and K[i-1].y < K[i].y: 
                    K[i].x -= 1;
                    K[i].y -= 1;

        tailVisited.add((K[-1].x, K[-1].y));

print(len(tailVisited));
