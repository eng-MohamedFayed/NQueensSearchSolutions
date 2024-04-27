from NQueensAlgorithms import solve_ids, print_board

def main():
    size = int(input("Please enter the size of the board: "))

 
    ids_solutions = solve_ids(size)

    print("Iterative Deepening Search (IDS) Solutions:")
    for i, solution in enumerate(ids_solutions):
        print(f"IDS Solution {i + 1}:")
        print_board(solution, size)

    print(f"Total IDS solutions: {len(ids_solutions)}")


if __name__ == "__main__":
    main()
