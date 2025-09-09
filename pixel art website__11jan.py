import tkinter as tk
import csv
import os


# Create a global variable to store the username
current_user = ""
user=""

#window
t = tk.Tk()
t.title('sign up or login')
t.geometry('2000x1000')
t['bg']='white'

#creating 10 frames
frames=[]
for i in range(10):
    frame = tk.Frame(t, bg='white')
    frame.pack(fill=tk.BOTH, expand=True)
    frames.append(frame)

#move to next frame by packing and forgetting
def showframe(index):
    for i in range(len(frames)):
        if i==index:
            frames[i].pack()
        else:
            frames[i].pack_forget()
############################################################

#heading label
label = tk.Label(frames[0], text="Are you admin or user? ")
label.config(font=("Arial", 20),width=100, height=10,bg="white")
label.pack()

#admin option
b1=tk.Button(frames[0],text='Admin',command=lambda:admpswd(1))
b1.config(font=("times",20,'bold'),width=40, height=3,bg="cornflower blue")
b1.pack()

#create gap space
s1= tk.Label(frames[0],width=70, height=2,bg="white")
s1.pack()

#user option
b2=tk.Button(frames[0],text='User',command=lambda:signuplogin(2))
b2.config(font=("times",20,'bold'),width=40, height=3,bg="lawn green")
b2.pack()

def signuplogin(index):
    #heading label
    label = tk.Label(frames[index], text="Hello there! \n sign up or login to enter into the website ")
    label.config(font=("Arial", 20),width=100, height=10,bg="white")
    label.pack()

    #sign up option
    b1=tk.Button(frames[index],text='Sign Up',command=lambda:signup(3))
    b1.config(font=("times",20,'bold'),width=40, height=3,bg="red",fg='white')
    b1.pack()

    #create gap space
    s1= tk.Label(frames[index],width=70, height=2,bg="white")
    s1.pack()

    #login option
    b2=tk.Button(frames[index],text='Login',command=lambda:login(4))
    b2.config(font=("times",20,'bold'),width=40, height=3,bg="blue",fg='white')
    b2.pack()

    showframe(index)


def signup(index):
    #header label
    l = tk.Label(frames[index], text='Sign Up', font=("times",40,'bold'),width=70, height=2,bg="white")
    l.pack()

    # Create a label for email
    email_label = tk.Label(frames[index], text="Email:",font=("times",30,'bold'), width=40, height=3, bg="white")
    email_label.pack()

    # Create an entry widget for email
    email_entry = tk.Entry(frames[index])
    email_entry.pack()

    # Create a label for password
    password_label = tk.Label(frames[index], text="Password:",font=("times",30,'bold'), width=40, height=3, bg="white")
    password_label.pack()

    # Create an entry widget for password
    password_entry = tk.Entry(frames[index], show="*")
    password_entry.pack()

    #create gap space
    s2= tk.Label(frames[index],width=70, height=2,bg="white")
    s2.pack()

    # Create a button to register the user
    entry_button = tk.Button(frames[index], text="Enter",font=("times",25,'bold'),width=15, height=2,bg='green',fg='white',command=lambda:enter(email_entry.get(), password_entry.get()))
    entry_button.pack()

    def enter(email, password):
        # Check if the fields are empty
        if email == "" or password == "" :
            message1.config(text="Please fill all the fields")

        else:
            with open('userdata.csv', 'r') as file:
                reader = csv.reader(file)
                for i in reader:
                    if i[1] == email or i[2]==password:
                        message1.config(text="details already exist")
                        break
                else:
                    profile(5,email,password)
    #REPEAT MESSAGE JUST ONCE
    message1 = tk.Label(frames[index],font=("times",15,'bold'), bg='white',fg="red")
    message1.pack()


    showframe(index)
    


def login(index):
    #header label
    l = tk.Label(frames[index], text='Login', font=("times",40,'bold'),width=70, height=2,bg="white")
    l.pack()

    # Create a label for email
    email_label = tk.Label(frames[index], text="Email:",font=("times",30,'bold'), width=40, height=3, bg="white")
    email_label.pack()

    # Create an entry widget for email
    email_entry = tk.Entry(frames[index])
    email_entry.pack()

    # Create a label for password
    password_label = tk.Label(frames[index], text="Password:",font=("times",30,'bold'), width=40, height=3, bg="white")
    password_label.pack()

    # Create an entry widget for password
    password_entry = tk.Entry(frames[index], show="*")
    password_entry.pack()

    #create gap space
    s1= tk.Label(frames[index],width=70, height=2,bg="white")
    s1.pack()

    # Create a button to register the user
    entry_button = tk.Button(frames[index], text="Enter",font=("times",25,'bold'),width=15, height=2,bg='green',fg='white',command=lambda:verify(email_entry.get(), password_entry.get()))
    entry_button.pack()

    def verify(email, password):
        global current_user
        global user
        # Check if the fields are empty
        if email == "" or password == "":
            message2.config(text="please fill in all the fields")

        
        else:
            # to check if the login detail is correct
            with open('userdata.csv', 'r') as file:
                reader = csv.reader(file)
                for i in reader:
                    if i[1]==email and i[2]==password:
                        current_user = i[1]# Assign the email to the global variable
                        user=i[0] # Assign the username to the global variable
                        t.destroy()
                        pixel()
                        break
                else:
                    message2.config(text="Email or password is incorrect, please try again")
                
    #REPEAT MESSAGE JUST ONCE
    message2 = tk.Label(frames[index],font=("times",15,'bold'), bg='white',fg="red")
    message2.pack()



    showframe(index)


def profile(index,email,password):

    l1 = tk.Label(frames[index], text="Create Profile Page")
    l1.config(font=("times",50,'bold'),width=60, height=1,bg="white")
    l1.pack()

    # Create a label for username
    username = tk.Label(frames[index], text="username:",font=("times",30,'bold'), width=40, height=1, bg="white")
    username.pack()

    # Create an entry widget for username
    username_entry = tk.Entry(frames[index])
    username_entry.pack()

    # Create a label for phone number
    phone = tk.Label(frames[index], text="phone number:",font=("times",30,'bold'), width=40, height=2, bg="white")
    phone.pack()

    # Create an entry widget for phone number
    phone_entry = tk.Entry(frames[index])
    phone_entry.pack()

    # Create a label for age
    age = tk.Label(frames[index], text="age:",font=("times",30,'bold'), width=40, height=2, bg="white")
    age.pack()

    # Create an entry widget for age
    age_entry = tk.Entry(frames[index])
    age_entry.pack()

    # Create a label for gender
    gender = tk.Label(frames[index], text="gender:",font=("times",30,'bold'), width=40, height=2, bg="white")
    gender.pack()

    # Create an entry widget for gender
    gender_entry = tk.Entry(frames[index])
    gender_entry.pack()

    #create gap space
    s1= tk.Label(frames[index],width=70, height=2,bg="white")
    s1.pack()

    # Create a button to register the user
    entry_button = tk.Button(frames[index], text="Submit", font=("times", 25, 'bold'), width=15, height=2,bg='green', fg='white',command=lambda: details(username_entry.get(), email, password,phone_entry.get(), age_entry.get(), gender_entry.get()))
    entry_button.pack()

    def details(username,email, password,phone,age,gender):
        global current_user
        global user

        # Assign the username to the current_user variable
        current_user = email
        user=username
        # Check if the fields are empty
        if username == "" or phone == "" or age=="" or gender=="":
            message.config(text="please fill in all the fields")
        
        else:
            with open('userdata.csv', 'r') as file:
                reader = csv.reader(file)
                for i in reader:
                    if i[0] == username or i[3]==phone:
                        message.config(text="details already exist")
                        break
                else:
                    # Write the data to a CSV file
                    with open('userdata.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([username,email, password,phone,age,gender])
                                    
                        t.destroy()
                        pixel()

    #REPEAT MESSAGE JUST ONCE
    message = tk.Label(frames[index],font=("times",15,'bold'), bg='white',fg="red")
    message.pack()

    showframe(index)

def admpswd(index):
        #header label
        l = tk.Label(frames[index], text='Admin', font=("times",40,'bold'),width=70, height=2,bg="white")
        l.pack()

        # Create a label for password
        pswd_label = tk.Label(frames[index], text="Enter Admin Password:",font=("times",30,'bold'), width=40, height=3, bg="white")
        pswd_label.pack()

        # Create an entry widget for password
        pswd_entry = tk.Entry(frames[index], show="*")
        pswd_entry.pack()

        #create gap space
        s1= tk.Label(frames[index],width=70, height=2,bg="white")
        s1.pack()

        # Create a button to register the admin
        entry_button = tk.Button(frames[index], text="Enter",font=("times",25,'bold'),width=15, height=2,bg='green',fg='white',command=lambda:verify(pswd_entry.get()))
        entry_button.pack()

        #create gap space
        s2= tk.Label(frames[index],width=70, height=5,bg="white")
        s2.pack()

        def verify(pswd):
            # Check if the fields are empty
            if pswd == "":
                message1.config(text="Password field empty")

            
            else:
                if pswd=='roothangu':
                    csvoption(6)
                    # Clear the password entry field and error message
                    pswd_entry.delete(0, 'end')
                    message1.config(text='')
                else:
                    message1.config(text="Password is incorrect, please try again")

        #REPEAT MESSAGE JUST ONCE
        message1 = tk.Label(frames[index],font=("times",15,'bold'), bg='white',fg="red")
        message1.pack()

        #create gap space
        s3= tk.Label(frames[index],width=70, height=30,bg="white")
        s3.pack()

        showframe(index)

def csvoption(index):
    #create gap space
    s1= tk.Label(frames[index])
    s1.config(width=70, height=5,bg="white")
    s1.pack()
        
    #view user logins
    b1=tk.Button(frames[index],text='View User Logins',command=lambda:csvuserlogin())
    b1.config(font=("times",20,'bold'),width=40, height=3,bg="green yellow")
    b1.pack()

    #create gap space
    s2= tk.Label(frames[index])
    s2.config(width=70, height=1,bg="white")
    s2.pack()

    #view user works
    b2=tk.Button(frames[index],text='View User Works',command=lambda:csvuserwork())
    b2.config(font=("times",20,'bold'),width=40, height=3,bg="hot pink")
    b2.pack()

    #create gap space
    s3= tk.Label(frames[index])
    s3.config(width=70, height=1,bg="white")
    s3.pack()

    #view delete user
    b3=tk.Button(frames[index],text='Delete User',command=lambda:deleteuser(7))
    b3.config(font=("times",20,'bold'),width=40, height=3,bg="hot pink")
    b3.pack()

    #create gap space
    s4= tk.Label(frames[index])
    s4.config(width=70, height=1,bg="white")
    s4.pack()

    #back button
    back = tk.Button(frames[index], text="Back",width=17, height=2,bg='green',fg='white',font=("times",20,'bold'),command=lambda:showframe(0))
    back.pack()

    #create gap space
    s5= tk.Label(frames[index])
    s5.config(width=70, height=20,bg="white")
    s5.pack()

    showframe(index)

def csvuserlogin():
    filename = "userdata"
    os.system("start excel.exe " + filename)

def csvuserwork():
    filename = "pixelarts"
    os.system("start excel.exe " + filename)


def deleteuser(index):
    def delete():
        name = name_entry.get()
        rows1_to_keep = []
        if name=='':
            message2.config(text="Please fill the field")

        else:
            with open('userdata.csv', 'r') as file:
                reader1 = csv.reader(file)
                rows1 = list(reader1)
                for i in rows1:
                    if name != i[0]:
                        rows1_to_keep.append(i)
            rows2_to_keep = []
            with open('pixelarts.csv', 'r') as pfile:
                reader2 = csv.reader(pfile)
                rows2= list(reader2)
                for i in rows2:
                    if name != i[0]:
                        rows2_to_keep.append(i)
            if len(rows1_to_keep) == len(rows1) and len(rows2_to_keep) == len(rows2):
                message2.config(text="Username not found")
            else:
                write(rows1_to_keep, rows2_to_keep)

        

    def write(rows1,rows2):
        with open('userdata.csv', 'w', newline='') as file:
            writer1 = csv.writer(file)
            writer1.writerows(rows1)
        with open('pixelarts.csv', 'w',newline="") as pfile:
            writer2 = csv.writer(pfile)
            writer2.writerows(rows2)
            csvoption(6)
            name_entry.delete(0,tk.END)
            message2.pack_forget()


    #create gap space
    s1= tk.Label(frames[index])
    s1.config(width=70, height=5,bg="white")
    s1.pack()

    # Create a label and entry widget for entering the username
    name_label = tk.Label(frames[index], text="Enter username:",font=("times",30,'bold'),width=40, height=1,bg="white")
    name_label.pack()
    name_entry = tk.Entry(frames[index])
    name_entry.pack()

    #create gap space
    s2= tk.Label(frames[index])
    s2.config(width=70, height=5,bg="white")
    s2.pack()

    # Create a button for deleting the details
    delete_button = tk.Button(frames[index], text="Delete", command=lambda:delete(),font=("times",30,'bold'),width=10, height=1,bg="red",fg='white')
    delete_button.pack()

    # REPEAT MESSAGE ONCE
    message2 = tk.Label(frames[index], text="",bg='white',fg='red',font=("times",15,'bold'))
    message2.pack()

    #create gap space
    s3= tk.Label(frames[index])
    s3.config(width=70, height=30,bg="white")
    s3.pack()

    showframe(index)



def pixel():
    import csv
    
    # importing pixel art files

    #with grid
    import avocado
    import nightcat
    import heartcup
    import mushroom
    import potrait
    import uno
    import flower
    import cateye
    import whitecat
    import cathi
    import heart
    import pyramid
    import penguin
    import dog

    #without grid
    import avocado1
    import nightcat1
    import heartcup1
    import mushroom1
    import potrait1
    import uno1
    import flower1
    import cateye1
    import whitecat1
    import cathi1
    import heart1
    import pyramid1
    import penguin1
    import dog1

    import tkinter as tk
    t = tk.Tk()
    t.geometry('2000x1000')
    t['bg']='darkorchid1'

    #creating 10 frames
    frames=[]
    for i in range(10):
        frame = tk.Frame(t, bg='darkorchid1')
        frame.pack(fill=tk.BOTH, expand=True)
        frames.append(frame)

    #move to next frame by packing and forgetting
    def showframe(index):
        for i in range(len(frames)):
            if i==index:
                frames[i].pack()
            else:
                frames[i].pack_forget()
        
    #########################################################
    #creating first frame
    l1 = tk.Label(frames[0], text="Welcome To Our Website ")
    l1.config(font=("times",50,'bold'),width=70, height=3,bg="darkorchid1")
    l1.pack()

    #start drawing button
    b1=tk.Button(frames[0],text='Start Drawing',command=lambda:createart())
    b1.config(font=("times",20,'bold'),width=40, height=3,bg="green yellow")
    b1.pack()

    #create gap space
    s1= tk.Label(frames[0])
    s1.config(width=70, height=1,bg="darkorchid1")
    s1.pack()

    #view others art button
    b2=tk.Button(frames[0],text='View Developer\' s Art',command=lambda:gridoption(1))
    b2.config(font=("times",20,'bold'),width=40, height=3,bg="hotpink")
    b2.pack()

    #create gap space
    s2= tk.Label(frames[0])
    s2.config(width=70, height=1,bg="darkorchid1")
    s2.pack()

    #edit profile details
    b2=tk.Button(frames[0],text='Edit My Profile',command=lambda:editprofile(4))
    b2.config(font=("times",20,'bold'),width=40, height=3,bg="cornflower blue")
    b2.pack()
    
    #################################################################


    def gridoption(index):

        #create gap space
        s1= tk.Label(frames[index])
        s1.config(width=70, height=15,bg="darkorchid1")
        s1.pack()
        
        #view with grid
        b3=tk.Button(frames[index],text='View With Grid',command=lambda:grid(2))
        b3.config(font=("times",20,'bold'),width=40, height=3,bg="green yellow")
        b3.pack()

        #create gap space
        s2= tk.Label(frames[index])
        s2.config(width=70, height=1,bg="darkorchid1")
        s2.pack()

        #view without grid
        b4=tk.Button(frames[index],text='View Without Grid',command=lambda:nogrid(3))
        b4.config(font=("times",20,'bold'),width=40, height=3,bg="hot pink")
        b4.pack()

        #create gap space
        s3= tk.Label(frames[index])
        s3.config(width=100, height=5,bg="darkorchid1")
        s3.pack()


        #packing frame
        showframe(index)

    def grid(index):

        # Create buttons and place them in a grid with padding
        button1 = tk.Button(frames[index], text="Avacado",width=17, height=4,bg='green yellow',font=("times",20,'bold'),command=lambda:avocado.avocado())
        button1.grid(row=0, column=0, padx=30, pady=15)

        button2 = tk.Button(frames[index], text="Night Cat",width=17, height=4,bg='cornflower blue',font=("times",20,'bold'),command=lambda:nightcat.nightcat())
        button2.grid(row=0, column=1, padx=30, pady=15)

        button3 = tk.Button(frames[index], text="Cat Eye",width=17, height=4,bg='orange',font=("times",20,'bold'),command=lambda:cateye.cateye())
        button3.grid(row=0, column=2, padx=30, pady=15)

        button4 = tk.Button(frames[index], text="Heartcup",width=17, height=4,bg='salmon',font=("times",20,'bold'),command=lambda:heartcup.heartcup())
        button4.grid(row=0, column=3, padx=30, pady=15)

        button5 = tk.Button(frames[index], text="Uno 4+",width=17, height=4,bg='white',font=("times",20,'bold'),command=lambda:uno.uno())
        button5.grid(row=1, column=0, padx=30, pady=15)

        button6 = tk.Button(frames[index], text="Flower Pattern",width=17, height=4,bg='lawn green',font=("times",20,'bold'),command=lambda:flower.flower())
        button6.grid(row=1, column=1, padx=30, pady=15)

        button7 = tk.Button(frames[index], text="Potrait",width=17, height=4,bg='sienna3',font=("times",20,'bold'),command=lambda:potrait.potrait())
        button7.grid(row=1, column=2, padx=30, pady=15)

        button8 = tk.Button(frames[index], text="Mushroom in a Jar",width=17, height=4,bg='magenta2',font=("times",20,'bold'),command=lambda:mushroom.mushroom())
        button8.grid(row=1, column=3, padx=30, pady=15)

        button9 = tk.Button(frames[index], text="Heart Pattern",width=17, height=4,bg='pink',font=("times",20,'bold'),command=lambda:heart.heart())
        button9.grid(row=2, column=0, padx=30, pady=15)

        button10 = tk.Button(frames[index], text="Pyramids",width=17, height=4,bg='gold',font=("times",20,'bold'),command=lambda:pyramid.pyramid())
        button10.grid(row=2, column=1, padx=30, pady=15)

        button11 = tk.Button(frames[index], text="White Cat",width=17, height=4,bg='plum2',font=("times",20,'bold'),command=lambda:whitecat.whitecat())
        button11.grid(row=2, column=2, padx=30, pady=15)

        button12 = tk.Button(frames[index], text="Cat Says Hi",width=17, height=4,bg='gold',font=("times",20,'bold'),command=lambda:cathi.cathi())
        button12.grid(row=2, column=3, padx=30, pady=15)

        button13 = tk.Button(frames[index], text="Dog",width=17, height=4,bg='purple1',font=("times",20,'bold'),command=lambda:dog.dog())
        button13.grid(row=3, column=0, padx=30, pady=15)

        button14 = tk.Button(frames[index], text="penguin",width=17, height=4,bg='white',font=("times",20,'bold'),command=lambda:penguin.penguin())
        button14.grid(row=3, column=1, padx=30, pady=15)

        button15 = tk.Button(frames[index], text="Back",width=17, height=4,bg='green',fg='white',font=("times",20,'bold'),command=lambda:showframe(0))
        button15.grid(row=3, column=2, padx=30, pady=15)




         #packing frame
        showframe(index)

    def nogrid(index):

        # Create buttons and place them in a grid with padding
        button1 = tk.Button(frames[index], text="Avacado",width=17, height=4,bg='green yellow',font=("times",20,'bold'),command=lambda:avocado1.avocado1())
        button1.grid(row=0, column=0, padx=30, pady=15)

        button2 = tk.Button(frames[index], text="Night Cat",width=17, height=4,bg='cornflower blue',font=("times",20,'bold'),command=lambda:nightcat1.nightcat1())
        button2.grid(row=0, column=1, padx=30, pady=15)

        button3 = tk.Button(frames[index], text="Cat Eye",width=17, height=4,bg='orange',font=("times",20,'bold'),command=lambda:cateye1.cateye1())
        button3.grid(row=0, column=2, padx=30, pady=15)

        button4 = tk.Button(frames[index], text="Heartcup",width=17, height=4,bg='salmon',font=("times",20,'bold'),command=lambda:heartcup1.heartcup1())
        button4.grid(row=0, column=3, padx=30, pady=15)

        button5 = tk.Button(frames[index], text="Uno 4+",width=17, height=4,bg='white',font=("times",20,'bold'),command=lambda:uno1.uno1())
        button5.grid(row=1, column=0, padx=30, pady=15)

        button6 = tk.Button(frames[index], text="Flower Pattern",width=17, height=4,bg='lawn green',font=("times",20,'bold'),command=lambda:flower1.flower1())
        button6.grid(row=1, column=1, padx=30, pady=15)

        button7 = tk.Button(frames[index], text="Potrait",width=17, height=4,bg='sienna3',font=("times",20,'bold'),command=lambda:potrait1.potrait1())
        button7.grid(row=1, column=2, padx=30, pady=15)

        button8 = tk.Button(frames[index], text="Mushroom in a Jar",width=17, height=4,bg='magenta2',font=("times",20,'bold'),command=lambda:mushroom1.mushroom1())
        button8.grid(row=1, column=3, padx=30, pady=15)

        button9 = tk.Button(frames[index], text="Heart Pattern",width=17, height=4,bg='pink',font=("times",20,'bold'),command=lambda:heart1.heart1())
        button9.grid(row=2, column=0, padx=30, pady=15)

        button10 = tk.Button(frames[index], text="Pyramids",width=17, height=4,bg='gold',font=("times",20,'bold'),command=lambda:pyramid1.pyramid1())
        button10.grid(row=2, column=1, padx=30, pady=15)

        button11 = tk.Button(frames[index], text="White Cat",width=17, height=4,bg='plum2',font=("times",20,'bold'),command=lambda:whitecat1.whitecat1())
        button11.grid(row=2, column=2, padx=30, pady=15)

        button12 = tk.Button(frames[index], text="Cat Says Hi",width=17, height=4,bg='gold',font=("times",20,'bold'),command=lambda:cathi1.cathi1())
        button12.grid(row=2, column=3, padx=30, pady=15)

        button13 = tk.Button(frames[index], text="Dog",width=17, height=4,bg='purple1',font=("times",20,'bold'),command=lambda:dog1.dog1())
        button13.grid(row=3, column=0, padx=30, pady=15)

        button14 = tk.Button(frames[index], text="Penguin",width=17, height=4,bg='white',font=("times",20,'bold'),command=lambda:penguin1.penguin1())
        button14.grid(row=3, column=1, padx=30, pady=15)

        button15 = tk.Button(frames[index], text="Back",width=17, height=4,bg='green',fg='white',font=("times",20,'bold'),command=lambda:showframe(0))
        button15.grid(row=3, column=2, padx=30, pady=15)



         #packing frame
        showframe(index)


    def editprofile(index):
        def display_details():
            global current_user
            email =current_user
            username=user
            with open('userdata.csv', 'r') as file:
                reader = csv.reader(file)
                for i in reader:
                    if i[1] == email:
                        username_entry.delete(0, tk.END)
                        username_entry.insert(tk.END, i[0])
                        email_entry.delete(0, tk.END)
                        email_entry.insert(tk.END, i[1])
                        password_entry.delete(0, tk.END)
                        password_entry.insert(tk.END, i[2])
                        phone_entry.delete(0, tk.END)
                        phone_entry.insert(tk.END, i[3])
                        age_entry.delete(0, tk.END)
                        age_entry.insert(tk.END, i[4])
                        gender_entry.delete(0, tk.END)
                        gender_entry.insert(tk.END, i[5])
                    
        def save_details():
            global current_user
            global user
            email = current_user
            username = username_entry.get()
            password = password_entry.get()
            phone = phone_entry.get()
            age = age_entry.get()
            gender = gender_entry.get()
            rows2=[]
            with open('pixelarts.csv','r') as pfile:
                reader2 = csv.reader(pfile)
                for j in reader2:
                    if j[0]==user:
                        j[0]=username
                    rows2.append(j)
            user=username
            rows1= []
            with open('userdata.csv', 'r') as file:
                reader1 = csv.reader(file)
                for i in reader1:
                    if i[1] == email:
                        i[0] = username
                        i[1] = email
                        i[2] = password
                        i[3] = phone
                        i[4] = age
                        i[5] = gender
                    rows1.append(i)
            with open('userdata.csv', 'w', newline='') as file:
                writer1 = csv.writer(file)
                writer1.writerows(rows1)
            with open('pixelarts.csv', 'w', newline='') as pfile:
                writer2 = csv.writer(pfile)
                writer2.writerows(rows2)
                showframe(0)

        #create gap space
        s1= tk.Label(frames[index])
        s1.config(width=70, height=1,bg="darkorchid1")
        s1.pack()

        # Create a button for displaying the details
        dislay_button = tk.Button(frames[index], text="Display details", command=display_details,font=("times",20,'bold'),width=10, height=1,bg="lawn green")
        dislay_button.pack()

        # Create labels and entry widgets for the details
        username_label = tk.Label(frames[index], text="Username:", font=("times",20,'bold'), width=40, height=2, bg="darkorchid1")
        username_label.pack()
        username_entry = tk.Entry(frames[index])
        username_entry.pack()

        
        # Create labels and entry widgets for the details
        email_label = tk.Label(frames[index], text="Email:",font=("times",20,'bold'),width=40, height=2,bg="darkorchid1")
        email_label.pack()
        email_entry = tk.Entry(frames[index])
        email_entry.pack()

        password_label = tk.Label(frames[index], text="Password:",font=("times",20,'bold'),width=40, height=2,bg="darkorchid1")
        password_label.pack()
        password_entry = tk.Entry(frames[index])
        password_entry.pack()

        phone_label = tk.Label(frames[index], text="Phone:",font=("times",20,'bold'),width=40, height=2,bg="darkorchid1")
        phone_label.pack()
        phone_entry = tk.Entry(frames[index])
        phone_entry.pack()

        age_label = tk.Label(frames[index], text="Age:",font=("times",20,'bold'),width=40, height=2,bg="darkorchid1")
        age_label.pack()
        age_entry = tk.Entry(frames[index])
        age_entry.pack()

        gender_label = tk.Label(frames[index], text="Gender:",font=("times",20,'bold'),width=40, height=2,bg="darkorchid1")
        gender_label.pack()
        gender_entry = tk.Entry(frames[index])
        gender_entry.pack()

        #create gap space
        s2= tk.Label(frames[index])
        s2.config(width=70, height=1,bg="darkorchid1")
        s2.pack()

        # Create a button for saving the details
        save_button = tk.Button(frames[index], text="Save details", command=save_details,font=("times",20,'bold'),width=10, height=1,bg="lawn green")
        save_button.pack()

        #create gap space
        s3= tk.Label(frames[index])
        s3.config(width=70, height=1,bg="darkorchid1")
        s3.pack()

        # REPEAT MESSAGE ONCE
        message = tk.Label(frames[index], text="",bg='darkorchid1',fg='white',font=("times",15,'bold'))
        message.pack()

        showframe(index)

def createart():
    import tkinter as tk
    import tkinter.colorchooser as cc
    from tkinter import filedialog
    from PIL import Image, ImageDraw
    import pickle
    import csv
    import os

    # Calculate the number of pixels needed for an 18cmx18cm area
    pixels_per_cm = 37.7952756
    width = int(18 * pixels_per_cm)
    height = int(18 * pixels_per_cm)

    # Calculate the number of pixels needed for 30 rows and columns of pixels
    pixel_size = int(width / 30)

    # Create the main window
    root = tk.Tk()
    root.title("Pixel Art Creator")  # Set the title of the window

    # Set the background color of the window to light pink
    window_bg_color = 'darkorchid1'
    root.configure(bg=window_bg_color)

    # Create a frame with light pink background
    frame = tk.Frame(root, bg=window_bg_color)
    frame.pack()

    # Create the Canvas widget with the calculated dimensions and place it inside the frame
    canvas = tk.Canvas(frame, width=width, height=height, bg=window_bg_color)
    canvas.pack(side='left')

    # Define a variable to store the selected color
    canvas.color = 'black'

    # Define a flag to alternate between grey and white
    alternate = True

    # Create an offscreen image to draw on
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # List to store image file paths
    images = []

    # Define a function to be called when the "Choose colour" button is clicked
    def choose_color():
        color = cc.askcolor()[1]
        canvas.color = color

    # Define a function to be called when the mouse button is clicked on the Canvas widget
    def paint_pixel(event):
        x, y = event.x, event.y
        x1, y1 = x - x % pixel_size, y - y % pixel_size
        x2, y2 = x1 + pixel_size, y1 + pixel_size
        canvas.create_rectangle(x1, y1, x2, y2, fill=canvas.color)
        # Draw the same rectangle on the offscreen image
        fill_color = canvas.color
        draw.rectangle([x1, y1, x2, y2], fill=fill_color)

    # Bind the mouse button click event to the Canvas widget
    canvas.bind("<Button-1>", paint_pixel)

    # Define a function to be called when the "Save your work" button is clicked
    def save_work():
        global user
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if file_path:
            image.save(file_path, 'JPEG')
            images.append(file_path)  # Append the file path to the list
            # Append the image file path as a hyperlink to the 'pixelartss' CSV file
            with open('pixelarts.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                link = f'=HYPERLINK("{os.path.abspath(file_path)}", "Open Image")'
                csv_writer.writerow([user,link])

    # Create a grey and white grid on the canvas
    for x in range(0, width, pixel_size):
        alternate = not alternate  # Switch between grey and white
        for y in range(0, height, pixel_size):
            fill_color = '#D3D3D3' if alternate else 'white'  # Light grey
            canvas.create_rectangle(x, y, x + pixel_size, y + pixel_size, fill=fill_color)
            alternate = not alternate  # Switch again for the next row

    # Create the "Choose colour" button and place it to the right of the Canvas widget
    button_choose_color = tk.Button(frame, text='Choose colour',bg='lawn green', command=choose_color, font=('Helvetica', 15))
    button_choose_color.pack(side='right')

    # Create the "Save your work" button and place it to the right of the "Choose colour" button
    button_save_work = tk.Button(frame, text='Save your work',bg='cornflower blue', command=save_work, font=('Helvetica', 15))
    button_save_work.pack(side='right')

    # Use the geometry method of the Tkinter window to set its position and size to snap it to the left side of the screen when viewed in 1360x750 resolution
    root.geometry("+" + str(0) + "+" + str(0))
    root.geometry(str(width) + "x" + str(height))

    # Start the main loop
    root.mainloop()




    




            
    


