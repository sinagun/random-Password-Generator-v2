from tkinter import *
from random import randint

root = Tk()
root.iconbitmap('icoforsina.ico')
root.title('sina_only_use')
root.geometry("500x300")

my_password = chr(randint(33,126))
######################################################################
# def
def new_rand():
    # ClEar our Entry Box
    pw_entry.delete(0,END)

    # Get pw length to int
    pw_length = int(my_entry.get())

    # careate a to hold password
    my_password=''

    # Loop password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    # output to screen
    pw_entry.insert(0,my_password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
######################################################################
# label frame
lf = LabelFrame(root,text="how many characters")
lf.pack(pady=20)
######################################################################
# Create Entry Box to Designate Number of characters
my_entry = Entry(lf,font=("Helvica",24))
my_entry.pack(pady=20,padx=20)
######################################################################
# Create Entry Box for our returned password
pw_entry =Entry(root,text='',font=("Helvica",24),bd=0,bg="systembuttonface")
pw_entry.pack(pady=20)
######################################################################
# Create a frame for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)
######################################################################
# Create our buttons
my_button= Button(my_frame,text="generate strong password",command=new_rand)
my_button.grid(row=0,column=0,padx=10)
clip_button = Button(my_frame,text="copy to clipboad",command=clipper)
clip_button.grid(row=0,column=1,padx=10)






















root.mainloop()


