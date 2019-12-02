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

class FileSystem:

    class __Node:
        __slots__ = '_node', '_value', '_branch'

        def __init__(self, node, value, branch):
            self._node = node
            self._value = value
            self._branch = branch

    def __init__(self):
        self._root = self.__Node(['/'], -1, [])


    def create(self, path, value):
        temppath = path.split('/')
        temppath = temppath[1:]
        print(temppath)
        currNode = self._root
        print('currNode: node{} value:{} branch:{}'.format(currNode._node, currNode._value, currNode._branch))
        if len(temppath) == 1:
            newNode = self.__Node([temppath[0]], value, [])
            currNode._branch.append(newNode)
            print('currNode: node{} value:{} branch:{}'.format(currNode._node, currNode._value, currNode._branch))
            return True

        flag = 0
        for i in range(len(temppath) - 1):
            folder = temppath[i]
            flag = 0
            branchlist = currNode._branch
            for nodes in branchlist:
                currNode = nodes
                print('foldername:{} node.name:{}'.format(folder, currNode._node))
                if folder == currNode._node[0]:
                    flag = 1
                    break
            print('currNode: node{} value:{} branch:{}'.format(currNode._node, currNode._value, currNode._branch))

        if flag == 0:
            return False

        newNode = self.__Node([temppath[-1]], value, [])
        currNode._branch.append(newNode)
        print('currNode: node{} value:{} branch:{}'.format(currNode._node, currNode._value, currNode._branch))
        return True


    def get(self, path):
        temppath = path.split('/')
        temppath = temppath[1:]
        print(temppath)

        currNode = self._root
        print('Get currNode: node{} value:{} branch:{}'.format(currNode._node, currNode._value, currNode._branch))
        if len(temppath) == 1:
            branchlist = currNode._branch
            for nodes in branchlist:
                currNode = nodes
                if temppath[0] == currNode._node[0]:
                    return currNode._value
            return -1

        val = -1
        flag = 0
        for i in range(len(temppath)):
            flag = 0
            folder = temppath[i]
            branchlist = currNode._branch
            for nodes in branchlist:
                currNode = nodes
                if folder == currNode._node[0]:
                    flag = 1
                    break

        if flag == 0:
            return -1
        print('Get currNode: node{} value:{} branch:{}'.format(currNode._node, currNode._value, currNode._branch))
        return currNode._value


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

