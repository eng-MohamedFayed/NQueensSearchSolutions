from NQueensAlgorithms import solve_a_star, print_board

def main():
    size = int(input("Please enter the size of the board: "))

    
    astar_solutions = solve_a_star(size)


    print("A* Search Solutions:")
    for i, solution in enumerate(astar_solutions):
        print(f"A* Solution {i + 1}:")
        print_board(solution, size)


    print(f"Total A* solutions: {len(astar_solutions)}")

if __name__ == "__main__":
    main()
