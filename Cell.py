class Cell:
    def __init__(self, num: int, is_princess: bool, idx_in_arr: int):
        self.num = num
        self.is_princess = is_princess
        self.idx_in_arr = idx_in_arr


def parse_cell(cell_str: str, idx_in_arr: int) -> Cell:

    parts = cell_str.strip().split()
    if len(parts) != 2:
        raise ValueError(f"Invalid cell string format: {cell_str}")

    cell_type, num_str = parts
    num = int(num_str)

    if cell_type.lower() == "p":
        is_princess = True
    elif cell_type.lower() == "d":
        is_princess = False
    else:
        raise ValueError(f"Invalid cell type: {cell_type}. Must be 'p' or 'd'")

    return Cell(num, is_princess, idx_in_arr)
