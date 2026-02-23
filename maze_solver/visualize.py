from typing import List, Tuple, Optional
from .maze import Maze
try:
    import matplotlib.pyplot as plt
    import numpy as np
    HAS_MPL = True
except Exception:
    HAS_MPL = False


def print_maze(maze: Maze, path: Optional[List[Tuple[int, int]]] = None) -> None:
    grid = [["."] * maze.cols for _ in range(maze.rows)]
    for (r, c) in maze.walls:
        grid[r][c] = '#'
    sr, sc = maze.start
    gr, gc = maze.goal
    grid[sr][sc] = 'S'
    grid[gr][gc] = 'G'
    if path:
        for (r, c) in path:
            if (r, c) != maze.start and (r, c) != maze.goal:
                grid[r][c] = '*'
    for row in grid:
        print(''.join(row))


def plot_maze(maze: Maze, path: Optional[List[Tuple[int, int]]] = None) -> None:
    if not HAS_MPL:
        raise RuntimeError("matplotlib and numpy required for plotting")
    data = np.ones((maze.rows, maze.cols, 3), dtype=float)
    for (r, c) in maze.walls:
        data[r, c] = [0.0, 0.0, 0.0]
    sr, sc = maze.start
    gr, gc = maze.goal
    data[sr, sc] = [0.0, 1.0, 0.0]
    data[gr, gc] = [1.0, 0.0, 0.0]
    if path:
        for (r, c) in path:
            if (r, c) != maze.start and (r, c) != maze.goal:
                data[r, c] = [0.0, 0.0, 1.0]
    plt.imshow(data, interpolation='nearest')
    plt.gca().invert_yaxis()
    plt.axis('off')
    plt.show()
