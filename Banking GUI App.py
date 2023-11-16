#Imports
from tkinter import *
import os #operating system-To read how many files are there for different user accounts
from PIL import ImageTk, Image # Image to show in Tkinter

#Main Screen
window=Tk()
window.title('Banking App')
window.minsize(width=200,height=300)
window.maxsize(width=500,height=500)

#Functions
def finish_reg():
    name=temp_name.get()#To get the temporary stored variable value and stores in a new variable
    age=temp_age.get()
    gender=temp_gender.get()
    password=temp_password.get()
    all_accounts=os.listdir()#To find what files are in our directory,array of all files we have
    
    if name=="" or age=="" or gender=="" or password=="":#To ask the user to fill all details
        notif.config(fg="red",bg='black',text="*All fields are required *") 
        return

#for checking the already registered user name
    for name_check in all_accounts:
        if name==name_check:
            notif.config(fg="red",bg='black',text="*Account already exists") 
            return
        else:
            new_file=open(name,"w")#"w"-in write mode-To create a new file
            new_file.write(name+'\n')#'\n'-for creating a blank line
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            new_file.write('0')#For balance(the balance the user starts with is zero)
            new_file.close()#variable.close()-To save the changes
            notif.config(fg="white",bg='green',text="Account has been created")



def register():
    #vars(variables)
    global temp_name#2 (global-To make the variable globalize(public) and use it anywhere)
    global temp_age
    global temp_gender
    global temp_password
    global notif
    
    temp_name=StringVar()#1 StringVar()-initialize an empty string variable for using somewhere
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_password=StringVar()

    #Register screen
    register_screen=Toplevel(window)#Toplevel(main screen) To create a popup window that inherits the characteristics of main window
    register_screen.title('Register')
    register_screen.maxsize(width=300,height=300)


    #Labels
    Label(register_screen,text="Please enter your details here to register",fg='white',bg='green',font=('Calibri',12)).grid(row=0,sticky=N,pady=10)#Replacing the main screen with the register_screen
    Label(register_screen,text="Name",font=('Calibri',12)).grid(row=1,sticky=W)#(sticky=W(W=West- for replacing in the left most end ))
    Label(register_screen,text="Age",font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen,text="Gender",font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen,text="Password",font=('Calibri',12)).grid(row=4,sticky=W)
    notif=Label(register_screen,font=('Calibri',12))#For showing notification
    notif.grid(row=6,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)#storing data's temporarily into a textvariable using a temp_variable
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0)#("*"-To show password hidden or censored)

    #Register Button
    Button(register_screen,text="Register",bg='green',command=finish_reg,font=('Calibri',12)).grid(row=5,sticky=N,pady=10)

#Function
def login_session():
    global login_name#making the variable public 
    all_accounts=os.listdir()#To return all the files in our directory
    login_name=temp_login_name.get()
    login_password=temp_login_password.get()

    #to look for all the names in our directory
    for name in all_accounts:
        if name==login_name:
            #to check the correct password
            file=open(name,"r")#"r"-to open in read mode
            file_data=file.read()#its gonna include all the data's inside the file
            file_data = file_data.split('\n')#To overwrite the file data with an array of each field of information included in "file"
                                             #Its going to have a each value on a different line,store it in a array as soon the new line is detected
            password=file_data[3]#assigning the password from the list[lee,24,male,password](password=3rd index in the list)

            # Creating an Account Dashboard
            if login_password==password:
                login_screen.destroy()#To destroy the login screen and to open the new window(Account Dashboard)
                account_dashboard=Toplevel(window)#To inherits the characteriscts of main screen
                account_dashboard.title('Dashboard')
                account_dashboard.maxsize(width=300,height=300)

                #Labels
                Label(account_dashboard,text="Account Dashboard",fg='white',bg='blue',font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard,text="Welcome "+name,fg='red',font=('Calibri',12)).grid(row=1,sticky=N,pady=5)#+name=for showing name in label
                #Buttons
                Button(account_dashboard,text="Personal Details",font=('Calibri',12),width=30,command=personal_details).grid(row=2,sticky=N,padx=10)#personal details button
                Button(account_dashboard,text="Deposit",font=('Calibri',12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)#deposit button
                Button(account_dashboard,text="Withdraw",font=('Calibri',12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)#withdraw button
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red",bg='black',text="*Incorrect password")#notification for incorrect password
                return
        
    login_notif.config(fg="red",bg='black',text="*No account found")#notification for invalid account.If the username name is wrong,it shows"No account found",because..
                                                        #.. we are creating the account with a username.

#Functions-For Dash board
def deposit():
    #Variables(global)
    global amount
    global deposit_notif# A Label for telling the status of the deposit
    global current_balance_label#for updating the current balance

    #Variables
    amount=StringVar()
    file=open(login_name,'r')#for reading file
    file_data=file.read()
    user_details=file_data.split('\n')#it will return an array which will store all the details in a separate line's
    details_balance=user_details[4]#in an array fourth(4)index is denoting balance

    #Deposit screen
    deposit_screen=Toplevel(window)
    deposit_screen.title('Deposit')
    deposit_screen.maxsize(width=300,height=300)


    #Labels
    Label(deposit_screen,text="Deposit",fg='white',bg='blue',font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label=Label(deposit_screen,text="Current Balance: ₹"+details_balance,font=('Calibri',12))#showing current balance of the user in the start
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen,text="Amount: ",font=('Calibri',12)).grid(row=2,sticky=W)#for entering the deposit amount
    deposit_notif=Label(deposit_screen,font=('Calibri',12))#for showing deposit notification
    deposit_notif.grid(row=4,sticky=N,pady=5)

    #Entry for amount
    Entry(deposit_screen,textvariable=amount).grid(row=2,column=1,padx=5)#textvariable=amount-is gonna temporarily store the amount

    #Button for amount deposit
    Button(deposit_screen,text="Finish",font=('Calibri',12),bg='green',command=finish_deposit).grid(row=3,sticky=W,pady=5,padx=5)

#Function for amount deposit
def finish_deposit():
    if amount.get()=="":#if depoist entry is blank
        deposit_notif.config(text="*Amount is required",fg="red",bg='black')
        return #since we are not using an "else statement",we should use "return".
    if float(amount.get()) <=0: #Initially we have stored the value as a sring value(StringVar) ,but we need to change it to float (decimal) to do the "math operation"
        deposit_notif.config(text="*Valid Amount is required",fg="red",bg='black')  #if the amount entered is negative number or zero 
        return #since we are not using an "else statement",we should use "return".  

    file=open(login_name,'r+') # 'r+'-To "read and write" the file for updating the balance
    file_data=file.read() 
    details=file_data.split('\n') #It will take each line and save it as an item in the array
    current_balance=details[4] # balance is in the 4th index of this array
    updated_balance = current_balance # For storing updated balance
    updated_balance = float(updated_balance) + float(amount.get()) # For updating balance # float(updated_balance)+float(amount.get())-Because we can't add number to a string
    file_data = file_data.replace(current_balance,str(updated_balance))#replacing(over writting) the file_data # replace() -It is a function that looks for a "string" and replaces it with whatever we want
                                                                           # str(updated_balance)-updated_balance should be converted to string before using in replace function
        
     #For emptying the previous file and writing the new updated data into it
    file.seek(0) # To set the current file position in a file stream
    file.truncate(0)#It resizes the file to a specified size.Here the size is zero(0),Because we want to start from zero(0)
    file.write(file_data)#To write the most recent and over written file data
    file.close()

    #For updating current balance label
    current_balance_label.config(text="Current Blance: ₹"+str(updated_balance),fg="green")#concatenation(addition)-here,[string + str(float)]- because,we cannot add a number to a string
    #For showing deposit screen notification after updation
    deposit_notif.config(text="Balance Updated",fg='white',bg='green')




def withdraw():
    #Variables(global)
    global withdraw_amount
    global withdraw_notif# A Label for telling the status of the withdraw
    global current_balance_label#for updating the current balance

    #Variables
    withdraw_amount=StringVar()
    file=open(login_name,'r')#for reading file
    file_data=file.read()
    user_details=file_data.split('\n')#it will return an array which will store all the details in a separate line's
    details_balance=user_details[4]#in an array fourth(4)index is denoting balance

    #Withdraw screen
    withdraw_screen=Toplevel(window)
    withdraw_screen.title('Withdraw')
    withdraw_screen.maxsize(width=300,height=300)


    #Labels
    Label(withdraw_screen,text="Withdraw",fg='white',bg='blue',font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label=Label(withdraw_screen,text="Current Balance: ₹"+details_balance,font=('Calibri',12))#showing current balance of the user in the start
    current_balance_label.grid(row=1,sticky=W,pady=5)
    Label(withdraw_screen,text="Withdraw Amount: ",font=('Calibri',12)).grid(row=2,sticky=W)#for entering the withdraw amount
    withdraw_notif=Label(withdraw_screen,font=('Calibri',12))#for showing withdraw notification
    withdraw_notif.grid(row=4,sticky=N,pady=5)

    #Entry for amount
    Entry(withdraw_screen,textvariable=withdraw_amount).grid(row=2,column=1,padx=5)#textvariable=amount-is gonna temporarily store the amount

    #Button for withdraw deposit
    Button(withdraw_screen,text="Finish",font=('Calibri',12),bg='green',command=finish_withdraw).grid(row=3,sticky=W,pady=5,padx=5)


#Function for amount withdraw
def finish_withdraw():
    if withdraw_amount.get()=="":#if depoist entry is blank
        withdraw_notif.config(text="*Amount is required",fg="red",bg='black')
        return #since we are not using an "else statement",we should use "return".
    if float(withdraw_amount.get()) <=0: #Initially we have stored the value as a sring value(StringVar) ,but we need to change it to float (decimal) to do the "math operation"
        withdraw_notif.config(text="*Valid Amount is required",fg="red",bg='black')  #if the amount entered is negative number or zero 
        return #since we are not using an "else statement",we should use "return".  

    file=open(login_name,'r+') # 'r+'-To "read and write" the file for updating the balance
    file_data=file.read() 
    details=file_data.split('\n') #It will take each line and save it as an item in the array
    current_balance=details[4] # balance is in the 4th index of this array

    #For checking whether the withdraw amount is greater than than the current balance
    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text='*Insufficient Fund!',fg='red',bg='black')
        return

    updated_balance = current_balance # For storing updated balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get()) # For updating balance # float(updated_balance)-float(withdraw_amount.get())-Because we can't add number to a string
    file_data = file_data.replace(current_balance,str(updated_balance))#replacing(over writting) the file_data # replace() -It is a function that looks for a "string" and replaces it with whatever we want
                                                                           # str(updated_balance)-updated_balance should be converted to string before using in replace function
        
     #For emptying the previous file and writing the new updated data into it
    file.seek(0) # To set the current file position in a file stream
    file.truncate(0)#It resizes the file to a specified size.Here the size is zero(0),Because we want to start from zero(0)
    file.write(file_data)#To write the most recent and over written file data
    file.close()

    #For updating current balance label
    current_balance_label.config(text="Current Blance: ₹"+str(updated_balance),fg='green')#concatenation(addition)-here,[string + str(float)]- because,we cannot add a number to a string
    #For showing withdraw screen notification after updation
    withdraw_notif.config(text=" Balance Updated ",fg='white',bg='green')


def personal_details():#for showing personal details to the user
    #Vars-Variables
    file=open(login_name,'r')
    file_data=file.read()
    user_details=file_data.split('\n')
    details_name=user_details[0]
    details_age=user_details[1]
    details_gender=user_details[2]
    details_balance=user_details[4]

    #Personal detail's screen
    personal_details_screen=Toplevel(window)
    personal_details_screen.title("Personal Details")
    personal_details_screen.maxsize(width= 300,height=300)


    
    #Labels
    Label(personal_details_screen,text="Personal Details",fg='white',bg='blue',font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen,text="Name: "+details_name,font=('Calibri',12)).grid(row=1,sticky=W)
    Label(personal_details_screen,text="Age: "+details_age,font=('Calibri',12)).grid(row=2,sticky=W)
    Label(personal_details_screen,text="Gender: "+details_gender,font=('Calibri',12)).grid(row=3,sticky=W)
    Label(personal_details_screen,text="Balance: ₹"+details_balance,font=('Calibri',12)).grid(row=4,sticky=W)
    

                                                         

def login():
    #Vars-Variable
    global temp_login_name #2 to make it a global variable
    global temp_login_password
    global login_notif
    global login_screen

    temp_login_name=StringVar()#1 initialize an empty string variable
    temp_login_password=StringVar()


    #Login Screen
    login_screen=Toplevel(window)
    login_screen.title('Login')
    login_screen.maxsize(width=300,height=300)

    #Labels
    Label(login_screen,text="Login to your account",fg='white',bg='black',font=('Calibric',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen,text="Username",font=('Calibric',12)).grid(row=1,sticky=W)
    Label(login_screen,text="Password",font=('Calibric',12)).grid(row=2,sticky=W)
    login_notif=Label(login_screen,font=('Calibri',12))#Login notifications
    login_notif.grid(row=4,sticky=N)

    #Entries
  
    Entry(login_screen,textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen,textvariable=temp_login_password,show="*").grid(row=2,column=1,padx=5)

    #Button
    Button(login_screen,text="Login",fg='black',bg='green',command=login_session,width=15,font=('Calibric',12)).grid(row=3,sticky=W,pady=5,padx=5)


    

#Image import
img=Image.open("D:/Python/Python projects/Banking GUI App/Bank image.png")
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)#To convert the image into Tkinter format for reading it

#Labels
Label(window,text="Custom Banking Beta",fg='white',bg='black',font=('Calibri',14)).grid(row=0,sticky=N,pady=10)#sticky=N(N-North)-(for placing exactly in center),pady=10(in y or vertical direction)
Label(window,text="The Best customer satisfactory Bank you always want ",fg='white',bg='black',font=('Calibri',12)).grid(row=1,sticky=N)
Label(window,image=img).grid(row=3,sticky=N,pady=15)#image=attribute

#Buttons
Button(window,text="Register",fg='black',bg='green',font=('Calibri',12),width=15,command=register).place(x=30,y=250)
Button(window,text="Login",fg='black',bg='green',font=('Calibri',12),width=15,command=login).place(x=195,y=250)
#Main loop
window.mainloop()