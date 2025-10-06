import heapq

from Cell import Cell


class DragonHeap:
    def __init__(self):
        self.heap = []
        self.total_gold = 0

    def push(self, item: Cell):
        # min heap sorted by item.num
        heapq.heappush(self.heap, (item.num, item))
        self.total_gold += item.num

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        popped_item = heapq.heappop(self.heap)
        self.total_gold -= popped_item[1].num

    def truncate_heap_to_len(self, n):
        while len(self.heap) > n:
            self.pop()

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def to_sorted_by_idx_list(self) -> list[Cell]:
        items = [item for (_, item) in self.heap]
        return sorted(items, key=lambda cell: cell.idx_in_arr)
