from NQueensAlgorithms import solve_bfs, print_board

def main():
    size = int(input("Please enter the size of the board: "))

    bfs_solutions = solve_bfs(size)


    print("Breadth-First Search (BFS) Solutions:")
    for i, solution in enumerate(bfs_solutions):
        print(f"BFS Solution {i + 1}:")
        print_board(solution, size)

    print(f"Total BFS solutions: {len(bfs_solutions)}")

if __name__ == "__main__":
    main()
