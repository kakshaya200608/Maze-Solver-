import heapq
from typing import Callable, List, Tuple, Optional
from .maze import Maze, Position
import math


def manhattan(a: Position, b: Position) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean(a: Position, b: Position) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _reconstruct_path(came_from: dict, current: Position) -> List[Position]:
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(maze: Maze, heuristic: Callable[[Position, Position], float] = manhattan) -> Optional[List[Position]]:
    """Run A* on the given Maze. Returns a list of positions from start to goal, or None if unreachable."""
    start = maze.start
    goal = maze.goal

    open_heap = []  # elements are (f_score, g_score, position)
    heapq.heappush(open_heap, (heuristic(start, goal), 0, start))

    came_from = {}
    g_score = {start: 0}
    closed = set()

    while open_heap:
        f, g, current = heapq.heappop(open_heap)
        if current == goal:
            return _reconstruct_path(came_from, current)
        if current in closed:
            continue
        closed.add(current)

        for neighbor in maze.neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor in g_score and tentative_g >= g_score[neighbor]:
                continue
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g
            fscore = tentative_g + heuristic(neighbor, goal)
            heapq.heappush(open_heap, (fscore, tentative_g, neighbor))

    return None
