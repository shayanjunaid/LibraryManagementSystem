from tkinter import *
from tkinter import messagebox, ttk
from turtle import Screen
from pyodbc import *
from datetime import *

conn = connect('Driver={SQL Server};''Server=SLICKMACHINE;''Database=Library;''Trusted_connection=yes;')
query = conn.cursor()
BG_COLOR = "#E1ECC8"
BUTTON_COLOR = "#F7FFE5"
SECONDARY_COLOR = "#A0C49D"
FONT = ("Arial", 20, "bold")


def select():
    window = Tk()
    window.title("Select")
    window.resizable(FALSE, FALSE)
    window.config(padx=25, pady=25, bg=BG_COLOR)

    def gotologin():
        window.destroy()
        empLogin()

    def goUser():
        window.destroy()
        userCatalog()

    empPortal = Button()
    empPortal.config(width=20, height=10, highlightthickness=0, text="Employee Portal", bg=BUTTON_COLOR,
                     font=("Arial", 12, "bold"), command=gotologin)
    empPortal.grid(row=2, column=0)

    customerPortal = Button()
    customerPortal.config(width=20, height=10, highlightthickness=0, text="Customer Portal", bg=BUTTON_COLOR,
                          font=("Arial", 12, "bold"), command=goUser)
    customerPortal.grid(row=2, column=1)

    topText = Label()
    topText.config(text="Welcome to The Library", pady=20, bg=BG_COLOR, font=FONT)
    topText.grid(row=0, column=0, columnspan=2)
    window.mainloop()


def empLogin():
    def tryLogin():
        name = empName.get()
        password = empPass.get()
        response = query.execute(f"select dbo.[empLogin]('{name}', '{password}')").fetchone()
        if response[0] == 1:
            messagebox.showinfo(message="Success")
            window.destroy()
            empDashBoard()
        else:
            messagebox.showinfo(message="Failure")

    def goBack():
        window.destroy()
        select()

    window = Tk()
    window.title("Login")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    empName = Entry()
    empName.config(width=40, font=("Arial", 15, "normal"))
    empName.grid(column=1, row=1, columnspan=1)

    empPass = Entry()
    empPass.config(width=40, font=("Arial", 15, "normal"), show='*')
    empPass.grid(column=1, row=2, columnspan=1)

    nameLabel = Label()
    nameLabel.config(text="Name: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    nameLabel.grid(column=0, row=1)

    passwordLabel = Label()
    passwordLabel.config(text="Password: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    passwordLabel.grid(column=0, row=2)

    topText = Label()
    topText.config(text="Login", pady=20, bg=BG_COLOR, font=FONT)
    topText.grid(row=0, column=1)

    spacer = Label()
    spacer.config(pady=20, bg=BG_COLOR)
    spacer.grid(row=3, column=1)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=0, row=4)

    loginButton = Button()
    loginButton.config(bg=BUTTON_COLOR, width=10, pady=10, text="Login", command=tryLogin, font=("Arial", 10, "bold"))
    loginButton.grid(column=2, row=4)

    window.mainloop()


def empDashBoard():
    window = Tk()
    window.title("Dashboard")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    def goBack():
        window.destroy()
        select()

    def goCatalogue():
        window.destroy()
        empCatalogue()

    def Users():
        window.destroy()
        ManageUsers()

    def libCard():
        window.destroy()
        makeLibCard()

    def employees():
        window.destroy()
        manageEmp()

    def bookdonate():
        window.destroy()
        Donation()

    def issue():
        window.destroy()
        issueBook()

    def returnBook():
        window.destroy()
        bookReturn()

    topText = Label()
    topText.config(text="Library Management System", pady=20, bg=BG_COLOR, font=FONT)
    topText.grid(row=0, column=1, columnspan=3)

    bottomText = Label()
    bottomText.config(text="Having trouble? Contact DB Manager", pady=20, bg=BG_COLOR, font=("Arial", 8, "normal"))
    bottomText.grid(row=4, column=1, columnspan=3)

    catalogue = Button()
    catalogue.config(bg=BUTTON_COLOR, width=15, pady=25, text="Catalogue", font=("Arial", 12, "bold"),
                     command=goCatalogue)
    catalogue.grid(column=1, row=1)

    makeAccount = Button()
    makeAccount.config(bg=BUTTON_COLOR, width=15, pady=25, text="Manage Users", font=("Arial", 12, "bold"),
                       command=Users)
    makeAccount.grid(column=2, row=1)

    issueCard = Button()
    issueCard.config(bg=BUTTON_COLOR, width=15, pady=25, text="Issue Library card", font=("Arial", 12, "bold"),
                     command=libCard)
    issueCard.grid(column=3, row=1)

    issuebook = Button()
    issuebook.config(bg=BUTTON_COLOR, width=15, pady=25, text="Issue a Book", font=("Arial", 12, "bold"), command=issue)
    issuebook.grid(column=1, row=2)

    returnbook = Button()
    returnbook.config(bg=BUTTON_COLOR, width=15, pady=25, text="Return a Book", font=("Arial", 12, "bold"), command=returnBook)
    returnbook.grid(column=2, row=2)

    bookDonation = Button()
    bookDonation.config(bg=BUTTON_COLOR, width=15, pady=25, text="Book Donation", font=("Arial", 12, "bold"), command=bookdonate)
    bookDonation.grid(column=3, row=2)

    empManage = Button()
    empManage.config(bg=BUTTON_COLOR, width=15, pady=25, text="Manage Employees", font=("Arial", 12, "bold"),
                     command=employees)
    empManage.grid(column=1, row=3)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=1, row=5)

    window.mainloop()


def bookReturn():
    window = Tk()
    window.title("Returns")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    def goBack():
        window.destroy()
        empDashBoard()

    def renew():
        selected = trv.item(trv.focus())
        isbn = selected['values'][0]
        libcard = selected['values'][1]
        empid = selected['values'][2]
        issuedate = selected['values'][3]
        returndate = selected['values'][4]
        check = query.execute(f"select dbo.renew_check({isbn})").fetchone()
        ans = 0
        for row in check:
            ans = row
        if ans >0:
            messagebox.showinfo(message="Book is reserved for someone else, cannot be renewed at this time")
        else:
            query.execute(f"exec renew_book {isbn}, {libcard}, {empid}")
            query.execute("commit transaction")

    def retbook():
        selected = trv.item(trv.focus())
        isbn = selected['values'][0]
        libcard = selected['values'][1]
        empid = selected['values'][2]
        fineamount = fine.get()
        condtn = condition.get()

        query.execute(f"exec return_book {isbn}, {libcard}, {empid}, {fineamount}, {condtn}")
        query.execute("commit transaction")


    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=5)

    returnButton = Button()
    returnButton.config(bg="green", width=10, pady=10, text="Return", command=retbook, font=("Arial", 10, "bold"))
    returnButton.grid(column=0, row=5)

    renewbutton = Button()
    renewbutton.config(bg="gray", width=10, pady=10, text="Renew", command=renew, font=("Arial", 10, "bold"))
    renewbutton.grid(column=1, row=5)

    finelbl = Label()
    finelbl.config(text="Fines: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    finelbl.grid(column=0, row=3)

    conditionlbl = Label()
    conditionlbl.config(text="Condition: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    conditionlbl.grid(column=0, row=4)

    fine = Entry()
    fine.config(width=40, font=("Arial", 15, "normal"))
    fine.grid(column=1, row=3)

    condition = Entry()
    condition.config(width=40, font=("Arial", 15, "normal"))
    condition.grid(column=1, row=4)

    response = query.execute("select * from get_borrow_details()").fetchall()
    trv = ttk.Treeview(selectmode="browse")
    trv.grid(row=1, column=1)
    trv["columns"] = ("Book", "LibCard", "Employee", "IssueDate", "ReturnDate")
    trv["show"] = "headings"
    trv.column("Book", width=80, anchor="c")
    trv.column("LibCard", width=200, anchor="c")
    trv.column("Employee", width=120, anchor="c")
    trv.column("IssueDate", width=120, anchor="c")
    trv.column("ReturnDate", width=80, anchor="c")
    trv.heading("Book", text="Book")
    trv.heading("LibCard", text="LibCard")
    trv.heading("Employee", text="Employee")
    trv.heading("IssueDate", text="IssueDate")
    trv.heading("ReturnDate", text="ReturnDate")
    for row in response:
        trv.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))

    window.mainloop()


def issueBook():
    window = Tk()
    window.title("Dashboard")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    def goBack():
        window.destroy()
        empDashBoard()

    def issue():
        isbn = isbnselect.get()
        libcard = cardselect.get()
        empid = empidselect.get()
        book = ""
        card = ""
        emp = ""
        filter = ["(", ")", ","]
        for letters in isbn:
            if letters not in filter:
                book = book+letters
        for letters in libcard:
            if letters not in filter:
                card = card+letters
        for letters in empid:
            if letters not in filter:
                emp = emp+letters
        query.execute(f"exec borrow_book {book}, {card}, {emp}")

    gottenisbns = query.execute("select * from get_books()").fetchall()
    gottenlibcards = query.execute("select * from get_cardno()").fetchall()
    gottenempids = query.execute("select * from get_empid()").fetchall()

    isbnlbl = Label()
    isbnlbl.config(text="ISBN: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    isbnlbl.grid(column=0, row=1)

    titlelbl = Label()
    titlelbl.config(text="Library Card: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    titlelbl.grid(column=0, row=2)

    reldatelbl = Label()
    reldatelbl.config(text="Employee ID: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    reldatelbl.grid(column=0, row=3)

    isbnselect = StringVar()
    isbncb = ttk.Combobox(textvariable=isbnselect)
    isbncb.config(width=38, font=("Arial", 15, "normal"))
    isbncb["values"] = gottenisbns
    isbncb.grid(column=1, row=1)

    cardselect = StringVar()
    libcardcb = ttk.Combobox(textvariable=cardselect)
    libcardcb.config(width=38, font=("Arial", 15, "normal"))
    libcardcb["values"] = gottenlibcards
    libcardcb.grid(column=1, row=2)

    empidselect = StringVar()
    empidcb = ttk.Combobox(textvariable=empidselect)
    empidcb.config(width=38, font=("Arial", 15, "normal"))
    empidcb["values"] = gottenempids
    empidcb.grid(column=1, row=3)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=4)

    addButton = Button()
    addButton.config(bg="Green", width=10, pady=10, text="Issue", font=("Arial", 10, "bold"), command=issue)
    addButton.grid(column=0, row=4)

    window.mainloop()

def Donation():
    def goBack():
        window.destroy()
        empDashBoard()

    def add():
        isbn = isbne.get()
        title = titlee.get()
        reldate = reldatee.get()
        userid = useride.get()
        condition = conditione.get()
        query.execute(f"exec book_donate '{isbn}', '{title}', '{reldate}', {userid}, {condition}")
        query.execute("commit transaction")

    window = Tk()
    window.title("Book Donation")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    isbnlbl = Label()
    isbnlbl.config(text="ISBN: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    isbnlbl.grid(column=0, row=1)

    titlelbl = Label()
    titlelbl.config(text="Title: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    titlelbl.grid(column=0, row=2)

    reldatelbl = Label()
    reldatelbl.config(text="Release Date: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    reldatelbl.grid(column=0, row=3)

    usridlbl = Label()
    usridlbl.config(text="UserID: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    usridlbl.grid(column=0, row=4)

    bkcondition = Label()
    bkcondition.config(text="Book Condition(1-5): ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    bkcondition.grid(column=0, row=5)

    isbne = Entry()
    isbne.config(width=40, font=("Arial", 15, "normal"))
    isbne.grid(column=1, row=1)

    titlee = Entry()
    titlee.config(width=40, font=("Arial", 15, "normal"))
    titlee.grid(column=1, row=2)

    reldatee = Entry()
    reldatee.config(width=40, font=("Arial", 15, "normal"))
    reldatee.grid(column=1, row=3)

    useride = Entry()
    useride.config(width=40, font=("Arial", 15, "normal"))
    useride.grid(column=1, row=4)

    conditione = Entry()
    conditione.config(width=40, font=("Arial", 15, "normal"))
    conditione.grid(column=1, row=5)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=6)

    addButton = Button()
    addButton.config(bg="Green", width=10, pady=10, text="Add donation", font=("Arial", 10, "bold"), command=add)
    addButton.grid(column=0, row=6)

    window.mainloop()


def manageEmp():
    def goBack():
        window.destroy()
        empDashBoard()

    def addemp():
        window.destroy()
        newEmp()

    def remEmp():
        selected = trv.item(trv.focus())
        name = selected['values'][0]
        address = selected['values'][1]
        email = selected['values'][2]
        contact = selected['values'][3]
        jobtitle = selected['values'][4]
        query.execute(f"exec del_emp {name}, '{address}', '{email}', '{contact}', '{jobtitle}'")
        query.execute("commit transaction")

    window = Tk()
    window.title("Employees")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=3)

    addButton = Button()
    addButton.config(bg="Green", width=10, pady=10, text="Add Employee", font=("Arial", 10, "bold"), command=addemp)
    addButton.grid(column=1, row=2)

    removeButton = Button()
    removeButton.config(bg="red", width=10, pady=10, text="Remove Employee", font=("Arial", 10, "bold"), command=remEmp)
    removeButton.grid(column=2, row=2)

    response = query.execute("select * from get_emp()").fetchall()
    trv = ttk.Treeview(selectmode="browse")
    trv.grid(row=1, column=1, columnspan=2)
    trv["columns"] = ("Name", "Address", "Email", "Contact", "Jobtitle")
    trv["show"] = "headings"
    trv.column("Name", width=80, anchor="c")
    trv.column("Address", width=200, anchor="c")
    trv.column("Email", width=120, anchor="c")
    trv.column("Contact", width=120, anchor="c")
    trv.column("Jobtitle", width=80, anchor="c")
    trv.heading("Name", text="Name")
    trv.heading("Address", text="Address")
    trv.heading("Email", text="Email")
    trv.heading("Contact", text="Contact")
    trv.heading("Jobtitle", text="Jobtitle")
    for row in response:
        trv.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))

    window.mainloop()


def newEmp():
    def goBack():
        window.destroy()
        manageEmp()

    def addemp():
        name = ename.get()
        address = eaddress.get()
        contact = econtact.get()
        email = eemail.get()
        dob = edob.get()
        password = epass.get()
        selectedjob = job.get()
        jobtext = ""
        for letter in selectedjob:
            if letter not in ["(", ")", ","]:
                jobtext = jobtext + letter
        query.execute(f"exec add_emp '{name}', '{email}', '{contact}', {jobtext}, '{dob}', '{password}', '{address}'")
        query.execute("commit transaction")

    window = Tk()
    window.title("Add Employee")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    jobs = query.execute("select * from get_jobs()").fetchall()

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=8)

    addButton = Button()
    addButton.config(bg="Green", width=10, pady=10, text="Add Employee", font=("Arial", 10, "bold"), command=addemp)
    addButton.grid(column=0, row=8)

    empname = Label()
    empname.config(text="Name: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    empname.grid(column=0, row=1)

    empaddress = Label()
    empaddress.config(text="Address: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    empaddress.grid(column=0, row=2)

    empemail = Label()
    empemail.config(text="Email: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    empemail.grid(column=0, row=3)

    empcontact = Label()
    empcontact.config(text="Contact: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    empcontact.grid(column=0, row=4)

    empjob = Label()
    empjob.config(text="Job: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    empjob.grid(column=0, row=5)

    empdob = Label()
    empdob.config(text="DOB: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    empdob.grid(column=0, row=6)

    emppass = Label()
    emppass.config(text="Password: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    emppass.grid(column=0, row=7)

    ename = Entry()
    ename.config(width=40, font=("Arial", 15, "normal"))
    ename.grid(column=1, row=1)

    eaddress = Entry()
    eaddress.config(width=40, font=("Arial", 15, "normal"))
    eaddress.grid(column=1, row=2)

    eemail = Entry()
    eemail.config(width=40, font=("Arial", 15, "normal"))
    eemail.grid(column=1, row=3)

    econtact = Entry()
    econtact.config(width=40, font=("Arial", 15, "normal"))
    econtact.grid(column=1, row=4)

    job = StringVar()
    ejob = ttk.Combobox(textvariable=job)
    ejob.config(width=38, font=("Arial", 15, "normal"))
    ejob["values"] = jobs
    ejob.grid(column=1, row=5)

    edob = Entry()
    edob.config(width=40, font=("Arial", 15, "normal"))
    edob.grid(column=1, row=6)

    epass = Entry()
    epass.config(width=40, font=("Arial", 15, "normal"))
    epass.grid(column=1, row=7)

    window.mainloop()

def makeLibCard():
    def goBack():
        window.destroy()
        empDashBoard()

    def issueCard():
        name = user.get()
        libcardno = cardno.get()
        memberselect = member.get()
        membershipname = ""
        for letter in memberselect:
            if letter not in ["(", ")", ","]:
                membershipname = membershipname + letter
        query.execute(f"exec make_assign_card '{name}', '{libcardno}', {membershipname}")
        query.execute("commit transaction")

    members = query.execute("select * from get_memberships()").fetchall()
    window = Tk()
    window.title("Dashboard")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    memberselect = StringVar()
    member = ttk.Combobox(textvariable=memberselect)
    member.config(width=38, font=("Arial", 15, "normal"))
    member["values"] = members
    member.grid(column=1, row=2)

    user = Entry()
    user.config(width=40, font=("Arial", 15, "normal"))
    user.grid(column=1, row=1)

    membership = Label()
    membership.config(text="Membership Type: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    membership.grid(column=0, row=2)

    cardno = Entry()
    cardno.config(width=40, font=("Arial", 15, "normal"))
    cardno.grid(column=1, row=0)

    cardNo = Label()
    cardNo.config(text="Card Number: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    cardNo.grid(column=0, row=0)

    userName = Label()
    userName.config(text="User Name: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    userName.grid(column=0, row=1)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=3)

    assignbutton = Button()
    assignbutton.config(bg="Green", width=10, pady=10, text="Assign", font=("Arial", 10, "bold"), command=issueCard)
    assignbutton.grid(column=0, row=3)

    window.mainloop()


def ManageUsers():
    def goBack():
        window.destroy()
        empDashBoard()

    def addUser():
        window.destroy()
        newUser()

    def remUser():
        selected = trv.item(trv.focus())
        name = selected['values'][0]
        address = selected['values'][1]
        email = selected['values'][4]
        query.execute(f"exec delete_user {name}, '{address}', '{email}'")
        query.execute("commit transaction")

    window = Tk()
    window.title("Add New User")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=3)

    addButton = Button()
    addButton.config(bg="Green", width=10, pady=10, text="Add User", font=("Arial", 10, "bold"), command=addUser)
    addButton.grid(column=1, row=2)

    removeButton = Button()
    removeButton.config(bg="red", width=10, pady=10, text="Remove User", font=("Arial", 10, "bold"), command=remUser)
    removeButton.grid(column=2, row=2)

    response = query.execute("select * from get_users()").fetchall()
    trv = ttk.Treeview(selectmode="browse")
    trv.grid(row=1, column=1, columnspan=2)
    trv["columns"] = ("Name", "Address", "Phone", "DOB", "Email")
    trv["show"] = "headings"
    trv.column("Name", width=120, anchor="c")
    trv.column("Address", width=150, anchor="c")
    trv.column("Phone", width=120, anchor="c")
    trv.column("DOB", width=80, anchor="c")
    trv.column("Email", width=150, anchor="c")
    trv.heading("Name", text="Name")
    trv.heading("Address", text="Address")
    trv.heading("Phone", text="Phone")
    trv.heading("DOB", text="DOB")
    trv.heading("Email", text="Email")
    for row in response:
        trv.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))

    window.mainloop()


def newUser():
    def goBack():
        window.destroy()
        ManageUsers()

    def addUser():
        name = uname.get()
        address = uaddress.get()
        dob = udob.get()
        phone = uphone.get()
        email = uemail.get()
        query.execute(f"exec add_user '{name}', '{address}', '{dob}', '{phone}', '{email}'")
        query.execute("commit transaction")

    window = Tk()
    window.title("Add New User")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    unamelbl = Label()
    unamelbl.config(text="User Name: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    unamelbl.grid(column=0, row=1)

    uname = Entry()
    uname.config(width=40, font=("Arial", 15, "normal"))
    uname.grid(column=1, row=1)

    uaddresslbl = Label()
    uaddresslbl.config(text="User Address: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    uaddresslbl.grid(column=0, row=2)

    uaddress = Entry()
    uaddress.config(width=40, font=("Arial", 15, "normal"))
    uaddress.grid(column=1, row=2)

    uphonelbl = Label()
    uphonelbl.config(text="User Phone: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    uphonelbl.grid(column=0, row=3)

    uphone = Entry()
    uphone.config(width=40, font=("Arial", 15, "normal"))
    uphone.grid(column=1, row=3)

    udoblbl = Label()
    udoblbl.config(text="User DOB: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    udoblbl.grid(column=0, row=4)

    udob = Entry()
    udob.config(width=40, font=("Arial", 15, "normal"))
    udob.grid(column=1, row=4)

    uemaillbl = Label()
    uemaillbl.config(text="User Email: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    uemaillbl.grid(column=0, row=5)

    uemail = Entry()
    uemail.config(width=40, font=("Arial", 15, "normal"))
    uemail.grid(column=1, row=5)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=6)

    useradd = Button()
    useradd.config(bg="green", width=10, pady=10, text="Add", font=("Arial", 10, "bold"), command=addUser)
    useradd.grid(column=0, row=6)

    window.mainloop()


def newAuthor():
    def goBack():
        window.destroy()
        addBooks()

    def addAuthor():
        name = author.get()
        query.execute(f"exec adding_authors '{name}'")
        query.execute("commit transaction")

    window = Tk()
    window.title("Add an Author")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=2)

    author = Entry()
    author.config(width=40, font=("Arial", 15, "normal"))
    author.grid(column=1, row=1)

    authadd = Button()
    authadd.config(bg="green", width=10, pady=10, text="Add", font=("Arial", 10, "bold"), command=addAuthor)
    authadd.grid(column=0, row=2)

    Authtitle = Label()
    Authtitle.config(text="Author Name: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    Authtitle.grid(column=0, row=1)

    window.mainloop()


def newGenre():
    def goBack():
        window.destroy()
        addBooks()

    def addGenre():
        name = genre.get()
        query.execute(f"exec adding_genre '{name}'")
        query.execute("commit transaction")

    window = Tk()
    window.title("Add a Genre")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=2)

    genre = Entry()
    genre.config(width=40, font=("Arial", 15, "normal"))
    genre.grid(column=1, row=1)

    genreadd = Button()
    genreadd.config(bg="green", width=10, pady=10, text="Add", font=("Arial", 10, "bold"), command=addGenre)
    genreadd.grid(column=0, row=2)

    genretitle = Label()
    genretitle.config(text="Genre Name: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    genretitle.grid(column=0, row=1)

    window.mainloop()


def newPublisher():
    def goBack():
        window.destroy()
        addBooks()

    def addPublisher():
        name = Pub.get()
        query.execute(f"exec adding_Publishers '{name}'")
        query.execute("commit transaction")

    window = Tk()
    window.title("Add a Publisher")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=2)

    Pub = Entry()
    Pub.config(width=40, font=("Arial", 15, "normal"))
    Pub.grid(column=1, row=1)

    Pubadd = Button()
    Pubadd.config(bg="green", width=10, pady=10, text="Add", font=("Arial", 10, "bold"), command=addPublisher)
    Pubadd.grid(column=0, row=2)

    Pubtitle = Label()
    Pubtitle.config(text="Publisher Name: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    Pubtitle.grid(column=0, row=1)

    window.mainloop()


def addBooks():
    def goBack():
        window.destroy()
        empCatalogue()

    def addAuthor():
        window.destroy()
        newAuthor()

    def addGenre():
        window.destroy()
        newGenre()

    def addPublisher():
        window.destroy()
        newPublisher()

    def add():
        isbnno = isbn.get()
        booktitle = title.get()
        bookdate = date.get()
        authorn = authselect.get()
        authorname = ""
        for letters in authorn:
            if letters != "," and letters != "(" and letters != ")":
                authorname = authorname + letters
        genn = genselect.get()
        genrename = ""
        for letters in genn:
            if letters != "," and letters != "(" and letters != ")":
                genrename = genrename + letters
        pubn = pubselect.get()
        publishername = ""
        for letters in pubn:
            if letters != "," and letters != "(" and letters != ")":
                publishername = publishername + letters
        bs = bsselect.get()
        bookshelf = ""
        for letters in bs:
            if letters != "," and letters != "'" and letters != "(" and letters != ")":
                bookshelf = bookshelf + letters
        columnno = col.get()
        rowno = row.get()
        query.execute(
            f"exec book_entry {isbnno}, '{booktitle}', '{bookdate}', {authorname}, {genrename}, {publishername}, {bookshelf}, {rowno}, {columnno}")
        query.execute("commit transaction")

    authors = query.execute("select * from get_Authors()").fetchall()
    genres = query.execute("select * from get_Genre()").fetchall()
    publishers = query.execute("select * from get_Publishers()").fetchall()
    bookshelfs = query.execute("select * from get_Bookshelfs()").fetchall()

    window = Tk()
    window.title("Add a book")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=10)

    addButton = Button()
    addButton.config(bg="green", width=10, pady=10, text="Add", command=add, font=("Arial", 10, "bold"))
    addButton.grid(column=0, row=10)

    isbn = Entry()
    isbn.config(width=40, font=("Arial", 15, "normal"))
    isbn.grid(column=1, row=1)

    title = Entry()
    title.config(width=40, font=("Arial", 15, "normal"))
    title.grid(column=1, row=2)

    date = Entry()
    date.config(width=40, font=("Arial", 15, "normal"))
    date.grid(column=1, row=3)

    authselect = StringVar()
    author = ttk.Combobox(textvariable=authselect)
    author.config(width=38, font=("Arial", 15, "normal"))
    author['values'] = authors
    author.grid(column=1, row=4)

    genselect = StringVar()
    genre = ttk.Combobox(textvariable=genselect)
    genre.config(width=38, font=("Arial", 15, "normal"))
    genre["values"] = genres
    genre.grid(column=1, row=5)

    pubselect = StringVar()
    publisher = ttk.Combobox(textvariable=pubselect)
    publisher.config(width=38, font=("Arial", 15, "normal"))
    publisher["values"] = publishers
    publisher.grid(column=1, row=6)

    bsselect = StringVar()
    bookshelf = ttk.Combobox(textvariable=bsselect)
    bookshelf.config(width=38, font=("Arial", 15, "normal"))
    bookshelf["values"] = bookshelfs
    bookshelf.grid(column=1, row=7)

    col = Entry()
    col.config(width=40, font=("Arial", 15, "normal"))
    col.grid(column=1, row=8)

    row = Entry()
    row.config(width=40, font=("Arial", 15, "normal"))
    row.grid(column=1, row=9)

    isbntitle = Label()
    isbntitle.config(text="ISBN: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    isbntitle.grid(column=0, row=1)

    titletitle = Label()
    titletitle.config(text="Title: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    titletitle.grid(column=0, row=2)

    datetitle = Label()
    datetitle.config(text="Date (YYYY-MM-DD): ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    datetitle.grid(column=0, row=3)

    Authtitle = Label()
    Authtitle.config(text="Author: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    Authtitle.grid(column=0, row=4)

    genretitle = Label()
    genretitle.config(text="Genre: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    genretitle.grid(column=0, row=5)

    pubtitle = Label()
    pubtitle.config(text="Publisher: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    pubtitle.grid(column=0, row=6)

    bstitle = Label()
    bstitle.config(text="BookShelf: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    bstitle.grid(column=0, row=7)

    coltitle = Label()
    coltitle.config(text="Column: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    coltitle.grid(column=0, row=8)

    rowtitle = Label()
    rowtitle.config(text="Row: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    rowtitle.grid(column=0, row=9)

    authadd = Button()
    authadd.config(bg="green", width=10, pady=3, text="Add", font=("Arial", 10, "bold"), command=addAuthor)
    authadd.grid(column=2, row=4)

    genreadd = Button()
    genreadd.config(bg="green", width=10, pady=3, text="Add", font=("Arial", 10, "bold"), command=addGenre)
    genreadd.grid(column=2, row=5)

    pubadd = Button()
    pubadd.config(bg="green", width=10, pady=3, text="Add", font=("Arial", 10, "bold"), command=addPublisher)
    pubadd.grid(column=2, row=6)

    window.mainloop()


def empCatalogue():
    def goBack():
        window.destroy()
        empDashBoard()

    def addBook():
        window.destroy()
        addBooks()

    def deleteBook():
        selected = trv.item(trv.focus())
        isbn = selected['values'][0]
        title = selected['values'][1]
        author = selected['values'][2]
        publisher = selected['values'][3]
        genre = selected['values'][4]
        query.execute(f"exec delete_books {isbn}, '{title}', '{author}', '{genre}', '{publisher}'")
        query.execute("commit transaction")

    window = Tk()
    window.title("Catalogue")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=2, row=3)

    addButton = Button()
    addButton.config(bg="Green", width=10, pady=10, text="Add Book", font=("Arial", 10, "bold"), command=addBook)
    addButton.grid(column=1, row=2)

    removeButton = Button()
    removeButton.config(bg="red", width=10, pady=10, text="Remove Book", font=("Arial", 10, "bold"), command=deleteBook)
    removeButton.grid(column=2, row=2)

    response = query.execute("select * from get_books_catalog()").fetchall()
    trv = ttk.Treeview(selectmode="browse")
    trv.grid(row=1, column=1, columnspan=2)
    trv["columns"] = ("ISBN", "Title", "Author", "Publisher", "Genre", "BookShelf", "Row", "Column", "Available")
    trv["show"] = "headings"
    trv.column("ISBN", width=80, anchor="c")
    trv.column("Title", width=200, anchor="c")
    trv.column("Author", width=120, anchor="c")
    trv.column("Publisher", width=120, anchor="c")
    trv.column("Genre", width=80, anchor="c")
    trv.column("BookShelf", width=20, anchor="c")
    trv.column("Row", width=20, anchor="c")
    trv.column("Column", width=20, anchor="c")
    trv.column("Available", width=20, anchor="c")
    trv.heading("ISBN", text="ISBN")
    trv.heading("Title", text="Title")
    trv.heading("Author", text="Author")
    trv.heading("Publisher", text="Publisher")
    trv.heading("Genre", text="Genre")
    trv.heading("BookShelf", text="BookShelf")
    trv.heading("Row", text="Row")
    trv.heading("Column", text="Column")
    trv.heading("Available", text="Available")
    for row in response:
        trv.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    window.mainloop()


def userCatalog():
    def goBack():
        window.destroy()
        select()

    def res():
        selected = trv.item(trv.focus())
        title = selected['values'][0]
        author = selected['values'][1]
        genre = selected['values'][2]
        available = selected['values'][3]
        if available == "True":
            messagebox.showinfo(message="Cannot reserve book currently available")
        else:
            cardno = libcard.get()
            query.execute(f"exec reserve_book '{title}', '{cardno}'")
            query.execute("commit transaction")

    def doSearch():
        bkname = search.get()
        searchResults = query.execute(f"select * from user_book_search('{bkname}')")
        for item in trv.get_children():
            trv.delete(item)
        for rows in searchResults:
            trv.insert("", "end", values=(rows[0], rows[1], rows[2], rows[3]))


    window = Tk()
    window.title("User Catalogue")
    window.resizable(FALSE, FALSE)
    window.config(padx=50, pady=50, bg=BG_COLOR)

    backButton = Button()
    backButton.config(bg="red", width=10, pady=10, text="Back", command=goBack, font=("Arial", 10, "bold"))
    backButton.grid(column=3, row=5)

    searchlbl = Label()
    searchlbl.config(text="Book Name: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    searchlbl.grid(column=0, row=3)

    libcardlbl = Label()
    libcardlbl.config(text="Lib Card No.: ", font=("Arial", 15, "normal"), bg=BG_COLOR, pady=8)
    libcardlbl.grid(column=0, row=4)

    search = Entry()
    search.config(width=40, font=("Arial", 15, "normal"))
    search.grid(column=1, row=3)

    libcard = Entry()
    libcard.config(width=40, font=("Arial", 15, "normal"))
    libcard.grid(column=1, row=4)

    searchbtn = Button()
    searchbtn.config(bg="grey", width=10, pady=10, text="Search", command=doSearch, font=("Arial", 10, "bold"))
    searchbtn.grid(column=3, row=3)

    reserveBtn = Button()
    reserveBtn.config(bg="grey", width=10, pady=10, text="Reserve", command=res, font=("Arial", 10, "bold"))
    reserveBtn.grid(column=3, row=4)

    response = query.execute("select * from get_books_user()").fetchall()
    trv = ttk.Treeview(selectmode="browse")
    trv.grid(row=1, column=1, columnspan=2)
    trv["columns"] = ("Title", "Author", "Genre", "Available")
    trv["show"] = "headings"
    trv.column("Title", width=80, anchor="c")
    trv.column("Author", width=200, anchor="c")
    trv.column("Genre", width=120, anchor="c")
    trv.column("Available", width=120, anchor="c")
    trv.heading("Title", text="Title")
    trv.heading("Author", text="Author")
    trv.heading("Genre", text="Genre")
    trv.heading("Available", text="Available")
    for row in response:
        trv.insert("", "end", values=(row[0], row[1], row[2], row[3]))

    window.mainloop()

select()
