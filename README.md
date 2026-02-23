# Maze Solver (A* Search)

Simple Python package implementing A* search on a grid maze.

Usage:

- Run the demo:

```bash
python -m examples.run_demo
```

Grid format for `Maze.from_grid` uses these characters:
- `S` start
- `G` goal
- `#` wall
- any other char: free space

The package provides `astar()` and two heuristics: `manhattan` and `euclidean`.
