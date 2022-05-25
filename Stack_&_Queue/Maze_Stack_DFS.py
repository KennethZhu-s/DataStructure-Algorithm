maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y: (x-1,y),
    lambda x,y: (x+1,y),
    lambda x,y: (x,y-1),
    lambda x,y: (x,y+1),
]

def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while(len(stack)>0):
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            # get to the goal
            for p in stack:
                print(p)
            return True

        # 4 directions   up: x-1, y   down: x+1, y    left: x, y-1    right: x, y+1
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # if next node is available :
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2   # 2 means nodes traveled
                break
        else:  # no available node found
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("No Way Out")
        return False


maze_path(1,1,8,8)
