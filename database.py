# Final-Project-Database

# import modules for code, as well as establish where the database will be stored
import sqlite3 
from sqlite3 import Error
from datetime import date 

data = "conquer.sqlite"

# the function we will use to calculate the member's and guest's age
def calculate_year(birthDate): 
    if (birthDate == None): return None
    birthDate = birthDate.replace("/"," ")
    birthDate = birthDate.split()
    birthDate = date(int(birthDate[2]),int(birthDate[0]),int(birthDate[1]))
    today = date.today() 
    years = today.year - birthDate.year
    if ((today.month, today.day) < (birthDate.month, birthDate.day)):
        years = years - 1
        
    return years
 
# the lists in which we will hold all the data for each member
# this establishes a baseline for member records, making sure they can be recovered from 4/23/2020
MemberID = [100008053,100008584,100008405,100005596,100006959,100006960,100000033,100000688,100000689,100000553,100000552,100009007,100009948,100005576,100007960,100007961,100007814,100007813,100008302,100000176,100005074,100009520,100006969,100009455,100008093,100009446,100008091,100008092,100007188,100009287,100007946,100010126,100008783,100010283,100003081,100001779,100003874,100003809,100009532,100008623,100000247,100009586,100009916,100003872,100003871,100007252,100009252,100006741,100004605,100010215,100003815,100003100,100009581,100005171,100005351,100009510,100007947,100009713,100009736,100010150,100006683,100006684,100006685,100005488,100006657,100006658,100008128,100002486,100002240,100002239,100000834,100000837,100008273,100008351,100004300,100004299,100003254,100007437,100005730,100004887,100004019,100004020,100004105,100005352,100002578,100001040,100007963,100008033,100007899,100010242,100005848,100005000,100009738,100006800,100005767,100008795,100004686,100007066,100000713,100007299,100004999,100000165,100004045,100007010,100008916,100001778,100002865,100002229,100000246,100005330,100009528,100010117,100000130,100005169,100005170,100000200,100005846,100009293,100008417,100000444,100000177,100003253,100004445,100001290,100005819,100001039]
MemberFirst = ["Hana","Allison","Andrea","Isabella","Ben","Leo","Steve","Jaxon","Teddy","Kaylee","Nathan","Jaxon","Lucas","Nathaniel","Eman","Mariam","Faith","Nicole","Micah","Jack","Ryne","Genevieve","Liam","Willam","Cody","Elliana","Dominik","Jocelyn","Jessica","Sarah","Tyler","Levi","Noah","Mark","Ashley","Blake","Max","Asmara","Owen","Lucy","Jacob","Julia","Lucas","Ashton","Austin","Marta","Kassidy","Daniel","Zach","Macleod","Nick","Kari","Evan","Caleb","Daizie","Vincent","Jack","Danielle","Ethan","Yazzn","Brittany","Jackson","Jayden","Tony","Araeya","Hannah","Cassidy","Connor","Maliya","Michelle","Elliot","Graham","Evelyn","Wesley","Joelle","Miles","Darwin","Matthew","Ben","Zane","Max","Sam","Fiona","Calvin","Kiki","Sydney","Amin","Inam","Nazeeha","Angie","Jaden","Brandon","Charlotte","Lincoln","Amory","Rylan","Chase","Jake","Laura","Alexis","Wendy","Addison","Ty","Clara","Rebekah","Joshua","Matthew","Steve","Elizabeth","Elizabeth","Elaina","Joseph","Tyler","Andrew","Isaac","Sean","James","Zac","Jessica","Collin","Matt","Alexander","Lisa","James","Wessels","Ryan"]
MemberLast = ["Aboubaker","Anderson","Apostolou","Bergeson","Bilger","Bilger","Calabrese","Cooke","Cooke","Curwirk","Curwick","Davis-Gries","Diffley","Engstrom","Faisal","Faisal","Fisher","Fisher","Folman","Froslee","Grosbier","Haas","Hagen","Harris","Harrison","Harty","Hawks","Hawks","Hegenbarth","Hill","Hursh","Inwards","Jacklitch","Janssen","Jensen","Johnson","Kinney","Kiros","Larson","Lawrence","Levinshteyn","Lima","Lima","Mattson","Mattson","Mccoy","Miller","Montalvan","Mooney","Nathan","Nelson","Nokken","Ollestad","Peltier","Peterson","Porter","Riley","Risty","Risty","Salem","Schultz","Schultz","Schultz","Sedesky","Sell","Sell","Seymour","Sherzer","Slotto","Slotto","Stevens","Stevens","Stusynski","Stusynski","Taylor","Taylor","Tennis","Theis","Tombers","Vanguilder","Von Wald","Von Wald","Wahlgren","Wessels","Wielinski","Wirrer","Yousuf","Yousuf","Yousuf","Zurek","Avelsgard","Benshoof","Blansette","Bolitho","Braddock","Ceronsky","Dallmann","Dotte","Erickson","Fiksen","Frantz","Granlund","Guell","Haas","Hevern","Johnson","Krueger","Kuester","Levinshteyn","Nelson","Newcomer","Orrey","Orrey","Peltier","Peltier","Sardeson","Scott","Siegle","Slater","Stout","Ten Napel","Tennis","Vague","Wallek","Wessels","Wirrer"]
MemberEmail = ["aboubaker.aboubaker@yahoo.com",None,"lapostolou23@gmail.com","randygunderson@hotmail.com",None,None,"randygunderson@hotmail.com",None,None,"curwickfamily@gmail.com","curwickfamily@gmail.com","Kgries7@gmail.com","bethdiffley@gmail.com","nathaniel.engstrom@gmail.com",None,None,None,"patnode09@gmail.com","micah.folman@yahoo.com","vfroslee@msn.com","chadgrosbie@gmail.com",None,"eeide3@msn.com","harrisnish@yahoo.com",None,None,"jennyw03@hotmail.com","jennyw03@hotmail.com","JHeg21@gmail.com","saajhill2@comcast.net",None,None,None,"mjdragonexpert23@gmail.com","atjensen11@msn.com","jjohnson98@gmail.com","kinneyjen@hotmail.com","bkiros@gmail.com",None,"senatorwu@hotmail.com","peter.levinshteyn@gmail.com",None,"sig_joao@Hotmail.com","james_a_mattson@yahoo.com","james_a_mattson@yahoo.com","karenhoff@hotmail.com","dymand31@gmail.com",None,"michael_c_mooney@hotmail.com","nathanmacleod2010@gmail.com",None,"eknokken@comcast.net",None,None,"missy4kids@icloud.com",None,"djriley007@gmail.com",None,"jristy08@yahoo.com","ozoz2012@yahoo.com","britanykaye@yahoo.com","britanykaye@yahoo.com","britanykaye@yahoo.com","Notthedirtyredhead@hotmail.com",None,None,"penny.seymour@comcast.net","rickandalison@gmail.com","slotto43@yahoo.com","slotto43@yahoo.com","brian.stevens@greatclips.net","brianjosephstevens@yahoo.com",None,None,"richellerealty612@gmail.com","richellerealty612@gmail.com","jacobandsaleen@hotmail.com","jennlou415@yahoo.com","davetombers@icloud.com","wkvanguilder@comcast.net","vonwaldjean@comcast.net","vonwaldjean@comcast.net","heyladym@yahoo.com","Stripedtiger07@gmail.com","davewielinski@yahoo.com","bcwirrer@comcast.net","yous0050@gmail.com",None,None,"angzurek30@gmail.com",None,"b.benshoof@gmail.com",None,"tstephan23@hotmail.com","gaelbraddock@gmail.com",None,"chasedallmann01@gmail.com","jakedotte@msn.com","kmklerickson@comcast.net","running96@hotmail.com","wendy.frantz@gmail.com","christa.granlund@gmail.com",None,"clara_haas@icloud.com","jenniferhevern@gmail.com","jjohnson98@gmail.com",None,"sjsak2@yahoo.com","elizabethlevinshteyn@gmail.com","loudharpo@hotmail.com","michele_leigh@msn.com","jorrey22@yahoo.com","orreym@yahoo.com","pelt0070@umn.edu",None,"seansardeson@frontier.co",None,"kristen.siegle@gmail.com","jslater8245@gmail.com","murphstout@yahoo.com","matttn65@yahoo.com","jacobandsaleen@hotmail.com","vaguelisa@gmail.com","kathywallek@comcast.net",None,"bcwirrer@comcast.net"]
MemberPhone = ["612-618-7731","234-804-6679","763-913-2417","763-245-0672",None,None,"763-439-4510","612-306-1378","612-306-1378","763-792-2320","763-792-2320","952-412-8582",None,"651-485-0377","763-354-0151",None,"651-485-7833","651-485-7833","651-246-9922","763-458-3283","763-412-9715","651-343-9602","612-306-8153","612-817-2869",None,None,"612-367-9083","612-367-9083","763-516-7053","612-280-8504","612-254-5838",None,None,"763-843-5141","763-783-5646","763-229-0297",None,"612-616-4847","612-400-5925","612-280-2313",None,None,"651-335-0535",None,None,"763-843-7803","612-282-5309","763-203-5103","612-804-9117","218-791-5139",None,"763-205-6179","612-598-5776","952-465-9372","651-356-2608",None,"651-373-2420","612-790-0774",None,"612-345-0606","651-295-9473","651-295-9473","651-295-9473","612-723-4118","763-226-0752","763-226-0752","763-300-6952","763-607-3860","612-749-4290","612-749-4290","612-210-9427",None,None,"612-749-9792","612-964-0143","612-964-0143",None,"651-470-1930","763-567-8750",None,"651-271-5520",None,"651-492-6375","651-485-3658","651-765-8432","651-490-3132","763-744-7960",None,None,"612-281-9182",None,None,"763-218-2655","612-210-9021","763-607-7941","651-357-6254","651-246-1878","651-354-9198","763-780-1867",None,"763-242-9643","763-226-6549","702-701-1952","763-389-5183","763-862-3482","763-229-0297","507-459-0320","651-271-1336",None,"763-244-4904","763-742-3042","612-414-4809","763-390-0997","952-465-9372","952-465-9372",None,None,None,"425-299-8425","612-414-1896","952-220-0463","651-728-1731","651-335-8929","651-341-6694",None,"651-490-3132"]
MembershipType = []

#this adds that a membership is month-to-month or year-long;
#only applies to the existing records, new records are much easier to add
for i in range(0,90):
    if ((i == 4) or (i == 5) or (i == 9) or (i == 12) or (i == 21) or (i == 25) or (i == 30) or (i == 38) or (i == 41) or (i == 42) or (i == 49) or (i == 52) or (i == 55) or (i == 60) or (i == 66) or (i == 67) or (i == 70) or (i == 71) or (i == 89)):
        MembershipType.append("Month-to-Month")
    else:
        MembershipType.append("Year Long")

#adds a different type of membership type to a few existing records
for i in range(90,len(MemberID)):
    MembershipType.append("Team member")
  
MemberBirthDate = ["10/01/1984","09/06/2012","04/18/2010","09/23/2007","12/27/2011","07/23/2009","04/28/1990","03/01/2012","06/14/2013","06/10/2012","12/03/2010","07/19/2010",None,"07/01/2003","07/03/2009","04/01/2012","01/03/2013","05/06/1981",None,"02/07/2007","03/26/2011","11/04/2009","12/08/2010",None,"06/07/1999",None,"03/25/2010","12/02/2011","05/22/1987","06/09/1975","12/05/2004",None,"11/25/2007","05/20/1987",None,"08/12/2010","09/10/2006","06/22/2011",None,"06/28/2012","01/29/2010",None,"12/01/2014","01/12/2007","01/12/2007","04/29/2009","10/28/2008","03/26/2008","12/30/2009",None,"03/10/2001","06/28/1975",None,"06/25/2011","03/31/2011","08/09/2004",None,None,"12/25/2013",None,"09/21/1986","02/25/2008","10/13/2005","10/23/2006","12/02/2008","05/31/2011","06/24/2007","04/05/2011","04/27/2012","02/11/1982","07/14/2009","07/07/2011","06/07/2010","01/18/2014","08/31/2009","09/02/2011","03/23/2011","01/23/2012","09/25/2007","06/01/2007","09/05/2008","09/05/2008","12/29/2003","08/03/1989","04/12/2007","03/01/2005",None,"06/03/2012","07/10/2010",None,None,None,"03/30/2011","05/07/2011","03/22/2010",None,"04/23/1992","10/02/1998","01/20/2003","01/26/2010","11/15/1969","08/27/2008",None,"09/08/2007","12/26/2010","01/20/1980","07/05/2004","12/17/1974","03/02/2007","11/07/1989",None,"03/20/1975",None,"01/02/1981","10/09/2009","10/13/2001",None,"04/03/2011","02/11/1995","10/19/2004","04/17/1977","05/01/2009","09/02/1963","04/17/2008","03/07/1995","04/13/2008"]


#creates a connection to the database for the data to be stored
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn
 
 
#creates a new table in sql
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#creates a select all from table function
def read_table_1condition(conn, query, condition1):
    try:
        c = conn.cursor()
        c.execute(query, condition1)
        rows = c.fetchall()
        return rows
            
    except Error as e:
        print(e)

def read_table(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        print(rows)
        return rows
            
    except Error as e:
        print(e)
        
def read_table_2condition(conn, query, condition1, condition2):
    try:
        c = conn.cursor() 
        c.execute(query, (condition1, condition2))
        rows = c.fetchall()
        return rows
            
    except Error as e:
        print(e)
        
#creates a function that allows a guest to be added using the program
def insertguest(conn, query, condition1, condition2, condition3, condition4, condition5, condition6, condition7, condition8):
    try:
        c = conn.cursor() 
        c.execute(query, (condition1, condition2, condition3, condition4, condition5, condition6, condition7, condition8))
        conn.commit()
            
    except Error as e:
        print(e)

#creates a function that allows a member to be added using the program
def insertmember(conn, query, condition1, condition2, condition3, condition4, condition5, condition6):
    try:
        c = conn.cursor() 
        c.execute(query, (condition1, condition2, condition3, condition4, condition5, condition6))
        conn.commit()
            
    except Error as e:
        print(e)

#creates a function that allows the # of visits to be added using the program
def insertvisits(conn, query, condition1, condition2, condition3, condition4, condition5, condition6, condition7, condition8, condition9):
    try:
        c = conn.cursor() 
        c.execute(query, (condition1, condition2, condition3, condition4, condition5, condition6, condition7, condition8, condition9))
        conn.commit()
            
    except Error as e:
        print(e)

def main():
    global data
    # creates the actual tables which data will be stored in
    sql_create_member_table = """ CREATE TABLE IF NOT EXISTS member (
                                        memberID INTEGER PRIMARY KEY,
                                        memberFirstName VARCHAR(20) NOT NULL,
                                        memberLastName VARCHAR(30) NOT NULL,
                                        memberEmail VARCHAR(50),
                                        memberPhone VARCHAR(12),
                                        membershipType VARCHAR(20) NOT NULL,
                                        memberBirthDate date,
                                        memberAge INTEGER 
                                    ); """
 
    sql_create_guest_table = """CREATE TABLE IF NOT EXISTS guest (
                                    guestID INTEGER PRIMARY KEY,
                                    memberID INTEGER NOT NULL,
                                    guestFirstName VARCHAR(20) NOT NULL,
                                    guestLastName VARCHAR(30) NOT NULL,
                                    guestEmail VARCHAR(50),
                                    guestPhone VARCHAR(12),
                                    guestBirthDate date,
                                    guestAge INTEGER,
                                    FOREIGN KEY (memberID) REFERENCES member (memberID)
                                ); """
                                
    sql_create_visits_table = """CREATE TABLE IF NOT EXISTS visits (
                                    guestID INTEGER,
                                    memberID INTEGER,
                                    guestFirstName VARCHAR(20) NOT NULL,
                                    guestLastName VARCHAR(30) NOT NULL,
                                    guestEmail VARCHAR(50),
                                    guestPhone VARCHAR(12),
                                    guestBirthDate date,
                                    guestAge INTEGER,
                                    visitDate date,
                                    FOREIGN KEY (memberID) REFERENCES member (memberID),
                                    FOREIGN KEY (guestID) REFERENCES guest (guestID)
                                ); """
                                    
    
    
    # create a database connection
    conn = create_connection(data)
    print(conn)
    # create tables
    if conn is not None:
        # create member table
        create_table(conn, sql_create_member_table)
        
        # create guest table
        create_table(conn, sql_create_guest_table)
        
        # create visits table
        create_table(conn, sql_create_visits_table)
        
        #inserts our values into this new table
        for i in range(0, len(MemberID)):
            if (MemberBirthDate[i] != 0): 
                insertguest(conn, "INSERT INTO member VALUES (?,?,?,?,?,?,?,?)", MemberID[i], MemberFirst[i], MemberLast[i], MemberEmail[i], MemberPhone[i], MembershipType[i], MemberBirthDate[i], calculate_year(MemberBirthDate[i]))
            else: 
                insertmember(conn, "INSERT INTO member (memberID, memberFirstName, memberLastName, memberEmail, memberPhone, membershipType) VALUES (?,?,?,?,?,?)", MemberID[i], MemberFirst[i], MemberLast[i], MemberEmail[i], MemberPhone[i], MembershipType[i])
        conn.commit()
        c = conn.cursor()
        conn.close()
    else:
        print("Error! cannot create the database connection.")
    
if (__name__ == "__main__"):
    main()
