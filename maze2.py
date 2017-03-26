
from priorityq import PQ
from pprint import pprint
from copy import deepcopy


class Maze(object):
    """A maze representation using a simple list of strings."""
    def __init__(self, maze):
        self.maze = maze
        self.width = len(maze[0])
        self.height = len(maze)
        self.start = None
        self.goal = None
        # find the starting and goal indices in the maze grid.
        y = 1
        while y < self.height and (not self.start or not self.goal):
            x = 1
            while x < self.width and (not self.start or not self.goal):
                if maze[y][x] == 'S':
                    self.start = (y, x)
                elif maze[y][x] == 'G':
                    self.goal = (y, x)
                x += 1
            y += 1


    def Astar(self, neighborMethod):
        frontier = PQ()
        frontier.push(self.start)
        came_from = {}
        cost_at = {}
        came_from[self.start] = None
        cost_at[self.start] = 0

        current = None
        while not frontier.isEmpty():
            current = frontier.pop()

            if current == self.goal:
                #print("Current equals goal Breaking out of loop.")
                break

            for neighbor in neighborMethod(current):
                new_cost = cost_at[current] + 1
                if neighbor not in cost_at or new_cost < cost_at[neighbor]:
                    cost_at[neighbor] = new_cost
                    priority = new_cost + manhattan(neighbor, self.goal)
                    frontier.push(neighbor, priority)
                    came_from[neighbor] = current
        # If at this point, the goal has not been reached, there is no solution.
        if current != self.goal:
            print("no solution!!!")
            return None
        # now reconstruct the path.
        return self.reconstruct_path(came_from)

    def greedy(self, neighborMethod):
        frontier = PQ()
        frontier.push(self.start)
        came_from = {}
        came_from[self.start] = None

        current = None
        while not frontier.isEmpty():
            current = frontier.pop()
            if current == self.goal:
                #print("Current equals goal Breaking out of loop.")
                break
            for neighbor in neighborMethod(current):
                if neighbor not in came_from:
                    priority = manhattan(neighbor, self.goal)
                    frontier.push(neighbor, priority)
                    came_from[neighbor] = current

        if current != self.goal:
            print("no solution!!!")
            return None

        return self.reconstruct_path(came_from)



    def reconstruct_path(self, came_from):
        """Works backwards from the goal to determine the path took by the algorithm from start."""
        current = self.goal
        path = []
        path.append(current)
        while current != self.start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


    def path_output(self, path):
        """
        Sets the nodes visited in the path passed as 'path' to the character P
        in a copy of the text representation of the maze and returns it.
        """
        mazeOut = deepcopy(self.maze)
        for y, x in path:
            if mazeOut[y][x] not in 'SG':
                #mazeOut[y][x] = 'P'
                # converting the line to replace characters, at indices,
                # since strings are immutable.
                strlist = list(mazeOut[y])
                strlist[x] = 'P'
                mazeOut[y] = ''.join(strlist)
        return mazeOut


    @classmethod
    def load_maze(cls, fname):
        with open(fname) as inf:
            maze = [line.rstrip("\r\n") for line in inf]
        return cls(maze)

    def neighborhood_partA(self, square):
        neighbors = []
        y, x = square
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

        return neighbors

    def neighborhood_partB(self, square):
        neighbors = []
        y, x = square
        # squares from part A:
        if self.maze[y-1][x] in "_G":
            neighbors.append((y-1, x))

        if self.maze[y + 1][x] in "_G":
            neighbors.append((y + 1, x))

        if self.maze[y][x - 1] in "_G":
            neighbors.append((y, x - 1))

        if self.maze[y][x + 1] in "_G":
            neighbors.append((y, x + 1))

        # additional squares, part B
        if self.maze[y-1][x - 1] in "_G":
            neighbors.append((y-1, x - 1))

        if self.maze[y-1][x + 1] in "_G":
            neighbors.append((y-1, x + 1))

        if self.maze[y + 1][x - 1] in "_G":
            neighbors.append((y + 1, x - 1))

        if self.maze[y + 1][x + 1] in "_G":
            neighbors.append((y + 1, x + 1))

        return neighbors


def manhattan(pointA, pointB): # a to b
    ay, ax = pointA
    by, bx = pointB
    return abs(by - ay) + abs(bx - ax)

def load_maze_file(filename):
    # load multiple mazes from a file in the format specified in the assignment.
    with open(filename) as inf:
        lines = [line.rstrip("\r\n") for line in inf]
    mazes = []
    maze = []
    for line in lines:
        if line == '':
            # if the line is an empty string, that means it's the end of
            # the current maze.
            if maze != []: # skip multiple blank lines
                mazes.append(maze)
                maze = []
        else:
            maze.append(line)
    if maze != []: # situation where the file has no blank lines at end.
        mazes.append(maze)
    return mazes



def main():
    #m = JLMaze.load_maze("pathfinding_a.txt")
    #print(m.Astar(m.neighborhood_partA))
    #print(m.greedy(m.neighborhood_partA))

    # part A
    mazes = load_maze_file("pathfinding_a.txt")
    with open("pathfinding_a_out.txt", 'w') as outfile:
        for maze in mazes:
            m = Maze(maze)
            outfile.write("A*\n")
            AstarRslt = m.Astar(m.neighborhood_partA)
            AstarOut = m.path_output(AstarRslt)
            # have to add \n's to these.
            outfile.writelines((line + "\n" for line in AstarOut))
            outfile.write("\n")
            outfile.write("Greedy\n")
            greedyRslt = m.greedy(m.neighborhood_partA)
            greedyOut = m.path_output(greedyRslt)
            outfile.writelines((line + "\n" for line in greedyOut))
            #outfile.writelines(greedyOut)
            outfile.write("\n")

    # part B
    mazes = load_maze_file("pathfinding_b.txt")
    with open("pathfinding_b_out.txt", 'w') as outfile:
        for maze in mazes:
            m = Maze(maze)
            outfile.write("A*\n")
            AstarRslt = m.Astar(m.neighborhood_partB)
            AstarOut = m.path_output(AstarRslt)
            # have to add \n's to these.
            outfile.writelines((line + "\n" for line in AstarOut))
            outfile.write("\n")
            outfile.write("Greedy\n")
            greedyRslt = m.greedy(m.neighborhood_partB)
            greedyOut = m.path_output(greedyRslt)
            outfile.writelines((line + "\n" for line in greedyOut))
            #outfile.writelines(greedyOut)
            outfile.write("\n")


if __name__ == '__main__':
    main()
