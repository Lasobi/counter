import tkinter as tk
from tkinter import ttk
import argparse


class Counter:
    def __init__(self, master, name, initial_count):
        self.master = master
        self.name = name
        self.count = initial_count

        # Create a new frame for the counter
        self.frame = ttk.Frame(self.master)
        self.frame.pack(pady=10)

        # Create a label to display the counter name
        if self.name:
            self.name_label = ttk.Label(
                self.frame, text=self.name, font=("Helvetica", 14, "bold")
            )
        else:
            self.name_label = ttk.Label(
                self.frame, text="Counter", font=("Helvetica", 14, "bold")
            )
        self.name_label.pack(side="top")

        # Create buttons to increment and decrement the count
        style = ttk.Style()
        style.configure(
            "TButton",
            padding=20,
            relief="flat",
            background="#d9d9d9",
            font=("Helvetica", 12),
        )

        self.increment_button_1 = ttk.Button(
            self.frame, text="+1", command=self.increment, style="TButton"
        )
        self.increment_button_1.pack(side="left", padx=10)

        self.increment_button_5 = ttk.Button(
            self.frame, text="+5", command=lambda: self.increment(5)
        )
        self.increment_button_5.pack(side="left", padx=10)

        self.increment_button_10 = ttk.Button(
            self.frame, text="+10", command=lambda: self.increment(10)
        )
        self.increment_button_10.pack(side="left", padx=10)

        self.decrement_button_1 = ttk.Button(
            self.frame, text="-1", command=self.decrement, style="TButton"
        )
        self.decrement_button_1.pack(side="right", padx=10)

        self.decrement_button_5 = ttk.Button(
            self.frame, text="-5", command=lambda: self.decrement(5)
        )
        self.decrement_button_5.pack(side="right", padx=10)

        self.decrement_button_10 = ttk.Button(
            self.frame, text="-10", command=lambda: self.decrement(10)
        )
        self.decrement_button_10.pack(side="right", padx=10)

        # Create a label to display the current count
        self.label = ttk.Label(
            self.frame, text=self.count, font=("Helvetica", 20)
        )
        self.label.pack(expand=True)

    def increment(self, value=1):
        self.count += value
        self.label.config(text=self.count)

    def decrement(self, value=1):
        self.count -= value
        self.label.config(text=self.count)


def main():
    parser = argparse.ArgumentParser(
        description="A program to create a window with one or more counters"
    )
    parser.add_argument(
        "names",
        metavar="name",
        type=str,
        nargs="*",
        help="a list of names for the counters",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        metavar="count_value",
        nargs="+",
        default=[],
        help="the initial count value(s) for the counters",
    )
    args = parser.parse_args()

    root = tk.Tk()
    root.title("Counters")

    if not args.names:
        Counter(root, "", 0)
    else:
        for i, name in enumerate(args.names):
            initial_count = args.count[i] if i < len(args.count) else 0
            Counter(root, name, initial_count)

    root.mainloop()


if __name__ == "__main__":
    main()
