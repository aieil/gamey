
from priorityq import PQ

# class MazePoint(object):
#     """a point in the maze"""
#     def __init__(self, y, x):
#         self.y = y
#         self.x = x
#

class JLMaze(object):
    """A maze representation using a simple list of strings."""
    def __init__(self, maze):
        self.maze = maze
        self.width = len(maze[0])
        self.height = len(maze)
        self.start = None
        self.goal = None

        # find the starting and goal indices in the maze grid.
        y = 1
        while y < self.height - 1 and not self.start and not self.goal:
            x = 1
            while x < self.width - 1 and not self.start and not self.goal:
                if maze[y][x] == 'S':
                    self.start = (y, x)
                elif maze[y][x] = 'G':
                    self.goal = (y, x)
                x += 1
            y += 1

    def Astar(self, neighborMethod):
        frontier = PQ()
        frontier.push(self.start)
        came_from = {}
        cost_at_position = {}
        came_from[self.start] = None
        cost_at_position[self.start] = 0

        while not frontier.isEmpty():
            current = frontier.pop()

            if current = self.goal:
                break

            for

    def load_maze(cls, fname):
        with open(fname) as inf:
            maze = [line.rstrip("\r\n") for line in inf]
        return cls(maze)

    def neighborhood_partA(y, x):
        neighbors = []
        # graph may have up to 4 neighbours.
        # directly above
        if self.maze[y-1][x] in "_G":
            neighbors.append((y-1, x))

        if self.maze[y + 1][x] in "_G":
            neighbors.append((y + 1, x))

        if self.maze[y][x - 1] in "_G":
            neighbors.append((y, x - 1))

        if self.maze[y][x + 1] in "_G":
            neighbors.append((y, x + 1))
