# N-Queens Search Algorithms

This repository contains implementations of multiple search algorithms to solve the N-Queens problem, where the goal is to place N queens on an NxN chessboard such that no two queens threaten each other. Each directory in the repository holds a Python script that demonstrates a particular search technique.

## Introduction

The N-Queens problem is a classic problem in computer science and artificial intelligence. The challenge is to place N queens on an N x N chessboard such that no two queens can attack each other according to the rules of chess. This repository explores different search algorithms for solving this problem, including Breadth-First Search (BFS), Uniform Cost Search (UCS), Iterative Deepening Search (IDS), Greedy Search, and A* Search.

## Algorithms Implemented

1. **Breadth-First Search (BFS)**: Explores the broadest level of node first before moving onto nodes at the next depth level.
2. **Uniform Cost Search (UCS)**: Expands the least cost node and is used here to consistently evaluate expanding nodes based on the depth of the search tree.
3. **Iterative Deepening Search (IDS)**: Combines the depth-first search's space-efficiency and breadth-first search's completeness.
4. **Greedy Search**: Chooses the next node based on a heuristic that tries to minimize the number of conflicts.
5. **A* Search**: Utilizes costs and a heuristic function to determine the path likely leading to a goal fastest.

## Repository Structure

Each search technique is contained in its own Python script for clarity and modularity:

- `NQUEENS_BFS.py`: Implementation of the BFS algorithm.
- `NQUEENS_UCS.py`: Implementation of the UCS algorithm.
- `NQUEENS_IDS.py`: Implementation of the IDS algorithm.
- `NQUEENS_GREEDY.py`: Implementation of the Greedy algorithm.
- `NQUEENS_Astar.py`: Implementation of the A* algorithm.

## Requirements

- Python 3.x
- No external libraries are required for the basic functionality.

## Usage

To run any of the search solutions, navigate to the directory containing the desired script and run it using Python. For example:

```bash
python NQUEENS_BFS.py
```

You will be prompted to enter the size of the chessboard, after which the script will calculate and display all the possible solutions using the selected search algorithm.

## How Each Algorithm Works

Each algorithm script prompts the user to input the size of the chessboard. It then uses a specific search strategy to solve the N-Queens problem and outputs each solution along with its respective chessboard visualization.

- **BFS, UCS, and IDS**: These scripts work by generating successor states for each node by placing a queen in a row that does not result in a conflict. They differ in how they prioritize nodes.
- **Greedy and A* Search**: These scripts use a heuristic function to estimate the best node to expand next. The Greedy algorithm looks only at the heuristic, whereas A* considers both the cost and the heuristic.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
