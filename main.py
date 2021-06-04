from tkinter import *
from tkinter import ttk 
from db import Database
import tkinter.messagebox as lo

db = Database("Employee.db")
root = Tk()
root.title("Employee Mangement System")
root.geometry("1366x768+0+0")
root.config(bg="#2c3e50")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()


#Entry Frame
entries_frame = Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title = Label(entries_frame,text="Employee Mangement System",font=("Calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan = 2,padx=10,pady=20)

lblName = Label(entries_frame,text="Name",font=("Calibri",14,),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10, sticky="w")
txtName = Entry(entries_frame,textvariable=name,font=("Calibri",14,),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10, sticky="w")

lblAge = Label(entries_frame,text="Age",font=("Calibri",14,),bg="#535c68",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10, sticky="w")
txtAge = Entry(entries_frame,textvariable=age,font=("Calibri",14,),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10, sticky="w")

lbldoj = Label(entries_frame,text="D.O.J",font=("Calibri",14,),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10, sticky="w")
txtdoj = Entry(entries_frame,textvariable=doj,font=("Calibri",14,),width=30)
txtdoj.grid(row=2,column=1,padx=10,pady=10, sticky="w")

lblEmail = Label(entries_frame,text="Email",font=("Calibri",14,),bg="#535c68",fg="white")
lblEmail.grid(row=2,column=2,padx=10,pady=10, sticky="w")
txtEmail = Entry(entries_frame,textvariable=email,font=("Calibri",14,),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=10, sticky="w")

lblGender = Label(entries_frame,text="Gender",font=("Calibri",14,),bg="#535c68",fg="white")
lblGender.grid(row=3,column=0,padx=10,pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame,font=("Calibri",14),width=29,textvariable=gender,state="readonly")
comboGender['values'] = ("Male","Female")
comboGender.grid(row=3,column=1,pady=10,padx=10,sticky='w')

lblContact = Label(entries_frame,text="Contact",font=("Calibri",14,),bg="#535c68",fg="white")
lblContact.grid(row=3,column=2,padx=10,pady=10, sticky="w")
txtContact = Entry(entries_frame,textvariable=contact,font=("Calibri",14,),width=30)
txtContact.grid(row=3,column=3,padx=10,pady=10, sticky="w")

lblAdderss = Label(entries_frame,text="Adderss",font=("Calibri",14,),bg="#535c68",fg="white")
lblAdderss.grid(row=4,column=0,padx=10,pady=10, sticky="w")
txtAddress = Text(entries_frame,width=85,height=5,font=("Calibri",16))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,pady=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row) 

def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtdoj.get() == "" or txtEmail.get() == "" or txtContact.get() == "" or txtAddress.get(1.0,END) == "" or comboGender.get() == "" :
        lo.showerror("Please fill all the Details")
        return
    db.insert(txtName.get(),txtAge.get(),txtdoj.get(),txtEmail.get() == "",comboGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    lo.showinfo("Inserted Succesfully")
    clear_employee()
    displayAll()

def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtdoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        lo.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtdoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(
                  1.0, END))
    lo.showinfo("Success", "Record Update")
    clear_employee()
    displayAll()


def remove_employee():
    db.remove(row[0])
    clear_employee()
    displayAll()

def clear_employee():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)

btn_frame = Frame(entries_frame,bg='#535c68')
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky='w')
btnAdd = Button(btn_frame,command=add_employee,text="Add Details",width=11,font=("Calibri",12,"bold"),bg="#16a085",bd=0,fg="white").grid(row=0,column=0)
btnAdd = Button(btn_frame,command=update_employee,text="Update Details",width=11,font=("Calibri",12,"bold"),bg="#2980b9",bd=0,fg="white").grid(row=0,column=1,padx=10)
btnAdd = Button(btn_frame,command=remove_employee,text="Delete Details",width=11,font=("Calibri",12,"bold"),bg="#c0392b",bd=0,fg="white").grid(row=0,column=2,padx=10)
btnAdd = Button(btn_frame,command=clear_employee,text="Clear Details",width=11,font=("Calibri",12,"bold"),bg="#f39c12",bd=0,fg="white").grid(row=0,column=3,padx=10)
#Table Frame
tree_frame = Frame(root,bg='#ecf0f1')
tree_frame.place(x=0,y=480,width=1980,height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibre',12),rowheight=50)
style.configure("mystyle.Treeview.Heading",font = ('Calibre',12))
tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=1)
tv.heading("2",text="Name")
tv.column("2",width=2)
tv.heading("3",text="Age")
tv.column("3",width=2)
tv.heading("4",text="D.O.J")
tv.column("4",width=2)
tv.heading("5",text="Email")
tv.heading("6",text="Gender")
tv.column("6",width=2)
tv.column("5",width=5)
tv.column("1",width=2)
tv.heading("7",text="Contact")
tv.heading("8",text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

displayAll()

root.mainloop()
