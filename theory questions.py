"""
1. a True The second player will play optimally, and so is perfectly predictable up to ties. Knowing which of two equally
good moves the opponent will make does not change the value of the game to the first player's move.
b. False . In a partially observable game, knowing the second play's move tells the first player additional information
about the game state that would otherwise be available only to the second player.
c. False. Backgammon is a game of chance, and the opponent may consistently roll much better dice. The correct statement
is that the expected winnings are optimal.

2 constraint : A constraint is a restriction on the possible values of two or more variables.
backtracking search : Backtracking search is a kind of depth- first search. For a certain search tree, backtracking and
DFS, the main difference is that backtracking method is not in the solution process . The complete tree structure is
preserved, while the depth-first search records the complete search tree/
arc consistency: A directed arc from variable A to variable B in a CSP is ar consistent if, for every value in the currents
domain of A, there is some consistent value of B.
Backjumpting: Backjumping is a way of making backtracking search more efficient,by jumping back more than one level when
a dead end is reached.
Min-conflicts is a heuristic for use with local search on CSP problems. The heuristic says that when given a variable to
modify. choose the value that conflicts with the fewest number of other variables
cycle cutset A cycle cutset is a set of variables which when removed from the constraint graph make it acyclic when the
variable of a cycle cutset are instantiated the remainder of the CSP can be solved in lineat time.

3.The most constrained variable makes sense because it chooses a variable that is likely to cause a failure, and it is
more efficient to fall as early as possible. The least constraining value heuristic makes sense because it allow ot allows
the most chances for future assignments to avoid conflict.

4 This procedure will give incorrecct results. Mathematically, the procedure amounts to assuming that averaging that
commutes with min and max, which it does not. Intuitively, the choices made by each player in the deterministic trees are
based on full knowledge of future dice rolls, and bear no necessary relationship to the moves made without such knowledge

"""