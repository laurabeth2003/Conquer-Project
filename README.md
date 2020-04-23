import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import database as db

class screendesign(ttk.Frame):
    def screen2(self):
        self.root1.destroy()
        root2 = tk.Tk()
        root2.title("Add Guest Pass")
        root2.geometry("700x400")
        ttk.Button(root2, text = "Exit Program", command = root2.destroy).place(height = 30, width = 100, x = 10, y = 0)
        ttk.Button(root2, text = "Back to Menu", command = self.screen1).place(height = 30, width = 100, x = 600, y = 0)
        root2.mainloop()
            
    def screen3(self):
        self.root1.destroy()
        root3 = tk.Tk()
        root3.title("Add Member")
        root3.geometry("700x400")
        root3.mainloop()
            
            
    def screen4(self):
        self.root1.destroy()
        root4 = tk.Tk()
        root4.title("Guest List")
        root4.geometry("700x400")
        root4.mainloop()
                
    def screen5(self):
        self.root1.destroy()
        root5 = tk.Tk()
        root5.title("Member Pass Records")
        root5.geometry("700x400")
        ttk.Button(root5, text="Add Guest Pass", command = root5.destroy).place(height = 30, width = 350, x = 165, y = 190)
        root5.mainloop()
         
    def screen1(self):    
        root1 = tk.Tk()
        root1.title("Guest Pass Program")
        root1.geometry("700x400")  
        path = 'C:/workspace-python/python/final project/resize.png' 
        image = Image.open(path)
        img = ImageTk.PhotoImage(image)
        reference = ttk.Label(root1, image = img)
        reference.image = img
        reference.place(x = 95, y = 35)
        ttk.Label(root1, text = "Guest Pass Program", font=("Ariel", 22)).place(height = 40, width = 300, x = 210, y = 145)
        ttk.Button(root1, text="Add Guest Pass", command = self.screen2).place(height = 30, width = 350, x = 165, y = 190)
        ttk.Button(root1, text="Add Member", command = self.screen3).place(height = 30, width = 350, x = 165, y = 225)
        ttk.Button(root1, text="Guest List", command = self.screen4).place(height = 30, width = 350, x = 165, y = 260)
        ttk.Button(root1, text="Member Pass Records", command = self.screen5).place(height = 30, width = 350, x = 165, y = 295)
        ttk.Button(root1,text="Exit Program", command = self.parent.destroy).place(height = 30, width = 350, x = 165, y = 330)
        root1.mainloop()
            
            
def main():
    screendesign.screen1
    
if __name__ == "__main__":
    main()
