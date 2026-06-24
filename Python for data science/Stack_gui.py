import tkinter as tk
from tkinter import messagebox
from Stack_main import Stack

class StackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Operations GUI")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.stack = Stack()

        title = tk.Label(
            root,
            text="Interactive Stack Operation Program",
            font=("Arial", 18, "bold"),
            fg="blue"
        )
        title.pack(pady=10)

        # Entry
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Push",
            width=12,
            command=self.push_item,
            bg="lightgreen"
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Pop",
            width=12,
            command=self.pop_item,
            bg="salmon"
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Peek",
            width=12,
            command=self.peek_item,
            bg="lightblue"
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Is Empty",
            width=12,
            command=self.is_empty,
            bg="khaki"
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Size",
            width=12,
            command=self.stack_size,
            bg="orange"
        ).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=12,
            command=self.clear_stack,
            bg="lightgray"
        ).grid(row=2, column=1, padx=5, pady=5)

        # Stack Display
        tk.Label(
            root,
            text="Current Stack",
            font=("Arial", 14, "bold")
        ).pack()

        self.stack_display = tk.Listbox(
            root,
            width=40,
            height=12,
            font=("Arial", 12)
        )
        self.stack_display.pack(pady=10)

        # Status Label
        self.status = tk.Label(
            root,
            text="Ready",
            font=("Arial", 12),
            fg="green"
        )
        self.status.pack()

        self.update_display()

    def update_display(self):
        self.stack_display.delete(0, tk.END)

        for item in reversed(self.stack.item):
            self.stack_display.insert(tk.END, item)

    def push_item(self):
        item = self.entry.get().strip()

        if not item:
            messagebox.showwarning(
                "Input Error",
                "Please enter an item."
            )
            return

        self.stack.push(item)

        self.status.config(
            text=f"'{item}' pushed successfully",
            fg="green"
        )

        self.entry.delete(0, tk.END)
        self.update_display()

    def pop_item(self):
        try:
            top_item = self.stack.peek()

            self.stack.pop()

            self.status.config(
                text=f"'{top_item}' popped successfully",
                fg="red"
            )

            self.update_display()

        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def peek_item(self):
        try:
            item = self.stack.peek()

            messagebox.showinfo(
                "Top Item",
                f"Top Item: {item}"
            )

        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def is_empty(self):
        if self.stack.is_empty():
            messagebox.showinfo(
                "Stack Status",
                "Stack is Empty"
            )
        else:
            messagebox.showinfo(
                "Stack Status",
                "Stack is NOT Empty"
            )

    def stack_size(self):
        messagebox.showinfo(
            "Stack Size",
            f"Size: {self.stack.size()}"
        )

    def clear_stack(self):
        self.stack.item.clear()

        self.update_display()

        self.status.config(
            text="Stack Cleared",
            fg="purple"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = StackGUI(root)
    root.mainloop()