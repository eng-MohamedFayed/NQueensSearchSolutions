from NQueensAlgorithms import print_board, solve_greedy

def main():
    size = int(input("Please enter the size of the board: "))

    greedy_solutions = solve_greedy(size)

  

    print("Greedy Algorithm Solutions:")
    for i, solution in enumerate(greedy_solutions):
        print(f"Greedy Solution {i + 1}:")
        print_board(solution, size)

   
    print(f"Total Greedy solutions: {len(greedy_solutions)}")

if __name__ == "__main__":
    main()
