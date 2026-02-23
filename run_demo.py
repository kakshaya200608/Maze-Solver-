from maze_solver.maze import Maze
from maze_solver.astar import astar, manhattan, euclidean
from maze_solver.visualize import print_maze, plot_maze


def demo(grid):
    maze = Maze.from_grid(grid)
    print("Original grid:")
    print_maze(maze)
    for name, heur in (("Manhattan", manhattan), ("Euclidean", euclidean)):
        print(f"\n--- {name} heuristic ---")
        path = astar(maze, heuristic=heur)
        if path:
            print(f"Path found; length={len(path)-1}")
            print_maze(maze, path)
            try:
                plot_maze(maze, path)
            except Exception:
                pass
        else:
            print("No path found.")


if __name__ == '__main__':
    grid = [
        "S....",
        ".##..",
        ".#G#.",
        ".#...",
        ".....",
    ]
    demo(grid)
