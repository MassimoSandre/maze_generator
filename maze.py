import random
import types

const = types.SimpleNamespace()
const.UP = 1
const.LEFT = 2
const.DOWN = 3
const.RIGHT = 4


class Maze:
    def __init__(self, dim) -> None:
        self.dim = dim
        self.generate_new()

    def generate_new(self):
        visited = [[False for _ in range(self.dim[0])] for _ in range(self.dim[1])]
        self.doors = []

        def dfs(x,y):
            visited[x][y] = True
            to_check = []
            if x > 0:
                to_check.append(const.LEFT)
            if x < self.dim[0]-1:
                to_check.append(const.RIGHT)
            if y > 0:
                to_check.append(const.UP)
            if y < self.dim[1]-1:
                to_check.append(const.DOWN)
            
            random.shuffle(to_check)

            for i in to_check:
                match i:
                    case const.UP:
                        if not visited[x][y-1]:
                            self.doors.append((x,y-1,x,y))
                            dfs(x,y-1)

                    case const.LEFT:
                        if not visited[x-1][y]:
                            self.doors.append((x-1,y,x,y))
                            dfs(x-1,y)

                    case const.DOWN:
                        if not visited[x][y+1]:
                            self.doors.append((x,y,x,y+1))
                            dfs(x,y+1)
                        
                    case const.RIGHT:
                        if not visited[x+1][y]:
                            self.doors.append((x,y,x+1,y))
                            dfs(x+1,y)

        dfs(0,0)