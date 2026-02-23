from typing import List, Tuple, Set, Optional

Position = Tuple[int, int]


class Maze:
    """Simple grid maze representation.

    Grid conventions for `from_grid`:
    - 'S' start
    - 'G' goal
    - '#' wall
    - any other char is free space
    """

    def __init__(self, rows: int, cols: int, start: Position, goal: Position, walls: Set[Position] = None):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.goal = goal
        self.walls = walls or set()

    @classmethod
    def from_grid(cls, grid: List[str]):
        rows = len(grid)
        cols = max(len(r) for r in grid) if rows else 0
        start = None
        goal = None
        walls: Set[Position] = set()
        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch == 'S':
                    start = (i, j)
                elif ch == 'G':
                    goal = (i, j)
                elif ch == '#':
                    walls.add((i, j))
        if start is None or goal is None:
            raise ValueError("Grid must contain 'S' (start) and 'G' (goal)")
        return cls(rows, cols, start, goal, walls)

    def in_bounds(self, pos: Position) -> bool:
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def passable(self, pos: Position) -> bool:
        return pos not in self.walls

    def neighbors(self, pos: Position):
        r, c = pos
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            n = (r + dr, c + dc)
            if self.in_bounds(n) and self.passable(n):
                yield n
