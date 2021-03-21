from tkinter import *
from PIL import ImageTk,Image

class login:
    def __init__(self,root):
        self.root = root
        self.root.title("login system")
        self.root.geometry("1000x500+200+100")
        self.bg = ImageTk.PhotoImage(Image.open("D:\image\desktop_wallpaper.png"))
        self.bg_image = Label(self.root,image = self.bg).place(x = 0,y = 0,relwidth = 1,relheight = 1)

    #    Frame_login = Frame(self.root,bg = "white")
    #    Frame_login.place(x = 650,y = 100,width = 300,height = 200)

    #    title= Label(Frame_login,text = "Login here",font= ("Arial",20,"underline"),bg = "white",fg = "orange").place(x = 10,y = 10)


root = Tk()
obj = login(root)
root.mainloop()
