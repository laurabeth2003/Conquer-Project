'''
#Programmer: Laura Erickson and Ty Regehr

#Program Name: finalProject.py

#Created on: 4/21/2020

#Last edited: 4/26/2020
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import database as db
from datetime import date


membertype = ""
i = 0
memberID = 0
guestID =  0
currentmemberID = 0
memberIDlist = []
uniqueIDs = []
start = ""
end = ""
guestname = 0
currentmonth = 0
currentyear = 0 
todaymonth = 0
todayyear = 0
x = 0
y = 0
u = 0
go = 0
guestname = ""
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

def calculate_date(Date):
    Date = Date.replace("/", " ")
    Date = Date.replace("-", " ")
    Date = Date.replace(".", " ")
    Date = Date.split()
    Date = date(int(Date[2]),int(Date[0]),int(Date[1]))
    
    return Date

        
def calculate_monthyear(currentdate):
    global currentmonth
    global currentyear
    currentdate = currentdate.replace("/"," ")
    currentdate = currentdate.replace("."," ")
    currentdate = currentdate.split()
    currentmonth = int(currentdate[0])
    currentyear = int(currentdate[2])
    return currentmonth, currentyear

def today():
    global todaymonth
    global todayyear
    today = str(date.today())
    today = today.replace("-"," ")
    today = today.split()
    todaymonth = int(today[1])
    todayyear = int(today[0])   
    return todaymonth, todayyear  
    
def todaydate():
    todays = str(date.today())
    todays = todays.replace("-"," ")
    todays = todays.split()
    todays = str((todays[1]) + "/" + (todays[2]) + "/" + (todays[0]))
    return todays



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
                global u
                u = 0
                def contin():
                    def two():
                        global go
                        global u
                        global memberID  
                        global currentmonth
                        global currentyear
                        global todaymonth
                        global todayyear
                        global i
                        global guestname
                        guestname = 0
                        today()
                        query = "SELECT visitDate FROM visits WHERE memberID = ?"
                        rows = db.read_table_1condition(db.create_connection(db.data), query, (memberID,))
                        for row in rows:
                            datelist = list(row)
                            calculate_monthyear(datelist[0])
                            if (currentmonth == todaymonth and currentyear == todayyear):
                                u += 1
                        if (u == 0):
                            ttk.Label(root2, text = "Member now has 0 passes left this month", font = ("Ariel", 12)).place(height = 30, width = 300, x = 200, y = (i*35 + 140))
                            i += 1
                            go = 1
                            ttk.Label(root2, text = "Enter guest name:", font = ("Ariel", 14)).place(height = 30, width = 200, x = 10, y = (i*35 + 140))
                            guestname = tk.StringVar()
                            ttk.Entry(root2, textvariable=guestname).place(height = 30, width = 350, x= 220, y = (i*35 + 140))
                            ttk.Button(root2, text = "Search", command = guestsearch).place(height = 30, width = 100, x = 590, y = (i*35 + 140))
                        if (u == 1):
                            ttk.Label(root2, text = "This member only has one pass left. They will only be able to get one guest free", font = ("Ariel", 12)).place(height = 30, width = 600, x = 50, y = (i*35 + 140))
                            i += 1
                            go = 0
                            ttk.Label(root2, text = "Enter guest name:", font = ("Ariel", 14)).place(height = 30, width = 200, x = 10, y = (i*35 + 140))
                            guestname = tk.StringVar()
                            ttk.Entry(root2, textvariable=guestname).place(height = 30, width = 350, x= 220, y = (i*35 + 140))
                            ttk.Button(root2, text = "Search", command = guestsearch).place(height = 30, width = 100, x = 590, y = (i*35 + 140))
                        elif (u >= 2): 
                            go = 0
                            ttk.Label(root2, text = "This member is already out of passes", font = ("Ariel", 18)).place(height = 50, width = 450, x = 160, y = (i*35 + 170))
                    def one():
                        global u
                        global memberID  
                        global currentmonth
                        global currentyear
                        global todaymonth
                        global todayyear
                        global i
                        global guestname
                        global go
                        guestname = 0
                        go = 0
                        today()
                        query = "SELECT visitDate FROM visits WHERE memberID = ?"
                        rows = db.read_table_1condition(db.create_connection(db.data), query, (memberID,))
                        for row in rows:
                            datelist = list(row)
                            calculate_monthyear(datelist[0])
                            if (currentmonth == todaymonth and currentyear == todayyear):
                                u += 1
                        if (u == 0):
                            ttk.Label(root2, text = "Member now has 1 pass left this month", font = ("Ariel", 12)).place(height = 30, width = 300, x = 200, y = (i*35 + 140))
                            i += 1
                            ttk.Label(root2, text = "Enter guest name:", font = ("Ariel", 14)).place(height = 30, width = 200, x = 10, y = (i*35 + 140))
                            guestname = tk.StringVar()
                            ttk.Entry(root2, textvariable=guestname).place(height = 30, width = 350, x= 220, y = (i*35 + 140))
                            ttk.Button(root2, text = "Search", command = guestsearch).place(height = 30, width = 100, x = 590, y = (i*35 + 140))
                        if (u == 1):
                            ttk.Label(root2, text = "Member now has 0 passes left this month", font = ("Ariel", 12)).place(height = 30, width = 300, x = 200, y = (i*35 + 140))
                            i += 1
                            ttk.Label(root2, text = "Enter guest name:", font = ("Ariel", 14)).place(height = 30, width = 200, x = 10, y = (i*35 + 140))
                            guestname = tk.StringVar()
                            ttk.Entry(root2, textvariable=guestname).place(height = 30, width = 350, x= 220, y = (i*35 + 140))
                            ttk.Button(root2, text = "Search", command = guestsearch).place(height = 30, width = 100, x = 590, y = (i*35 + 140))
                        elif (u >= 2): 
                            ttk.Label(root2, text = "This member is already out of passes", font = ("Ariel", 18)).place(height = 50, width = 450, x = 160, y = (i*35 + 170))
                        
                    
                                
                            
                    def guestsearch():
                        global guestname
                        def yes():
                            global y
                            global i
                            global guestID
                            global go
                            global memberID
                            global guestname 
                            guestname = 0
                            root2.bind('<Button-1>', motion)
                            g = i
                            for m in range(0, len(guestIDlist)):
                                if (y <= (245 + (g*35)) and y >= (210 + (g*35))):
                                    guestID = guestIDlist[m]       
                                g += 1
                            query = "SELECT * FROM guest WHERE guestID = ?"   
                            information = db.read_table_1condition(db.create_connection(db.data), query, (guestID,))
                            for info in information:
                                info = list(info)
                            query2 = "INSERT INTO visits VALUES (?,?,?,?,?,?,?,?,?)"
                            db.insertvisits(db.create_connection(db.data), query2, info[0], memberID, info[2], info[3], info[4], info[5], info[6], info[7], todaydate())
                            ttk.Label(root2, text = "Guest Pass Added", font = ("Ariel", 13)).place(height = 30, width = 200, x = 250, y = (210 + (g*35)))
                            if (go == 0):
                                backtomain()
                            if (go == 1): 
                                ttk.Label(root2).place(height = 365, width = 700, x = 0, y = 35)
                                ttk.Label(root2, text = "Enter Guest 2:", font = ("Ariel",18)).place(height = 30, width = 350, x = 100, y = 35)
                                guestname = tk.StringVar()
                                ttk.Label(root2, text = "Enter guest name:", font = ("Ariel", 14)).place(height = 30, width = 200, x = 10, y = 70)
                                ttk.Entry(root2, textvariable=guestname).place(height = 30, width = 350, x= 220, y = (70))
                                ttk.Button(root2, text = "Search", command = guestsearch).place(height = 30, width = 100, x = 590, y = 70)
                                i = -2
                                go = 0
                                
                                
                        def addguest():
                            def insertguest():
                                global guestname
                                global i
                                global go
                                phoneentry = (phone.get())
                                phoneentry = phoneentry.strip()
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
                                
                                firstname = (first.get())
                                firstname = firstname.strip()
                                lastname = last.get()
                                lastname = lastname.strip()
                                guestemail = email.get()
                                guestemail = guestemail.strip()
                                todayDate = today.get()
                                todayDate = todayDate.strip()
                                guestbirthdate = birthdate.get()
                                guestbirthdate = guestbirthdate.strip()
                                query = "INSERT INTO guest VALUES (?,?,?,?,?,?,?,?)"
                                query2 = "INSERT INTO visits VALUES (?,?,?,?,?,?,?,?,?)"
                                db.insertguest(db.create_connection(db.data), query, guestID, memberID, firstname, lastname, guestemail, phoneentry, guestbirthdate, calculate_year(str(guestbirthdate)))
                                db.insertvisits(db.create_connection(db.data), query2, guestID, memberID, firstname, lastname, guestemail, phoneentry, guestbirthdate, calculate_year(str(guestbirthdate)), todayDate)
                                ttk.Label(root2, text = "                                  Guest Added", font = ("Ariel", 18)).place(height = 40, width = 600, x = 50, y = 280)
                                if (go == 1):
                                    ttk.Label(root2).place(height = 365, width = 700, x = 0, y = 35)
                                    ttk.Label(root2, text = "Enter Guest 2:", font = ("Ariel",18)).place(height = 30, width = 350, x = 100, y = 35)
                                    guestname = tk.StringVar()
                                    ttk.Label(root2, text = "Enter guest name:", font = ("Ariel", 14)).place(height = 30, width = 200, x = 10, y = 70)
                                    ttk.Entry(root2, textvariable=guestname).place(height = 30, width = 350, x= 220, y = (70))
                                    ttk.Button(root2, text = "Search", command = guestsearch).place(height = 30, width = 100, x = 590, y = 70)
                                    i = -2
                                    go = 0
                                    
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
                        guestIDlist = []
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
                                ttk.Label(root2, width=80, text= "Guest ID").place(height = 30, width = 200, x = 450, y = i*35 + 175)
                                ttk.Label(root2, width=80, text= "Guest?").place(height = 30, width = 200, x = 600, y = i*35 + 175)
                                
                                for row in guests:
                                    j += 1
                                    i += 1
                                    guestlist = list(row)
                                    ttk.Label(root2, text = (str(j) + ".")).place(height = 30, width = 40, x = 10, y = i*35 + 175)
                                    ttk.Label(root2, text= guestlist[0]).place(height = 30, width = 200, x = 50, y = i*35 + 175)
                                    ttk.Label(root2, text= guestlist[1]).place(height = 30, width = 200, x = 250, y = i*35 + 175)
                                    ttk.Label(root2, text= guestlist[2]).place(height = 30, width = 150, x = 450, y = i*35 + 175)
                                    guestIDlist.append(guestlist[2])
                                    ttk.Button(root2, text = "Yes", command = yes).place(height = 30, width = 45, x = 600, y = i*35 + 175)
                                    ttk.Button(root2, text = "No", command = addguest).place(height = 30, width = 45, x = 650, y = i*35 + 175)
                                i -= 1
            
                        else:
                            query = "SELECT guestFirstName, guestLastName, guestID FROM guest WHERE (guestFirstName = ? AND guestLastName = ?)"
                            guests = db.read_table_2condition(db.create_connection(db.data), query, listguest[0], listguest[1])
                            j = 0
                            length = (len(guests))
                            if (length == 0):
                                ttk.Label(root2).place(height = 370, width = 700, x = 0, y = i*35 + 175)
                                ttk.Button(root2, text= "Add New Guest?", command = addguest).place(height = 30, width = 600, x = 50, y = i*35 + 175)
                            if (length > 0):
                                ttk.Label(root2, width=80, text= "First name").place(height = 30, width = 200, x = 50, y = i*35 + 175)
                                ttk.Label(root2, width=80, text= "Last name").place(height = 30, width = 200, x = 250, y = i*35 + 175)
                                ttk.Label(root2, width=80, text= "Guest ID").place(height = 30, width = 200, x = 450, y = i*35 + 175)
                                ttk.Label(root2, width=80, text= "Guest?").place(height = 30, width = 200, x = 600, y = i*35 + 175)
                                
                                for row in guests:
                                    j += 1
                                    i += 1
                                    guestlist = list(row)
                                    ttk.Label(root2, text = (str(j) + ".")).place(height = 30, width = 40, x = 10, y = i*35 + 175)
                                    ttk.Label(root2, text= guestlist[0]).place(height = 30, width = 200, x = 50, y = i*35 + 175)
                                    ttk.Label(root2, text= guestlist[1]).place(height = 30, width = 200, x = 250, y = i*35 + 175)
                                    ttk.Label(root2, text= guestlist[2]).place(height = 30, width = 150, x = 450, y = i*35 + 175)
                                    ttk.Button(root2, text = "Yes", command = yes).place(height = 30, width = 45, x = 600, y = i*35 + 175)
                                    ttk.Button(root2, text = "No", command = addguest).place(height = 30, width = 45, x = 650, y = i*35 + 175)
                                    guestIDlist.append(guestlist[2])
                                i -= 1
            
                    global i
                    global y
                    global memberID
                    memberID = 0
                    for m in range(0, len(memberIDlist)):
                        if (y <= (135 + (m*35)) and y >= (105 + (m*35))):
                            memberID = memberIDlist[m]       
                       
                    ttk.Label(root2, text = "How many guests?", font = ("Ariel", 16)).place(height = 30, width = 200, x = 50, y = (i*35 + 105))
                    ttk.Button(root2, text = "1", command = one).place(height = 30, width = 100, x = 250, y = (i*35 + 105))
                    ttk.Button(root2, text = "2", command = two).place(height = 30, width = 100, x = 375, y = (i*35 + 105))
                    
        
                global i
                global memberIDlist
                global x
                global y
                global memberID
                memberID = 0
                memberIDlist = []
                i = 0 
                root2.bind('<Button-1>', motion)
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
                        memberIDlist.append(rowlist[2])
                
            
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
            def searchmemberID():
                def teammember():
                    global membertype
                    membertype = "Team member"
                def month():
                    global membertype
                    membertype = "Month-to-Month"
                def year():
                    global membertype
                    membertype = "Year Long"
                def addmember():
                    global membertype
                    print(membertype)
                    memberfirstfixed = newMemberFirst.get()
                    memberfirstfixed = memberfirstfixed.strip()
                    memberlastfixed = newMemberLast.get()
                    memberlastfixed = memberlastfixed.strip()
                    memberemailfixed = newMemberEmail.get()
                    memberemailfixed = memberemailfixed.strip()
                    memberIDsfixed = newMemberID.get()
                    memberIDsfixed = int(memberIDsfixed.strip())
                    memberphonefixed = (newMemberPhone.get())
                    memberphonefixed = memberphonefixed.strip()
                    memberphonefixed = memberphonefixed.replace("(", "")
                    memberphonefixed = memberphonefixed.replace(")", "-")
                    memberphonefixed = memberphonefixed.replace(".", "-")
                    if (len(memberphonefixed) == 10): 
                        memberphonefixed = (memberphonefixed[0:3] + "-" + memberphonefixed[3:6] + "-" + memberphonefixed[6:10])
                    elif (len(memberphonefixed) == 11):
                        memberphonefixed = (memberphonefixed[0:7] + "-" + memberphonefixed[7:11])
                    
                    memberbirthdatefixed = newMemberDOB.get()
                    memberbirthdatefixed = memberbirthdatefixed.strip()
                    memberbirthdatefixed = memberbirthdatefixed.replace("-","/")
                    
                    query2 = "INSERT INTO member VALUES (?,?,?,?,?,?,?,?)"
                    db.insertguest(db.create_connection(db.data), query2, memberIDsfixed, memberfirstfixed, memberlastfixed, memberemailfixed, memberphonefixed, membertype, memberbirthdatefixed, calculate_year(memberbirthdatefixed))
                    ttk.Label(root3).place(height = 85, width = 700, x = 0, y = 315)
                    ttk.Label(root3, text = "Member Added", font = ("Ariel", 15)).place(height = 30, width = 300, x = 250, y = 315)
                    
                
                memberIDfixed = memberIDentry.get()
                memberIDfixed = int(memberIDfixed.strip())
                
                query = "SELECT memberID FROM member WHERE memberID = ?"
                members = db.read_table_1condition(db.create_connection(db.data), query, (memberIDfixed,))
                system = 0 
                if (len(members) ==  0):
                    system += 1
                
                if (system == 0): 
                    ttk.Label(root3, text = "Member already exists in system...", font = ("Ariel", 15)).place(height = 40, width = 400, x = 200, y = 70)
                
                elif (system == 1):
                    ttk.Label(root3).place(height = 330, width = 700, x = 0, y = 70)
                    ttk.Label(root3, text="Member First Name:").place(height = 30, width = 200, x = 10, y = 70)
                    newMemberFirst = tk.StringVar()
                    ttk.Entry(root3, width=40, textvariable=newMemberFirst).place(height = 30, width = 300, x = 220, y = 70)   
         
                    ttk.Label(root3, text="Member Last Name:").place(height = 30, width = 200, x = 10, y = 105)
                    newMemberLast = tk.StringVar()
                    ttk.Entry(root3, width=40, textvariable=newMemberLast).place(height = 30, width = 300, x = 220, y = 105)   
            
                    ttk.Label(root3, text="Membership ID:").place(height = 30, width = 200, x = 10, y = 140)
                    newMemberID = tk.StringVar()
                    ttk.Entry(root3, textvariable = newMemberID).place(height = 30, width = 300, x = 220, y = 140)
         
                    ttk.Label(root3, text="Membership Type:").place(height = 30, width = 200, x = 10, y = 175)
                    ttk.Button(root3, text="Month-to-Month", command = month).place(height = 30, width = 120, x = 220, y = 175)
                    ttk.Button(root3, text="Year Long", command = year).place(height = 30, width = 120, x = 350, y = 175)
                    ttk.Button(root3, text="Team Member", command = teammember).place(height = 30, width = 120, x = 480, y = 175)  
         
                    ttk.Label(root3, text="Phone:").place(height = 30, width = 200, x = 10, y = 210)
                    newMemberPhone = tk.StringVar()
                    ttk.Entry(root3, width=40, textvariable=newMemberPhone).place(height = 30, width = 300, x = 220, y = 210)  
                    
                    ttk.Label(root3, text = "Email:").place(height = 30, width = 200, x = 10, y = 245) 
                    newMemberEmail = tk.StringVar()
                    ttk.Entry(root3, textvariable = newMemberEmail).place(height = 30, width = 300, x = 220, y = 245)
            
                    ttk.Label(root3, text="Date of Birth:").place(height = 30, width = 200, x = 10, y = 280)
                    newMemberDOB = tk.StringVar()
                    ttk.Entry(root3, width=40, textvariable=newMemberDOB).place(height = 30, width = 300, x = 220, y = 280)   
         
                    ttk.Button(root3, text = "Add Member", command = addmember).place(height = 30, width = 500, x = 100, y = 315)
            
            
            def backtomain():
                root3.destroy()
                screendesign()
            root.destroy()
            root3 = tk.Tk()
            root3.title("Add Member")
            root3.geometry("700x400")   
            
            ttk.Button(root3, text = "Exit Program", command = root3.destroy).place(height = 30, width = 100, x = 10, y = 0)
            ttk.Button(root3, text = "Back to Menu", command = backtomain).place(height = 30, width = 100, x = 590, y = 0)
            ttk.Label(root3, text = "Add Member", font=("Ariel", 18)).place(height= 30, width = 300, x = 265, y = 0)
            ttk.Label(root3, text="Member ID:", font = ("Ariel", 15)).place(height = 30, width = 150, x = 10, y = 35)
            
            memberIDentry = tk.StringVar()
            ttk.Entry(root3, textvariable = memberIDentry).place(height = 30, width = 400, x = 160, y = 35)
            ttk.Button(root3, text = "Search", command = searchmemberID).place(height = 30, width = 100, x = 580, y = 35 )
            
            
        def screen4():
            def listall():
                global i 
                i = 0 
                guestID = ttk.Label(canvas, text = "Guest ID:")
                canvas.create_window(35, 155, width = 70, height = 30, window = guestID)
                guestfirstname = ttk.Label(canvas, text = "First Name:")
                canvas.create_window(105, 155, width = 80, height = 30, window = guestfirstname) 
                guestlastname = ttk.Label(canvas, text = "Last Name:")
                canvas.create_window(210, 155, width = 80, height = 30, window = guestlastname) 
                guestemail = ttk.Label(canvas, text = "Email:")
                canvas.create_window(290, 155, width = 200, height = 30, window = guestemail) 
                guestphone = ttk.Label(canvas, text = "Phone:")
                canvas.create_window(490, 155, width = 100, height = 30, window = guestphone) 
                guestbirthdate = ttk.Label(canvas, text = "Birthdate:")
                canvas.create_window(590, 155, width = 80, height = 30, window = guestbirthdate) 
                guestage = ttk.Label(canvas, text = "Age:")
                canvas.create_window(670, 155, width = 60, height = 30, window = guestage)  
                query = "SELECT * FROM guest"
                allguest = db.read_table(db.create_connection(db.data), query)
                for guest in allguest:
                    i += 1
                    list(guest)
                    guestIDlabel= ttk.Label(canvas, text = guest[0])
                    canvas.create_window(60, 155 + i*35, width = 100, height = 30, window = guestIDlabel) 
                    guestfirstnamelabel= ttk.Label(canvas, text = guest[2])
                    canvas.create_window(130, 155+ i*35, width = 100, height = 30, window = guestfirstnamelabel) 
                    guestlastnamelabel= ttk.Label(canvas, text = guest[3])
                    canvas.create_window(230, 155+ i*35, width = 100, height = 30, window = guestlastnamelabel) 
                    guestemaillabel= ttk.Label(canvas, text = guest[4])
                    canvas.create_window(330, 155+ i*35, width = 100, height = 30, window = guestemaillabel) 
                    guestphonelabel= ttk.Label(canvas, text = guest[5])
                    canvas.create_window(460, 155+ i*35, width = 100, height = 30, window = guestphonelabel) 
                    guestbirthdatelabel= ttk.Label(canvas, text = guest[6])
                    canvas.create_window(560, 155+ i*35, width = 100, height = 30, window = guestbirthdatelabel) 
                    guestagelabel= ttk.Label(canvas, text = guest[7])
                    canvas.create_window(660, 155+ i*35, width = 50, height = 30, window = guestagelabel) 
            def backtomain():
                root4.destroy()
                screendesign()
            root.destroy()
            root4 = tk.Tk()
            root4.title("Guest List")
            root4.geometry("700x400")
            frame=tk.Frame(root4,width=700,height=1000)
            frame.pack(expand=True, fill=tk.BOTH)
            canvas=tk.Canvas(frame,width=700,height=3000,scrollregion=(0,70,700,3000))
            vbar=tk.Scrollbar(canvas,orient=tk.VERTICAL)
            vbar.pack(side=tk.RIGHT,fill=tk.Y)
            ttk.Label(root4).place(height= 70, width = 680, x = 0, y = 0)
            ttk.Label(root4, text = "Guest List", font=("Ariel", 18)).place(height= 30, width = 300, x = 290, y = 0)
            ttk.Button(root4, text = "Exit Program", command = root4.destroy).place(height = 30, width = 100, x = 10, y = 0)
            ttk.Button(root4, text = "Back to Menu", command = backtomain).place(height = 30, width = 100, x = 580, y = 0)
            ttk.Label(root4, text = "Enter Guest Name:", font = ("Ariel",14)).place(height = 30, width = 180, x = 10, y = 35)
            guestname = tk.StringVar()
            ttk.Entry(root4, textvariable = guestname).place(height = 30, width = 270, x = 190, y = 35)
            ttk.Button(root4, text = "List All Guests", command = listall).place(height = 30, width = 100, x = 580, y = 35)
            ttk.Button(root4, text = "Search").place(height = 30, width = 100, x = 470, y = 35)
            
            vbar.config(command=canvas.yview)
            canvas.config(yscrollcommand=vbar.set)
            canvas.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
            root4.mainloop()

                
        def screen5():
            def motion(event):
                global x
                global y
                x = root5.winfo_pointerx() - root5.winfo_rootx()
                y = root5.winfo_pointery() - root5.winfo_rooty()
            def backtomain():
                root5.destroy()
                screendesign()
            
            def searchdate():
                def expand():
                    global i 
                    global y
                    global uniqueIDs
                    global start
                    global end
                    global currentmemberID
                    currentmemberID = 0
                    g = 0
                    print(g)
                    click = 0
                    while (click < (len(uniqueIDs))):
                        if (y <= (135 + (g*35)) and y >= (105 + (g*35))):
                            currentmemberID = uniqueIDs[click]    
                            break
                        click += 1
                        g += 1
                    initiallabel = ttk.Label(canvas)
                    canvas.create_window(340, 340 + g*35, height = 400, width = 680,window = initiallabel)
                    query = "SELECT * FROM visits WHERE memberID = ?"
                    allguests = db.read_table_1condition(db.create_connection(db.data), query, (currentmemberID,))
                    print(allguests)
                    gfirst = ttk.Label(canvas, text = "Guest First Name")
                    canvas.create_window(162, 140 + g*35, height = 30, width = 125, window = gfirst)
                    glast = ttk.Label(canvas, text = "Guest Last Name")
                    canvas.create_window(287, 140 + g*35, height = 30, width = 125, window = glast)
                    gbirth = ttk.Label(canvas, text= "Guest Birth Date")
                    canvas.create_window(412, 140 + g*35, height = 30, width = 125, window = gbirth)
                    gage = ttk.Label(canvas, text= "Guest Age")
                    canvas.create_window(525, 140 + g*35, height = 30, width = 100, window = gage)
                    gdate = ttk.Label(canvas, text= "Visit Date")
                    canvas.create_window(627, 140 + g*35, height = 30, width = 105, window = gdate)
                    
                    for guest in allguests:
                        g += 1
                        guestlist = list(guest)
                        print(guestlist)
                        if (calculate_date(guestlist[8]) > calculate_date(start) and calculate_date(guestlist[8]) < calculate_date(end)): 
                            gfirstlabel = ttk.Label(canvas, text = guestlist[2])
                            canvas.create_window(162, 225 + g*35, height = 30, width = 125, window = gfirstlabel)
                            glastlabel = ttk.Label(canvas, text = guestlist[3])
                            canvas.create_window(287, 225 + g*35, height = 30, width = 125, window = glastlabel)
                            gbirthlabel = ttk.Label(canvas, text = guestlist[6])
                            canvas.create_window(412, 225 + g*35, height = 30, width = 125, window = gbirthlabel)
                            gagelabel = ttk.Label(canvas, text = guestlist[7])
                            canvas.create_window(525, 225 + g*35, height = 30, width = 100, window = gagelabel)
                            gvisitdatelabel = ttk.Label(canvas, text = guestlist[8])
                            canvas.create_window(627, 225 + g*35, height = 30, width = 105, window = gvisitdatelabel)
                    
                            
                    
                global currentmonth
                global currentyear
                global todaymonth
                global todayyear
                global i
                global uniqueIDs
                global y
                global start
                global end
                y = 0
                root5.bind('<Button-1>', motion)
                i = 0
                initiallabel2 = ttk.Label(canvas) 
                canvas.create_window(0, 140, height = 340, width = 680, window = initiallabel2)
                today()
                query = 'SELECT * FROM visits'
                rows = db.read_table(db.create_connection(db.data), query)
                memberIDs = []
                mfirstlabel = ttk.Label(canvas, text = "First Name")
                canvas.create_window(10, 140, height = 30, width = 130, window = mfirstlabel)
                mlastlabel = ttk.Label(canvas, text = "Last Name")
                canvas.create_window(140, 140, height = 30, width = 130, window = mlastlabel)
                mpasses_ulabel = ttk.Label(canvas, text = "Passes used during period")
                canvas.create_window(270, 140, height = 30, width = 210, window = mpasses_ulabel)
                mpasses_rlabel = ttk.Label(canvas, text = "Passes remaining this month")
                canvas.create_window(480, 140, height = 30, width = 200, window = mpasses_rlabel)
                start = StartDate.get()
                start = start.strip()
                end = EndDate.get()
                end = end.strip()
                for r in rows:
                    if (calculate_date(r[8]) > calculate_date(start) and calculate_date(r[8]) < calculate_date(end)): 
                        memberid = list(r)
                        memberIDs.append(memberid[1])
                memberIDs = sorted(memberIDs)
                uniqueIDs = []
                uniqueIDs.append(memberIDs[0])
                
                for m in range(1, len(memberIDs)):
                    if (memberIDs[m - 1] != memberIDs[m]):
                        uniqueIDs.append(memberIDs[m])
                
                visitsinperiod = []
                
                for k in range(0, len(uniqueIDs)):
                    visit = 0
                    currentID = uniqueIDs[k]
                    for j in range(0, len(memberIDs)):
                        if (memberIDs[j] == currentID):
                            visit += 1
                    visitsinperiod.append(visit)
                
                for u in range(0, len(uniqueIDs)):
                    visits = 0
                    query2 = "SELECT memberFirstName, memberLastName FROM member WHERE memberID = ?"
                    columns = db.read_table_1condition(db.create_connection(db.data), query2, (uniqueIDs[u],))
                    for c in columns:
                        i += 1
                        col = list(c)
                        memberF = ttk.Label(canvas, text = str(col[0]))
                        canvas.create_window(10, (140 + i*35), height = 30, width = 130, window = memberF)
                        memberL = ttk.Label(canvas, text = str(col[1]))
                        canvas.create_window(140, (140 + i*35), height = 30, width = 130, window = memberL)
                        memberI = ttk.Label(canvas, text = str(visitsinperiod[u]))
                        canvas.create_window(270, (140 + i*35), height = 30, width = 20, window = memberI)
                        memberexpand = ttk.Button(canvas, text = "Expand", command = expand)
                        canvas.create_window(310, (140 + i*35), height = 30, width = 100, window =memberexpand)
                        query = "SELECT visitDate FROM visits WHERE memberID = ?"
                        rows = db.read_table_1condition(db.create_connection(db.data), query, (uniqueIDs[u],))
                        for row in rows:
                            datelist = list(row)
                            calculate_monthyear(datelist[0])
                            if (currentmonth == todaymonth and currentyear == todayyear):
                                visits += 1
                                
                            remaining = (2 - (visits))
                            memberrem = ttk.Label(canvas, text = str(remaining))
                            canvas.create_window(550, (140 + i*35), height = 30, width = 120, window = memberrem)
                
            root.destroy()
            root5 = tk.Tk()
            root5.title("Member Pass Records")
            root5.geometry("700x400")
            frame=tk.Frame(root5,width=700,height=1000)
            frame.pack(expand=True, fill=tk.BOTH)
            canvas=tk.Canvas(frame,width=700,height=3000,scrollregion=(0,70,700,3000))
            vbar=tk.Scrollbar(canvas,orient=tk.VERTICAL)
            vbar.pack(side=tk.RIGHT,fill=tk.Y)
            vbar.config(command=canvas.yview)
            ttk.Label(root5).place(height= 70, width = 680, x = 0, y = 0)
            ttk.Label(root5, text = "Member Pass Records", font=("Ariel", 18)).place(height= 30, width = 300, x = 240, y = 0)
            ttk.Button(root5, text = "Exit Program", command = root5.destroy).place(height = 30, width = 100, x = 10, y = 0)
            ttk.Button(root5, text = "Back to Menu", command = backtomain).place(height = 30, width = 100, x = 580, y = 0)
            ttk.Label(root5, text = "Records from:", font = ("Ariel", 16)).place(height = 30, width = 150, x = 10, y = 35)
            ttk.Label(root5, text = "Start Date:").place(height = 30, width = 70, x = 160, y = 35)
            ttk.Label(root5, text = "End Date:").place(height = 30, width = 70, x = 350, y = 35)
            StartDate = tk.StringVar()
            EndDate = tk.StringVar()
            ttk.Entry(root5, textvariable = StartDate).place(height = 30, width = 100, x = 230, y = 35)
            ttk.Entry(root5, textvariable = EndDate).place(height = 30, width = 100, x = 420, y = 35)
            ttk.Button(root5, text = "Search", command = searchdate).place(height = 30, width = 140, x = 540, y = 35)
            vbar.config(command=canvas.yview)
            canvas.config(yscrollcommand=vbar.set)
            canvas.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)
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
