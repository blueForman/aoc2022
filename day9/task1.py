f = open("input.txt", "r");
input = f.read().split('\n');

class Point:
	x = 0;
	y = 0;

	def __init__(self, x, y):
		self.x = x;
		self.y = y;


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
            H.y += 1;
        elif direction == 'D':
            H.y -= 1;
        elif direction == 'L':
            H.x -= 1;
        elif direction == 'R':
            H.x += 1;

        if  abs(H.y - T.y) > 1 or abs(H.x - T.x) > 1:
            if H.y == T.y and H.x - T.x > 1:
                T.x += 1;
            elif H.y == T.y and H.x - T.x < -1:
                T.x -= 1;
            elif H.x == T.x and H.y - T.y > 1:
                T.y += 1;
            elif H.x == T.x and H.y - T.y < -1:
                T.y -= 1;

            elif H.x > T.x and H.y > T.y:
                T.x += 1;
                T.y += 1;
            elif H.x > T.x and H.y < T.y:
                T.x += 1;
                T.y -= 1;
            elif H.x < T.x and H.y > T.y:
                T.x -= 1;
                T.y += 1;
            elif H.x < T.x and H.y < T.y:
                T.x -= 1;
                T.y -= 1;

            tailVisited.add((T.x, T.y));

print(len(tailVisited));
