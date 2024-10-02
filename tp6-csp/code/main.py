import CSPBacktracking
import CSPForwardChecking

if __name__ == "__main__":
    cspBack = CSPBacktracking.CSPBacktracking(8);
    solution = cspBack.solveCsp();
    print(solution)
    print(cspBack.iteration)

    cspForward = CSPForwardChecking.CSPForwardChecking(8);
    solution = cspForward.solveCsp()
    print(solution)
    print(cspForward.iteration)
