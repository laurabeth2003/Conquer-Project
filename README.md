'''
#Programmer: Laura Erickson and Ty Regehr

#Program Name: finalProject.py

#Created on: 4/21/2020

#Last edited: 4/23/2020
'''
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import database as db

class screendesign():
    def __init__(self):
        def screen2():
            def backtomain():
                root2.destroy()
                screendesign()
                
            def search():
                def contin():
                    ttk.Label(root2, text = "How many guests?", font = ("Ariel", 16)).place(height = 30, width = 200, x = 50, y = (i*35 + 105))
                    ttk.Button(root2, text = "1", command = root2.destroy).place(height = 30, width = 100, x = 250, y = (i*35 + 105))
                    ttk.Button(root2, text = "2", command = root2.destroy).place(height = 30, width = 100, x = 375, y = (i*35 + 105))
                    
                ttk.Label(root2).place(height = 370, width = 700, x = 0, y = 70)
                namelist = name.get()
                namelist = namelist.split()
                if (len(namelist) == 1): 
                    query = "SELECT memberFirstName, memberLastName, memberID FROM member WHERE memberFirstName = ?"
                    rows = db.read_table_1condition(db.create_connection(db.data), query, (namelist[0],))
                    i = 0
                    ttk.Label(root2, width=80, text= "First name").place(height = 30, width = 200, x = 50, y = 70)
                    ttk.Label(root2, width=80, text= "Last name").place(height = 30, width = 200, x = 250, y = 70)
                    ttk.Label(root2, width=80, text= "Member ID").place(height = 30, width = 200, x = 450, y = 70)
                    ttk.Label(root2, width=80, text= "Member?").place(height = 30, width = 200, x = 600, y = 70)
                    for row in rows:
                        i += 1
                        rowlist = list(row)
                        ttk.Label(root2, text = (str(i) + ".")).place(height = 30, width = 40, x = 10, y = (i*35 + 70))
                        ttk.Label(root2, text= rowlist[0]).place(height = 30, width = 200, x = 50, y = (i*35 + 70))
                        ttk.Label(root2, text= rowlist[1]).place(height = 30, width = 200, x = 250, y = (i*35 + 70))
                        ttk.Label(root2, text= rowlist[2]).place(height = 30, width = 150, x = 450, y = (i*35 + 70))
                        ttk.Button(root2, text = "Yes", command = contin).place(height = 30, width = 45, x = 600, y = (i*35 + 70))
            
                else:
                    query = "SELECT memberFirstName, memberLastName, memberID FROM member WHERE (memberFirstName = ? AND memberLastName = ?)"
                    rows = db.read_table_2condition(db.create_connection(db.data), query, namelist[0], namelist[1])
                    i = 1
                    ttk.Label(root2, width=80, text= "First name").place(height = 30, width = 200, x = 50, y = 70)
                    ttk.Label(root2, width=80, text= "Last name").place(height = 30, width = 200, x = 250, y = 70)
                    ttk.Label(root2, width=80, text= "Member ID").place(height = 30, width = 200, x = 450, y = 70)
                    ttk.Label(root2, width=80, text= "Member?").place(height = 30, width = 200, x = 600, y = 70)
                    for row in rows:
                        rowlist = list(row)
                        ttk.Label(root2, text = (str(i) + ".")).place(height = 30, width = 40, x = 10, y = (i*35 + 70))
                        ttk.Label(root2, text= rowlist[0]).place(height = 30, width = 200, x = 50, y = (i*35 + 70))
                        ttk.Label(root2, text= rowlist[1]).place(height = 30, width = 200, x = 250, y = (i*35 + 70))
                        ttk.Label(root2, text= rowlist[2]).place(height = 30, width = 150, x = 450, y = (i*35 + 70))
                        ttk.Button(root2, text = "Yes", command = contin).place(height = 30, width = 45, x = 600, y = (i*35 + 70))
            
                        i += 1
            
            root.destroy()
            root2 = tk.Tk()
            root2.title("Add Guest Pass")
            root2.geometry("700x400")
            ttk.Button(root2, text = "Exit Program", command = root2.destroy).place(height = 30, width = 100, x = 10, y = 0)
            ttk.Button(root2, text = "Back to Menu", command = backtomain).place(height = 30, width = 100, x = 590, y = 0)
            ttk.Label(root2, text = "Add Guest Pass", font=("Ariel", 18)).place(height= 30, width = 300, x = 265, y = 0)
            ttk.Label(root2, text = "Enter member name:", font = ("Ariel", 14)).place(height = 30, width = 200, x = 10, y = 35)
            name = tk.StringVar()
            ttk.Entry(root2, textvariable=name).place(height = 30, width = 350, x= 220, y = 35)
            ttk.Button(root2, text = "Search", command = search).place(height = 30, width = 100, x = 590, y = 35)
            root2.mainloop()
         
            
        def screen3():
            root.destroy()
            root3 = tk.Tk()
            root3.title("Add Member")
            root3.geometry("700x400")   
            
            ttk.Button(root3, text="Back to Menu", command = screendesign).place(height = 30, width = 100, x = 10, y = 0)
            ttk.Label(root3, text="Add Guest Pass").place(height = 30, width = 200, x= 300, y = 0)
            ttk.Button(root3, text="Exit Program", command=root3.destroy).place(height = 30, width = 100, x = 600, y = 0)
            ttk.Label(root3, text="Guest First Name:").place(height = 30, width = 200, x = 10, y = 50)
            self.firstName = tk.StringVar()
            ttk.Entry(root3, width=40, textvariable=self.firstName).place(height = 30, width = 200, x = 200, y = 50)
            ttk.Label(root3, text="Guest Last Name:").place(height = 30, width = 200, x = 10, y = 100)
            self.lastName = tk.StringVar()
            ttk.Entry(root3, width=40, textvariable=self.lastName).place(height = 30, width = 200, x = 200, y = 100)
            ttk.Label(root3, width=40, text="Member in System?").place(height = 30, width = 200, x = 10, y = 150)
            self.formermember = tk.StringVar()
            ttk.Entry(root3, width=80, textvariable=self.formermember, state="readonly").place(height = 30, width = 200, x = 200, y = 150)
            
            ttk.Label(root3, text="Guest First Name:").place(height = 30, width = 250, x = 10, y = 200)
            self.newMemberFirst = tk.StringVar()
            ttk.Entry(root3, width=40, textvariable=self.newMemberFirst).place(height = 30, width = 200, x = 220, y = 200)   
         
            ttk.Label(root3, text="Guest Last Name:").place(height = 30, width = 200, x = 10, y = 235)
            self.newMemberLast = tk.StringVar()
            ttk.Entry(root3, width=40, textvariable=self.newMemberLast).place(height = 30, width = 200, x = 220, y = 235)   
            
            ttk.Label(root3, text="Membership ID:").place(height = 30, width = 200, x = 10, y = 270)
            self.newMemberID = tk.StringVar()
            ttk.Entry(root3, width=40, textvariable=self.newMemberID).place(height = 30, width = 200, x = 220, y = 270)   
         
            ttk.Label(root3, text="Membership Type:").place(height = 30, width = 200, x = 10, y = 305)
            self.newMemberType = tk.StringVar()
            ttk.Entry(root3, width=40, textvariable=self.newMemberType).place(height = 30, width = 200, x = 220, y = 305)   
         
            ttk.Label(root3, text="Phone:").place(height = 30, width = 200, x = 10, y = 340)
            self.newMemberPhone = tk.StringVar()
            ttk.Entry(root3, width=40, textvariable=self.newMemberPhone).place(height = 30, width = 200, x = 220, y = 340)   
            
            ttk.Label(root3, text="Date of Birth:").place(height = 30, width = 200, x = 10, y = 375)
            self.newMemberDOB = tk.StringVar()
            ttk.Entry(root3, width=40, textvariable=self.newMemberDOB).place(height = 30, width = 200, x = 220, y = 375)   
         
            ttk.Label(root3, text="Age:").place(height = 30, width = 200, x = 10, y = 410)
            self.newMemberAge = tk.StringVar()
            ttk.Entry(root3, width=40, textvariable=self.newMemberAge).place(height = 30, width = 200, x = 220, y = 410)   
            
            
        def screen4():
            root.destroy()
            root4 = tk.Tk()
            root4.title("Guest List")
            root4.geometry("700x400")
            root4.mainloop()
                
        def screen5():
            root.destroy()
            root5 = tk.Tk()
            root5.title("Member Pass Records")
            root5.geometry("700x400")
            ttk.Button(root5, text="Add Guest Pass", command = root5.destroy).place(height = 30, width = 350, x = 165, y = 190)
            root5.mainloop()
             
        root = tk.Tk()
        root.title("Guest Pass Program")
        root.geometry("700x400")  
        path = 'C:/workspace-python/python/final project/resize.png' 
        image = Image.open(path)
        img = ImageTk.PhotoImage(image)
        reference = ttk.Label(root, image = img)
        reference.image = img
        reference.place(x = 95, y = 35)
        ttk.Label(root, text = "Guest Pass Program", font=("Ariel", 22)).place(height = 40, width = 300, x = 210, y = 145)
        ttk.Button(root, text="Add Guest Pass", command = screen2).place(height = 30, width = 350, x = 165, y = 190)
        ttk.Button(root, text="Add Member", command = screen3).place(height = 30, width = 350, x = 165, y = 225)
        ttk.Button(root, text="Guest List", command = screen4).place(height = 30, width = 350, x = 165, y = 260)
        ttk.Button(root, text="Member Pass Records", command = screen5).place(height = 30, width = 350, x = 165, y = 295)
        ttk.Button(root, text="Exit Program", command = root.destroy).place(height = 30, width = 350, x = 165, y = 330)
        root.mainloop()
            
def main():
    screendesign()
    
if __name__ == "__main__":
    main()
