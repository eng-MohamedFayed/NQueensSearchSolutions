from NQueensAlgorithms import solve_ucs, print_board

def main():
    size = int(input("Please enter the size of the board: "))

    ucs_solutions = solve_ucs(size)


    print("Uniform Cost Search (UCS) Solutions:")
    for i, solution in enumerate(ucs_solutions):
        print(f"UCS Solution {i + 1}:")
        print_board(solution, size)


    print(f"Total UCS solutions: {len(ucs_solutions)}")


if __name__ == "__main__":
    main()
