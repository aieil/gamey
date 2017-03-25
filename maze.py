from collections import namedtuple

Dir = namedtuple("Dir", ["char", "dy", "dx"])

class Maze:
    START = "S"
    END   = "G"
    WALL  = "#"
    PATH  = "_"
    OPEN  = {PATH, END}  # map locations you can move to (not WALL or already explored)

    RIGHT = Dir("P",  0,  1)
    DOWN  = Dir("P",  1,  0)
    LEFT  = Dir("P",  0, -1)
    UP    = Dir("P", -1,  0)
    DIRS  = [RIGHT, DOWN, LEFT, UP]

    @classmethod
    def load_maze(cls, fname):
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            maze  = [list(line) for line in lines]
        return cls(maze)

    def __init__(self, maze):
        self.maze = maze

    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)

    def find_start(self):
        for y,line in enumerate(self.maze):
            try:
                x = line.index("S")
                return y, x
            except ValueError:
                pass


        # not found!
        raise ValueError("Start location not found")

    def solve(self, y, x):
        if self.maze[y][x] == Maze.END:
            # base case - endpoint has been found
            return True
        else:
            print ("this is where the a* and greedy algo go")

    
def main():
    maze = Maze.load_maze("pathfinding_a.txt")

    print("Maze loaded:")
    print(maze)

    try:
        sy, sx = maze.find_start()
        print("solving...")
        if maze.solve(sy, sx):
            print(maze)
        else:
            print("    no solution found")
    except ValueError:
        print("No start point found.")

if __name__=="__main__":
    main()
