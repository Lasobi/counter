import tkinter as tk
from tkinter import ttk
import argparse

class Counter:
    def __init__(self, master, name, size, initial_count):
        self.master = master
        self.name = name
        self.count = initial_count
        
        # Create a new frame for the counter
        self.frame = ttk.Frame(self.master)
        self.frame.pack(pady=10)
        
        # Create a label to display the counter name
        if self.name:
            self.name_label = ttk.Label(self.frame, text=self.name, font=("Helvetica", 14, "bold"))
        else:
            self.name_label = ttk.Label(self.frame, text="Counter", font=("Helvetica", 14, "bold"))
        self.name_label.pack(side="top")
        
        # Create buttons to increment and decrement the count
        style = ttk.Style()
        style.configure("TButton", padding=20, relief="flat", background="#d9d9d9", font=('Helvetica', 12))
        self.increment_button = ttk.Button(self.frame, text="+", command=self.increment, style="TButton")
        self.increment_button.pack(side="left", padx=10)
        self.decrement_button = ttk.Button(self.frame, text="-", command=self.decrement, style="TButton")
        self.decrement_button.pack(side="right", padx=10)
        
        # Create a label to display the current count
        self.label = ttk.Label(self.frame, text=self.count, font=("Helvetica", 20))
        self.label.pack(expand=True)

    def increment(self):
        self.count += 1
        self.label.config(text=self.count)
    
    def decrement(self):
        self.count -= 1
        self.label.config(text=self.count)

def main():
    parser = argparse.ArgumentParser(description='A program to create multiple counters')
    parser.add_argument('names', metavar='name', type=str, nargs='*', help='a list of names for the counters')
    parser.add_argument('-s', '--size', type=int, default=100, help='the size of the counters')
    parser.add_argument('-c', '--count', type=int, metavar='count_value', nargs='+', default=[], help='the initial count value(s) for the counters')
    args = parser.parse_args()

    root = tk.Tk()
    root.title('Counters')

    counters_height = len(args.names) * 60  # Adjust the height based on the number of counters
    min_window_width = args.size
    min_window_height = counters_height + 100  # Add extra padding for window borders and controls

    root.minsize(min_window_width, min_window_height)

    if not args.names:
        Counter(root, "", args.size, 0)
    else:
        for i, name in enumerate(args.names):
            initial_count = args.count[i] if i < len(args.count) else 0
            Counter(root, name, args.size, initial_count)

    root.mainloop()

if __name__ == '__main__':
    main()
