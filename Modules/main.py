from tkinter import *
from PIL import ImageTk,Image
import videos
import notes
import games
import notes
import calculator

def books() :
    return 0

def videos() :
    return 0

def calculator() :
    return 0

def games() :
    return 0

def notes() :
    return 0



root = Tk()
root.title("Learning Management System By Code Owls")
root.configure(bg="#344e5c")
root.iconbitmap("H:\Mid Sem Project\icon.ico")
root.geometry("1280x600")
    
#Basic Label
mainlabel1 = Label(root,pady=0,bg="#344e5c")
mainlabel2 = Label(root, text="",fg="blue",bg="#344e5c")
books_button = Button(root,text="Books",padx=10,pady=10,fg="blue",bg="#ffffff",command=books)
videos_button = Button(root,text="Videos",padx=10,pady=10,fg="blue",bg="#ffffff",command=videos)
games_button = Button(root,text="Games",padx=10,pady=10,fg="blue",bg="#ffffff",command=games)
notes_button = Button(root,text="Notes",padx=10,pady=10,fg="blue",bg="#ffffff",command= notes)
calculator_button = Button(root,text="Calculator",padx=10,pady=10,fg="blue",bg="#ffffff",command= calculator)

#pack in grid
mainlabel1.grid(row=0,column =0)
mainlabel2.grid(row=1,column=0)
books_button.grid(row=1,column=1)
videos_button.grid(row=1,column=2)
games_button.grid(row=1,column=4)
notes_button.grid(row=1,column=6)
calculator_button.grid(row=1,column=6)

#search box

#search=Entry(root,width=50,bg="red",fg="blue",borderwidth=35)
#search.insert(0,"Search Stuff Here")
#search_button = Button(root,text="Click here to search",padx=10,pady=5,fg="blue",bg="red",command= clickme)
#search.grid(row=4,column=0)
#search_button.grid(row=5,column=0)

root.mainloop()