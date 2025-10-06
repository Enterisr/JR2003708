from dragon_heap import DragonHeap


def load_yaml_board(file_path: str):
    with open(file_path, "r") as file:
        data = file.readlines()

    size = int(data[0].strip()) - 1
    board = data[1:]
    return size, board


def print_output(dragon_heap: DragonHeap | None):
    if dragon_heap is None:
        print("-1")
        return

    print(dragon_heap.total_gold)
    print(len(dragon_heap))

    dragon_lst = dragon_heap.to_sorted_by_idx_list()
    result = ""

    for dragon in dragon_lst:
        # +2 because numbering of lines is 1-based+first line is size of arr.
        # i think its the domain of the output,
        #  buisness logic abstracted away from specific output details
        result += str(dragon.idx_in_arr + 2) + " "
    print(result.strip())
