from time import sleep
from plyer import notification
from tkinter import * 
from tkinter import ttk
import random
import string
import tkinter as tk
from tkcalendar import Calendar
from tkinter.filedialog import askopenfile , asksaveasfile
from tkinter import filedialog as f
import keyboard

# notification.notify(
#     title='Here is the title',
#     message='Here is the message',
#     app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
#     timeout=10,  # seconds
# )

    
def PWGeneratorWin():
    root.destroy()
    PWGWin = tk.Tk()
    PWGWin.title ("Password Generator")
    PWGWin.resizable(0,0)
    PWGWin.geometry("300x100")
    PWGWin.iconbitmap('favicon.ico')
    PWGWFrame = tk.Frame(PWGWin)
    PWGWFrame.pack_propagate(0)
    PWGWFrame.pack(fill=tk.BOTH , expand=0)
    
    res = ttk.Label(PWGWin , text="How many characters (enter a number)")
    res.pack()

    def PWGenerator(size):
        if int(entry.get()) > 18:
            res1.configure(text='Max chars are 18')
        elif entry.get().isdigit():
            size = int(entry.get())
        
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbol = string.punctuation
    
        all = lower + upper + num + symbol
        temp = random.sample(all, size)
        password = "".join(temp)
    
        print(password)
        res1.configure(text="Your password is : " + str(password),foreground='red')


    entry = ttk.Entry(PWGWin)
    entry.bind('<Return>',PWGenerator)
    entry.pack()
    
    res1 = ttk.Label(PWGWin)
    res1.pack()

    b1 = ttk.Button(PWGWin, text="Exit" , command=PWGWin.destroy)
    b1.pack()

    
    
    
def CRCalendar():
    root.destroy()
    
    newfile = tk.Tk()
    newfile.resizable(0,0)
    newfile.geometry("400x400")
    newfile.title("Calendar")
    newfile.iconbitmap('favicon.ico')
    
    cal = Calendar(newfile, selectedmode='day',year=2021,month=10,day=20)
    
    cal.pack()
    
    def grad_date():
        date.config(text='Selected date is: ' + cal.get_date()) 
    
    b4 = ttk.Button(newfile, text="Get date", command=grad_date)
    b4.pack(pady=10)
    
    date = ttk.Label(newfile, text="")
    date.pack(pady= 10)
    
    b3 = ttk.Button(newfile, text='Exit', command=newfile.destroy)
    b3.pack(pady= 10)
    newfile.mainloop()

def Notepad():
    root.destroy()
    
    def open_file():
        filetypes = (
            ("Text Files","*.txt"),
            ("All Files","*.*")
        )
        fo = f.askopenfile(filetypes=filetypes)
        if not fo:
            return
        txt_edit.delete(1.0,tk.END)
        txt_edit.insert(tk.END, fo.readlines())
        NPWin.title("M0nst3r Notepad")
    
    def save_file():
        # filepath = f.asksaveasfile(
        #     defaultextension="txt",
        #     filetype=[("text Files","*.txt"),
        #               ("All Files","*.*")]
        # )
        
        filetypes = (
            ("Text Files","*.txt"),
            ("All Files","*.*")
        )
        fo = f.asksaveasfile(mode="w",defaultextension="txt",filetype=filetypes)
        
        if fo is None:
            return 
        
        text2save = str(txt_edit.get(1.0 , tk.END))
        fo.write(text2save)
        fo.close()
        NPWin.title(f"M0nst3r Notepad - {fo}")
    
    NPWin = tk.Tk()
    NPWin.title("Notepad")
    NPWin.iconbitmap('favicon.ico')
    NPWin.rowconfigure(0, minsize=400, weight=1 )
    NPWin.columnconfigure(1, minsize=400, weight=1 )
    txt_edit = tk.Text(NPWin)
    NPFrame = tk.Frame(NPWin, relief=tk.RAISED, bd=2)
    NPOpen = ttk.Button(NPFrame, text="Open",command=open_file)
    NPSave = ttk.Button(NPFrame, text="Save as",command=save_file)
    NPExit = ttk.Button(NPFrame, text="Exit" , command=NPWin.destroy)
    
    
    NPOpen.grid(row=0 , column=0 ,sticky="ew", padx=5 , pady=5)
    NPSave.grid(row=1 , column=0 ,sticky="ew",padx=5 , pady=5)
    NPExit.grid(row=2 , column=0 ,sticky="ew", padx=5)
    
    NPFrame.grid(row=0 , column=0 , sticky="ns")
    txt_edit.grid(row=0 , column=1 , sticky="nsew")
    
    NPWin.mainloop()

def Clean():
    
    CWin = tk.Tk()
    CWin.title("Warning before cleaning")
    CWin.resizable(0,0)
    CWin.geometry("500x100")
    CWin.iconbitmap('favicon.ico')
    
    l1= ttk.Label( CWin ,text="Please close all applications before cleaning")
    l1.pack(pady=5)
    
    l2= ttk.Label(CWin ,text="If there is an error (File in use) , select all and then skip the remaining files")
    l2.pack(pady=5)
    
    def cont():
        CWin.destroy()
        keyboard.press_and_release('win+r')
        keyboard.write(' %temp%' , delay=0.1)
        keyboard.press_and_release('enter')
        keyboard.write('  ' , delay=0.1)
        keyboard.press_and_release('ctrl+a')
        keyboard.press_and_release('shift+delete')
        keyboard.write('  ' , delay=0.5)
        keyboard.press_and_release('enter')
        
        notification.notify(
            title='Cleaning is completed',
            message='Cached has been cleaned successfully',
            app_icon='favicon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
        )
        
        

    b1= ttk.Button(CWin,text="Next >" , command=cont)
    b1.pack()
    CWin.mainloop()

    
    

root = Tk()
root.iconbitmap('favicon.ico')
root.title('M0nst3r tools')
root.resizable(0,0)
root.geometry("300x150")
frame = ttk.Frame(root)
frame.pack_propagate(0)
frame.pack(fill=tk.BOTH, expand=0)

b1 = ttk.Button(root, text="Calendar" , command=CRCalendar)
b1.pack(pady= 5)

b2 = ttk.Button(root, text="Password Generator", command=PWGeneratorWin)
b2.pack(pady= 5)

b3 = ttk.Button(root, text="Notepad", command=Notepad)
b3.pack(pady= 5)

b4 = ttk.Button(root, text="Clean cache" , command=Clean)
b4.pack(pady= 5)

root.mainloop()
