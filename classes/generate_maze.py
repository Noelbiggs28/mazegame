import random
class Maze_Generator():
    def __init__(self):
        pass

    @staticmethod
    def generate_maze():
        maze_width = 20
        maze_height = 20
        maze = [[False for _ in range(maze_width)] for _ in range(maze_height)]
        visited = [[False for _ in range(maze_width)] for _ in range(maze_height)] #makes a new array. fillas all with false
        frontier = [(1, 1)]  # Start from the top-left corner
        exit_x = random.choice([0, maze_width - 1])
        exit_y = random.choice([0, maze_height - 1])

        while frontier:
            # Select a random corner as the exit
            x, y = random.choice(frontier)
            visited[y][x] = True

            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)] #checks two squares away so theres no squares of paths
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < maze_width and 0 <= ny < maze_height and not visited[ny][nx]: # Makes sure its in the maps perimeter and not done already
                    visited[ny][nx] = True #mark it visited
                    visited[y + dy // 2][x + dx // 2] = True #also makes adjacent square a path
                    frontier.append((nx, ny))

            frontier.remove((x, y))

        # Set the exit to an empty cell. 
        visited[exit_y][exit_x] = True

        # makes one squares next to exit true
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = exit_x + dx, exit_y + dy
            if 0 <= nx < maze_width and 0 <= ny < maze_height:
                visited[ny][nx] = 9
                

        # Copy the visited cells to the maze representation
        for y in range(maze_height):
            for x in range(maze_width):
                # changes maze of all walls to paths in visited
                if x == exit_x and y == exit_y:
                    maze[y][x] = 7
                elif visited[y][x] == 9:
                    maze[y][x] = 9
                elif visited[y][x] == False:
                    maze[y][x] = 8
                elif visited[y][x] == True:
                    maze[y][x] = 6
                # maze[y][x] = visited[y][x]
  
        return [maze,[exit_x, exit_y]]

