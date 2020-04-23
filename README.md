# Conquer-Project
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import database as db

class screen1(ttk.Frame):
    def __init__(self, parent):
        self.parent = parent 
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)   
        path = 'C:/workspace-python/python/final project/resize.png' 
        image = Image.open(path)
        img = ImageTk.PhotoImage(image)
        reference = ttk.Label(self, image = img)
        reference.image = img
        reference.place(x = 95, y = 35)
        ttk.Label(self, text = "Guest Pass Program", font=("Ariel", 22)).place(height = 40, width = 300, x = 210, y = 145)
        ttk.Button(self, text="Add Guest Pass", command = self.screen2).place(height = 30, width = 350, x = 165, y = 190)
        ttk.Button(self, text="Add Member", command = self.screen2).place(height = 30, width = 350, x = 165, y = 225)
        ttk.Button(self, text="Guest List", command = self.screen2).place(height = 30, width = 350, x = 165, y = 260)
        ttk.Button(self, text="Member Pass Records", command = self.screen2).place(height = 30, width = 350, x = 165, y = 295)
        ttk.Button(self, text="Exit Program", command = self.screen2).place(height = 30, width = 350, x = 165, y = 330)
    
    def screen2(self):
        ttk.Label(self, text = "Hello").place(x = 300, y = 375)
    
def main():
    root = tk.Tk()
    root.title("Guest Pass Program")
    root.geometry("700x400")
    screen1(root)
    root.mainloop()

if __name__ == "__main__":
    main()
