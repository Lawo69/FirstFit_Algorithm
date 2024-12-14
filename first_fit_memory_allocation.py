import tkinter as tk
from tkinter import messagebox

# First Fit Logic
def first_fit(block_sizes, process_sizes):
    allocations = [-1] * len(process_sizes)
    for i, process in enumerate(process_sizes):
        for j, block in enumerate(block_sizes):
            if block >= process:
                allocations[i] = j
                block_sizes[j] -= process
                break
    return allocations

# GUI Application
def allocate_memory():
    try:
        blocks = list(map(int, block_input.get().split(",")))
        processes = list(map(int, process_input.get().split(",")))

        initial_blocks = blocks.copy()
        allocations = first_fit(blocks, processes)

        # Display results
        result = ""
        for i, process in enumerate(processes):
            if allocations[i] != -1:
                result += f"Process {i+1} (Size {process}) -> Block {allocations[i]+1}\n"
            else:
                result += f"Process {i+1} (Size {process}) -> Not Allocated\n"

        result += f"\nRemaining Block Sizes: {blocks}"
        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer values separated by commas.")

# GUI Setup
app = tk.Tk()
app.title("First Fit Memory Allocation")
app.geometry("500x400")

tk.Label(app, text="First Fit Memory Allocation", font=("Arial", 16)).pack(pady=10)

# Input Fields
tk.Label(app, text="Enter Block Sizes (comma-separated):").pack()
block_input = tk.Entry(app, width=50)
block_input.pack()

tk.Label(app, text="Enter Process Sizes (comma-separated):").pack()
process_input = tk.Entry(app, width=50)
process_input.pack()

# Allocate Button
allocate_btn = tk.Button(app, text="Allocate Memory", command=allocate_memory)
allocate_btn.pack(pady=10)

# Result Display
result_label = tk.Label(app, text="", justify="left", font=("Courier", 10))
result_label.pack(pady=10)

# Run Application
app.mainloop()
