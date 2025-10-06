from Cell import parse_cell
from dragon_heap import DragonHeap
from IO_handler import load_yaml_board, print_output
import sys


def solve(size: int, board: list[str]):
    # cant have more dragons than cells in arr..
    curr_dragon_ceil = size
    dragon_heap = DragonHeap()

    # Process all cells except the last one
    for idx, cell_str in enumerate(board[:-1]):
        # in real world situation would have preprocessed probably to
        #  make more modular and better to unit test,
        #  but "one run" definition in the problem might hint against it.
        cell = parse_cell(cell_str, idx)

        if cell.is_princess:
            curr_dragon_ceil = min(curr_dragon_ceil, cell.num)
            curr_len = len(dragon_heap)
            if curr_dragon_ceil <= curr_len:
                # throw out the least valuable dragons
                dragon_heap.truncate_heap_to_len(curr_dragon_ceil - 1)
        else:
            # dragon
            dragon_heap.push(cell)

    # Check if the last princess's requirement can be satisfied
    # assuming last is princess because task dont say what to do otherwise
    last_cell = parse_cell(board[-1], len(board) - 1)
    if last_cell.num > len(dragon_heap):
        return None

    return dragon_heap


if __name__ == "__main__":

    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.yml"

    size, board = load_yaml_board(input_file)

    result = solve(size, board)

    print_output(result)
