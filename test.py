import unittest
import io
import os
from contextlib import redirect_stdout
from task import solve
from IO_handler import load_yaml_board, print_output
from Cell import parse_cell, Cell
from dragon_heap import DragonHeap

# in real world project each module will get file but this project is quite small


class TestDragonTask(unittest.TestCase):
    def test_simple_case(self):
        """Test the sample case with the provided input and output."""

        size = 5
        board = ["d 10", "d 12", "p 2", "d 1", "p 2"]
        result = solve(size, board)
        self.assertIsNotNone(result)
        self.assertEqual(result.total_gold, 13)
        self.assertEqual(len(result), 2)
        dragon_indices = [d.idx_in_arr for d in result.to_sorted_by_idx_list()]
        # 2,4 cause we use regular index
        self.assertEqual(dragon_indices, [1, 3])

    def test_complex_case(self):
        """Test the sample case with the provided input and output."""

        size = 8
        board = ["d 10", "d 29", "p 5", "d 1", "d 14", "p 2", "d 2", "p 2"]
        result = solve(size, board)
        self.assertIsNotNone(result)
        self.assertEqual(result.total_gold, 31)
        self.assertEqual(len(result), 2)
        dragon_indices = [d.idx_in_arr for d in result.to_sorted_by_idx_list()]
        self.assertEqual(dragon_indices, [1, 6])

    def test_input_and_inc2(self):
        """Test reading from a file"""
        # Create a temporary file with the test input from test_input.yml
        yaml_content = """
    6
    d 10
    d 12
    p 2
    d 1
    p 2
    """
        with open("input.yml", "w") as f:
            f.write(yaml_content)
        temp_file_path = "input.yml"

        try:
            size, board = load_yaml_board(temp_file_path)
            self.assertEqual(size, 6)  # Check board size
            self.assertEqual(len(board), 5)  # Check number of cells
            self.assertEqual(
                board, ["d 10", "d 12", "p 2", "d 1", "p 2"]
            )  # Check exact board content
        finally:
            os.remove(temp_file_path)

    def test_input_and_inc2(self):
        """Test reading from a file and printing the output."""

        dummy_heap = DragonHeap()

        dragon1 = Cell(10, False, 2)
        dragon2 = Cell(15, False, 4)
        dummy_heap.push(dragon1)
        dummy_heap.push(dragon2)

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            print_output(dummy_heap)
        # should inc in 2 because of anonying input format
        expected_output = "25\n2\n4 6\n"

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_no_solution_case(self):
        """Test a case where there is no solution."""
        size = 6
        board = [
            "d 10",
            "d 12",
            "p 2",
            "d 1",
            "p 3",
        ]
        result = solve(size, board)

        self.assertIsNone(result)

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            print_output(result)

        expected_output = "-1\n"

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_parse_cell(self):
        """Test reading and parsing cells from input strings."""
        dragon_cell_str = "d 15"
        dragon_cell = parse_cell(dragon_cell_str, 1)
        self.assertIsInstance(dragon_cell, Cell)
        self.assertEqual(dragon_cell.num, 15)
        self.assertEqual(dragon_cell.is_princess, False)
        self.assertEqual(dragon_cell.idx_in_arr, 1)

        princess_cell_str = "p 7"
        princess_cell = parse_cell(princess_cell_str, 2)
        self.assertIsInstance(princess_cell, Cell)
        self.assertEqual(princess_cell.num, 7)
        self.assertEqual(princess_cell.is_princess, True)
        self.assertEqual(princess_cell.idx_in_arr, 2)

        with self.assertRaises(ValueError):
            parse_cell("x 10", 5)  # Invalid cell type

        with self.assertRaises(ValueError):
            parse_cell("d10", 6)  # Invalid format (missing space)


if __name__ == "__main__":
    unittest.main()
