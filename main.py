import tkinter as tk


# I'm using an OOP approach for this app.
# Check this Stack Overflow answer:
# https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application/17470842#17470842

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Initialize rest of the GUI here.
        greeting = tk.Label(text="Hello world!")
        greeting.pack()


# Try running this!
if __name__ == '__main__':
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
