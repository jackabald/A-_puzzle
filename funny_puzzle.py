import heapq
import math

def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    distance = 0
    side_length = int(math.sqrt(len(to_state)))
    
    for i, state in enumerate(from_state):
        if state != 0:
            current = (i % side_length, i // side_length)
            goal_index = to_state.index(state)
            goal = (goal_index % side_length, goal_index // side_length) 
            distance += abs(current[0] - goal[0]) + abs(current[1] - goal[1])
    return distance

def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)

    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
    side_length = 3
    succ = []
    indices_of_zero = [i for i, x in enumerate(state) if x == 0]    
    
    #(row change, col change, index change)
    directions = [(-1, 0, -side_length), (1, 0, side_length),(0, -1, -1), (0, 1, 1)]
    
    for zero_index in indices_of_zero:
        row, col = divmod(zero_index, side_length)
        for row_change, col_change, index_change in directions:
            new_row, new_col = row + row_change, col + col_change
            if 0 <= new_row < side_length and 0 <= new_col < side_length:
                new_index = zero_index + index_change
                if state[new_index] != 0:
                    new_state = state[:]
                    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                    if new_state not in succ:  
                        succ.append(new_state)
    return sorted(succ)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """

    # This is a format helper，which is only designed for format purpose.
    # build "state_info_list", for each "state_info" in the list, it contains "current_state", "h" and "move".
    # define and compute max length
    # it can help to avoid any potential format issue.
    for state_info in state_info_list:
        current_state = state_info[0]
        h = state_info[1]
        move = state_info[2]
        print(current_state, "h={}".format(h), "moves: {}".format(move))
    print("Max queue length: {}".format(max_length))

if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([2,5,1,4,0,6,7,0,3])
    # print()

    #print(get_manhattan_distance([2,5,1,4,3,6,7,0,0], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    # print()

    #solve([2,5,1,4,0,6,7,0,3])
    #print()
