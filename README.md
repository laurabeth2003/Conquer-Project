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
from datetime import date

i = 0
memberIDlist = []
def calculate_year(birthDate): 
    birthDate = birthDate.replace("/"," ")
    birthDate = birthDate.replace("."," ")
    birthDate = birthDate.split()
    birthDate = date(int(birthDate[2]),int(birthDate[0]),int(birthDate[1]))
    today = date.today() 
    years = today.year - birthDate.year
    if ((today.month, today.day) < (birthDate.month, birthDate.day)):
        years = years - 1
        
    return years
x = 0
y = 0


class screendesign():
    def __init__(self):
        def screen2():
            def motion(event):
                global x
                global y
                x = root2.winfo_pointerx() - root2.winfo_rootx()
                y = root2.winfo_pointery() - root2.winfo_rooty()

            
            def backtomain():
                root2.destroy()
                screendesign()
                
            def search():
                def contin():
                    global i
                    global y
                    for m in range(0, len(memberIDlist)):
                        if (y <= (135 + (m*35)) and y >= (105 + (m*35))):
                            memberID = memberIDlist[m]
        
                    def guestsearch():
                        def addguest():
                            def insertguest():
                                phoneentry = (phone.get())
                                phoneentry = phoneentry.replace("(", "")
                                phoneentry = phoneentry.replace(")", "-")
                                phoneentry = phoneentry.replace(".", "-")
                                if (len(phoneentry) == 10): 
                                    phoneentry = (phoneentry[0:3] + "-" + phoneentry[3:6] + "-" + phoneentry[6:10])
                                elif (len(phoneentry) == 11):
                                    phoneentry = (phoneentry[0:7] + "-" + phoneentry[7:11])
                                query = "SELECT guestID FROM guest"   
                                rows = db.read_table(db.create_connection(db.data), query)
                                length = len(rows)
                                listingID = []
                                if (length != 0):
                                    for row in rows:
                                        listID = list(row)
                                        listingID.append(listID[0])
                                    listingID = sorted(listingID)
                                    guestID = listingID[length - 1]
                                    guestID += 1
                                else:
                                    guestID = 100000001
                                query = "INSERT INTO guest VALUES (?,?,?,?,?,?,?,?)"
                                query2 = "INSERT INTO visits VALUES (?,?,?,?,?,?,?,?,?)"
                                db.insertguest(db.create_connection(db.data), query, guestID, memberID, first.get(), last.get(), email.get(), phoneentry, birthdate.get(), calculate_year(birthdate.get()))
                                db.insertvisits(db.create_connection(db.data), query2, guestID, memberID, first.get(), last.get(), email.get(), phoneentry, birthdate.get(), calculate_year(birthdate.get()), today.get())
                                ttk.Label(root2, text = "                                  Guest Added", font = ("Ariel", 18)).place(height = 40, width = 600, x = 50, y = 280)
        
                            first = tk.StringVar()
                            last = tk.StringVar()
                            email = tk.StringVar()
                            phone = tk.StringVar()
                            today = tk.StringVar()
                            birthdate = tk.StringVar()
                            ttk.Label(root2).place(height = 370, width = 700, x = 0, y = 35)
                            ttk.Label(root2, text = "Guest First Name:").place(height = 30, width = 250, x = 50, y = 70)
                            ttk.Entry(root2, textvariable= first).place(height = 30, width = 300, x = 300, y = 70)  
                            ttk.Label(root2, text = "Guest Last Name:").place(height = 30, width = 250, x = 50, y = 105)
                            ttk.Entry(root2, textvariable= last).place(height = 30, width = 300, x = 300, y = 105)  
                            ttk.Label(root2, text = "Guest Email:").place(height = 30, width = 250, x = 50, y = 140)
                            ttk.Entry(root2, textvariable= email).place(height = 30, width = 300, x = 300, y = 140)  
                            ttk.Label(root2, text = "Guest Phone Number:").place(height = 30, width = 250, x = 50, y = 175)
                            ttk.Entry(root2, textvariable= phone).place(height = 30, width = 300, x = 300, y = 175)  
                            ttk.Label(root2, text = "Guest Birth Date:").place(height = 30, width = 250, x = 50, y = 210)
                            ttk.Entry(root2, textvariable= birthdate).place(height = 30, width = 300, x = 300, y = 210)  
                            ttk.Label(root2, text = "Today's Date:").place(height = 30, width = 250, x = 50, y = 245)
                            ttk.Entry(root2, textvariable= today).place(height = 30, width = 300, x = 300, y = 245) 
                            ttk.Button(root2, text = "Enter Guest into Database", command = insertguest).place(height = 30, width = 600, x = 50, y = 280)
                        
                        global i
                        ttk.Label(root2).place(height = 370, width = 700, x = 0, y = i*35 + 175)
                        listguest = guestname.get()
                        listguest = listguest.split()
                        if (len(listguest) == 1): 
                            query = "SELECT guestFirstName, guestLastName, guestID FROM guest WHERE guestFirstName = ?"
                            guests = db.read_table_1condition(db.create_connection(db.data), query, (listguest[0],))
                            j = 0
                            length = (len(guests))
                            if (length == 0):
                                ttk.Label(root2).place(height = 370, width = 700, x = 0, y = i*35 + 175)
                                ttk.Button(root2, text= "Add New Guest?", command = addguest).place(height = 30, width = 600, x = 50, y = i*35 + 175)
                            if (length > 0):
                                ttk.Label(root2, width=80, text= "First name").place(height = 30, width = 200, x = 50, y = i*35 + 175)
                                ttk.Label(root2, width=80, text= "Last name").place(height = 30, width = 200, x = 250, y = i*35 + 175)
                                ttk.Label(root2, width=80, text= "GuestID").place(height = 30, width = 200, x = 450, y = i*35 + 175)
                                ttk.Label(root2, width=80, text= "Guest?").place(height = 30, width = 200, x = 600, y = i*35 + 175)
                                for row in guests:
                                    j += 1
                                    i += 1
                                    guestlist = list(row)
                                    ttk.Label(root2, text = (str(j) + ".")).place(height = 30, width = 40, x = 10, y = i*35 + 175)
                                    ttk.Label(root2, text= guestlist[0]).place(height = 30, width = 200, x = 50, y = i*35 + 175)
                                    ttk.Label(root2, text= guestlist[1]).place(height = 30, width = 200, x = 250, y = i*35 + 175)
                                    ttk.Label(root2, text= guestlist[2]).place(height = 30, width = 150, x = 450, y = i*35 + 175)
                                    ttk.Button(root2, text = "Yes", command = root2.destroy).place(height = 30, width = 45, x = 600, y = i*35 + 175)
                                    ttk.Button(root2, text = "No", command = addguest).place(height = 30, width = 45, x = 650, y = i*35 + 175)
                                
            
                        else:
                            query = "SELECT guestFirstName, guestLastName, guestID FROM guest WHERE (guestFirstName = ? AND guestLastName = ?)"
                            rows = db.read_table_2condition(db.create_connection(db.data), query, listguest[0], listguest[1])
                            length = (len(rows))
                            if (length == 0):
                                ttk.Label(root2).place(height = 370, width = 700, x = 0, y = i*35 + 175)
                                ttk.Button(root2, text= "Add New Guest?", command = addguest).place(height = 30, width = 600, x = 50, y = i*35 + 175)
                            if (length > 0):
                                ttk.Label(root2).place(height = 370, width = 700, x = 0, y = i*35 + 175)
                                ttk.Button(root2, text= "Add New Guest?", command = addguest).place(height = 30, width = 600, x = 50, y = i*35 + 175)
                                ttk.Label(root2, width=80, text= "First name").place(height = 30, width = 200, x = 50, y = (i*35 + 175))
                                ttk.Label(root2, width=80, text= "Last name").place(height = 30, width = 200, x = 250, y = (i*35 + 175))
                                ttk.Label(root2, width=80, text= "Member ID").place(height = 30, width = 200, x = 450, y = (i*35 + 175))
                                ttk.Label(root2, width=80, text= "Guest?").place(height = 30, width = 200, x = 600, y = (i*35 + 175))
                                j = 0
                                memberIDlist = []
                                for row in rows:
                                    memberIDlist.append(rowlist[2])
                                    j += 1
                                    i += 1
                                    rowlist = list(row)
                                    ttk.Label(root2, text = (str(j) + ".")).place(height = 30, width = 40, x = 10, y = (i*35 + 175))
                                    ttk.Label(root2, text= rowlist[0]).place(height = 30, width = 200, x = 50, y = (i*35 + 175))
                                    ttk.Label(root2, text= rowlist[1]).place(height = 30, width = 200, x = 250, y = (i*35 + 175))
                                    ttk.Label(root2, text= rowlist[2]).place(height = 30, width = 150, x = 450, y = (i*35 + 175))
                                    ttk.Button(root2, text = "Yes", command = contin).place(height = 30, width = 45, x = 600, y = (i*35 + 175))
                                    ttk.Button(root2, text = "No", command = root2.destroy).place(height = 30, width = 45, x = 650, y = (i*35 + 175))
                            
                       
                    ttk.Label(root2, text = "How many guests?", font = ("Ariel", 16)).place(height = 30, width = 200, x = 50, y = (i*35 + 105))
                    ttk.Button(root2, text = "1").place(height = 30, width = 100, x = 250, y = (i*35 + 105))
                    ttk.Button(root2, text = "2").place(height = 30, width = 100, x = 375, y = (i*35 + 105))
                    # if member chooses one and has at least one guest pass remaining, continue
                    # if member chooses two and has only one guest pass remaining, state "Member has only one guest pass remaining... please enter info of one of the guests"
                    # if member chooses two and has both guest passes remaining, run continue function twice. 
                    # can't program now, as it will need to link to the guest list screen
                    ttk.Label(root2, text = "Enter guest name:", font = ("Ariel", 14)).place(height = 30, width = 200, x = 10, y = (i*35 + 140))
                    guestname = tk.StringVar()
                    ttk.Entry(root2, textvariable=guestname).place(height = 30, width = 350, x= 220, y = (i*35 + 140))
                    ttk.Button(root2, text = "Search", command = guestsearch).place(height = 30, width = 100, x = 590, y = (i*35 + 140))
                    
        
                global i
                global memberIDlist
                global x
                global y
                i = 0 
                root2.bind_all('<Button-1>', motion)
                ttk.Label(root2).place(height = 370, width = 700, x = 0, y = 70)
                namelist = name.get()
                namelist = namelist.split()
                if (len(namelist) == 1): 
                    query = "SELECT memberFirstName, memberLastName, memberID FROM member WHERE memberFirstName = ?"
                    rows = db.read_table_1condition(db.create_connection(db.data), query, (namelist[0],))
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
                        memberIDlist.append(rowlist[2])
            
                else:
                    query = "SELECT memberFirstName, memberLastName, memberID FROM member WHERE (memberFirstName = ? AND memberLastName = ?)"
                    rows = db.read_table_2condition(db.create_connection(db.data), query, namelist[0], namelist[1])
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
