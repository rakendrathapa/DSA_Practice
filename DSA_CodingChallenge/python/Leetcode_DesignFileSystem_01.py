"""

You are asked to design a file system which provides two functions:

create(path, value): Creates a new path and associates a value to it if possible and returns True. Returns False if the path already exists or its parent path doesn't exist.
get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.
The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Implement the two functions.

Please refer to the examples for clarifications.



Example 1:

Input:
["FileSystem","create","get"]
[[],["/a",1],["/a"]]
Output:
[null,true,1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.create("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input:
["FileSystem","create","create","get","create","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output:
[null,true,true,2,false,-1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.create("/leet", 1); // return true
fileSystem.create("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.create("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.

"""

from collections import defaultdict
from collections import defaultdict

class FileSystem:

    def __init__(self):
        self._root = defaultdict(int)


    def create(self, path, value):
        temppath = path.split('/')
        temppath = temppath[1:-1]

        checkpaths = ""
        for folders in temppath:
            checkpaths += "/" + folders
            if checkpaths not in self._root:
                return False

        self._root[path] = value
        return True

    def get(self, path):
        # print(path)
        if path in self._root:
            return self._root[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)

def main():
    # Your FileSystem object will be instantiated and called as such:
    testcases = list()
    cmdlist = ["FileSystem","create","create","get","create","get"]
    vallist = [[],["/leet",1],["/leet/code", 2],["/leet/code"],["/c/d",1],["/c"]]
    testcases.append((cmdlist, vallist))

    cmdlist = ["FileSystem", "create", "create", "create", "get", "create", "get"]
    vallist = [[], ["/leet", 1], ["/leet/code", 2], ["/c", 4], ["/leet/code"], ["/c/d", 1], ["/c"]]
    testcases.append((cmdlist, vallist))

    cmdlist = ["FileSystem", "create", "get"]
    vallist = [[], ["/a", 1], ["/a"]]
    testcases.append((cmdlist, vallist))

    for case in testcases:
        cmdlist , vallist = case
        zippedcase = zip(cmdlist, vallist)
        obj = None
        param_1 = None
        param_2 = None
        output = list()

        for cmd, value in zippedcase:
            if cmd == "FileSystem":
                obj = FileSystem()
                output.append(value)
            elif  cmd == "create":
                path, val = value
                param_1 = obj.create(path,val)
                output.append(param_1)
            elif cmd == "get":
                path = value[0]
                param_2 = obj.get(path)
                output.append(param_2)
            else:
                output = []

        print(output)




if __name__ == '__main__':
    main()

