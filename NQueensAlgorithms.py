# Function to solve the N-Queens problem using Breadth-First Search (BFS) algorithm
def solve_bfs(size):
    """
    Solves the N-Queens problem using Breadth-First Search (BFS) algorithm.

    Parameters:
        size (int): The size of the chessboard (number of queens).

    Returns:
        List of Lists: List of solutions, where each solution is a list of queen positions.
    """
    if size < 1:
        return []

    solutions = []  # Initialize an empty list to store solutions
    queue = [[]]  # Initialize a queue with an empty board configuration

    while queue:
        solution = queue.pop(0)  # Take the first configuration from the queue

        if conflict(solution):  # Check for conflicts in the configuration
            continue

        row = len(solution)

        if row == size:  # If all queens are placed, add the solution to the list
            solutions.append(list(solution))
            continue

        # Generate all possible next configurations and add them to the queue
        for col in range(size):
            queen = [row, col]
            queens = list(solution)
            queens.append(queen)
            queue.append(queens)

    return solutions


# Function to solve the N-Queens problem using Uniform Cost Search (UCS) algorithm
def solve_ucs(size):
    """
    Solves the N-Queens problem using Uniform Cost Search (UCS) algorithm.

    Parameters:
        size (int): The size of the chessboard (number of queens).

    Returns:
        List of Lists: List of solutions, where each solution is a list of queen positions.
    """
    if size < 1:
        return []

    solutions = []  # Initialize an empty list to store solutions
    queue = [{"queens": [], "cost": 0}]  # Initialize a queue with an empty board configuration and cost 0

    while queue:
        item = queue.pop(0)
        queens, cost = item["queens"], item["cost"]

        if conflict(queens):  # Check for conflicts in the configuration
            continue

        row = len(queens)

        if row == size:  # If all queens are placed, add the solution to the list
            solutions.append(list(queens))
            continue

        # Generate all possible next configurations and add them to the queue with updated cost
        for col in range(size):
            queen = [row, col]
            newQueens = list(queens) + [queen]
            newCost = cost + 1
            queue.append({"queens": newQueens, "cost": newCost})

        queue = sorted(queue, key=lambda x: x["cost"])  # Sort the queue based on cost

    return solutions


# Function to check if there is a conflict between queens on the board
def conflict(queens):
    """
    Checks if there is a conflict between queens on the board.

    Parameters:
        queens (List): List of queen positions.

    Returns:
        bool: True if there is a conflict, False otherwise.
    """
    for i in range(1, len(queens)):
        for j in range(0, i):
            a, b = queens[i]
            c, d = queens[j]
            if a == c or b == d or abs(a - c) == abs(b - d):
                return True
    return False


# Function to print the chessboard with queens placed
def print_board(queens, size):
    """
    Prints the chessboard with queens placed.

    Parameters:
        queens (List): List of queen positions.
        size (int): The size of the chessboard (number of queens).

    Returns:
        None
    """
    for i in range(size):
        print(" ---" * size)
        for j in range(size):
            p = "Q" if [i, j] in queens else " "
            print(f"| {p} ", end="")
        print("|")
    print(" ---" * size)


# Function to solve the N-Queens problem using Iterative Deepening Search (IDS) algorithm
def solve_ids(size):
    """
    Solves the N-Queens problem using Iterative Deepening Search (IDS) algorithm.

    Parameters:
        size (int): The size of the chessboard (number of queens).

    Returns:
        List of Lists: List of solutions, where each solution is a list of queen positions.
    """
    for depth in range(size):
        solutions = depth_limited_search(size, depth)
        if solutions:
            return solutions
    return []


# Function for depth-limited search used in Iterative Deepening Search (IDS)
def depth_limited_search(size, max_depth):
    """
    Depth-limited search used in Iterative Deepening Search (IDS).

    Parameters:
        size (int): The size of the chessboard (number of queens).
        max_depth (int): The maximum depth for the search.

    Returns:
        List of Lists: List of solutions, where each solution is a list of queen positions.
    """
    solutions = []
    stack = [[]]

    while stack:
        solution = stack.pop()

        if conflict(solution):  # Check for conflicts in the configuration
            continue

        row = len(solution)

        if row == size:  # If all queens are placed, add the solution to the list
            solutions.append(list(solution))
            continue

        if row <= max_depth:  # Adjusted condition for depth limit
            # Generate all possible next configurations and add them to the stack
            for col in range(size):
                queen = [row, col]
                queens = list(solution)
                queens.append(queen)
                stack.append(queens)

    return solutions


# Function to solve the N-Queens problem using A* algorithm
def solve_a_star(size):
    """
    Solves the N-Queens problem using A* algorithm.

    Parameters:
        size (int): The size of the chessboard (number of queens).

    Returns:
        List of Lists: List of solutions, where each solution is a list of queen positions.
    """
    if size < 1:
        return []

    solutions = []  # Initialize an empty list to store solutions
    open_list = [{"queens": [], "cost": 0, "heuristic": randomHeuristic()}]  # Initialize open list with an empty board configuration, cost 0, and a random heuristic
    closed_list = set()  # Initialize a set to keep track of visited configurations

    while open_list:
        open_list.sort(key=lambda x: x["cost"] + x["heuristic"])  # Sort open list based on cost + heuristic
        item = open_list.pop(0)
        queens, cost = item["queens"], item["cost"]

        if conflict(queens):  # Check for conflicts in the configuration
            continue

        row = len(queens)

        if row == size:  # If all queens are placed, add the solution to the list
            solutions.append(list(queens))
            break

        # Generate all possible next configurations and add them to the open list with updated cost and heuristic
        for col in range(size):
            queen = [row, col]
            newQueens = list(queens) + [queen]
            newCost = cost + 1
            heuristic = randomHeuristic()
            open_list.append({"queens": newQueens, "cost": newCost, "heuristic": heuristic})

        closed_list.add(str(queens))  # Add the current configuration to the set of visited configurations

    return solutions


# Function to generate a random heuristic (used in A* algorithm)
def randomHeuristic():
    """
    Generates a random heuristic value (used in A* algorithm).

    Returns:
        float: Random heuristic value.
    """
    import random
    return random.random()


# Function to solve the N-Queens problem using Greedy algorithm
def solve_greedy(size):
    """
    Solves the N-Queens problem using Greedy algorithm.

    Parameters:
        size (int): The size of the chessboard (number of queens).

    Returns:
        List of Lists: List of solutions, where each solution is a list of queen positions.
    """
    if size < 1:
        return []

    solutions = []  # Initialize an empty list to store solutions

    for i in range(size):
        solution = placeQueensGreedy(size, i)
        if len(solution) == size:  # If all queens are placed, add the solution to the list
            solutions.append(solution)

    return solutions


# Function to place queens using Greedy algorithm
def placeQueensGreedy(size, startRow):
    queens = []  # Initialize an empty list to store queen positions

    for row in range(startRow, size):
        minConflicts = size
        minConflictCol = -1

        for col in range(size):
            conflictCount = countConflicts(queens, row, col)

            if conflictCount < minConflicts:
                minConflicts = conflictCount
                minConflictCol = col

        if minConflictCol != -1:  # If a non-conflicting position is found, place the queen
            queens.append([row, minConflictCol])

    return queens


# Function to count conflicts for a queen placement
def countConflicts(queens, row, col):
    conflicts = 0

    for qRow, qCol in queens:
        if qCol == col or qRow - qCol == row - col or qRow + qCol == row + col:
            conflicts += 1

    return conflicts
