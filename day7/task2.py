f = open("input.txt", "r")
input = f.read().split('\n')

class Directory:
    def __init__(self, name, parent=None):
        self.name = name;
        self.parent = parent;
        self.files = [];
        self.subDirs = [];

    def size(self):
        filesSize = sum(self.files);

        dirsSize = 0;
        for subDir in self.subDirs:
            dirsSize += subDir.size();
        
        return filesSize + dirsSize;
    
    def findDir(self, name):
        for subDir in self.subDirs:
            if subDir.name == name:
                return subDir;
        return None;

directories = [];


currentDir = None;

for cmd in input:
    if cmd.startswith("dir") or cmd.startswith("$ ls"):
        continue
    elif cmd.startswith("$ cd"):
        parts = cmd.split(' ');

        if currentDir == None:
            currentDir = Directory('/');
            directories.append(currentDir);

        if parts[2] == "..":
            currentDir = currentDir.parent;
        else:
            lookedDir = currentDir.findDir(parts[2]);

            if lookedDir == None:
                newDir = Directory(parts[2], currentDir);
                currentDir.subDirs.append(newDir);
                directories.append(newDir);

                currentDir = newDir;
            else:
                currentDir = lookedDir;
    else:
        currentDir.files.append(int(cmd.split(' ')[0]));

maxSpace = 70000000;
allowedSpace = 30000000;

rootSpace = directories[0].size();
freeSpace = maxSpace - rootSpace;
requiredSpace = allowedSpace - freeSpace;

directoriesThatWouldFreeEnough = [];

for dir in directories:
    if (dir.size() > requiredSpace):
       directoriesThatWouldFreeEnough.append(dir.size()); 

directoriesThatWouldFreeEnough = sorted(directoriesThatWouldFreeEnough);

print(directoriesThatWouldFreeEnough[0]);
