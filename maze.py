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
        visited = [[False for _ in range(self.dim[1])] for _ in range(self.dim[0])]
        self.doors = []
        to_check = [const.UP, const.LEFT, const.DOWN, const.RIGHT]

        stack = [(-1,-1, 0,0)]

        while len(stack) > 0:
            px,py, x,y = stack.pop()

            if not visited[x][y]:
                if px != -1 and py != -1:
                    self.doors.append((min(px,x), min(py,y), max(px,x), max(py, y)))
                visited[x][y] = True
                
                random.shuffle(to_check)
                

                for i in to_check:
                    match i:
                        case const.UP:
                            if y > 0 and not visited[x][y-1]:
                                stack.append((x,y,x,y-1))

                        case const.LEFT:
                            if x > 0 and not visited[x-1][y]:
                                stack.append((x,y,x-1,y))

                        case const.DOWN:
                            if y < self.dim[1]-1 and not visited[x][y+1]:
                                stack.append((x,y,x,y+1))
                            
                        case const.RIGHT:
                            if x < self.dim[0]-1 and not visited[x+1][y]:
                                stack.append((x,y,x+1,y))