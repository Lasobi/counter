import unittest
from counter import Counter
import tkinter as tk


class TestCounter(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.counter = Counter(self.root, "TestCounter", 0)

    def test_increment(self):
        self.counter.increment()
        self.assertEqual(self.counter.count, 1)

    def test_decrement(self):
        self.counter.increment()
        self.counter.increment()
        self.counter.decrement()
        self.assertEqual(self.counter.count, 1)


if __name__ == "__main__":
    unittest.main()
